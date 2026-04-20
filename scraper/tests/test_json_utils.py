"""Tests for JSON utility functions."""

import json
import os
import tempfile
import unittest

from scraper.utils.json_utils import (
    extract_nested_value,
    flatten_json,
    load_json_file,
    merge_json_objects,
    safe_json_dumps,
    safe_json_loads,
    save_json_file,
)


class TestSafeJsonLoads(unittest.TestCase):
    def test_valid_json(self):
        assert safe_json_loads('{"key": "value"}') == {"key": "value"}

    def test_valid_list(self):
        assert safe_json_loads("[1, 2, 3]") == [1, 2, 3]

    def test_empty_string(self):
        assert safe_json_loads("") is None

    def test_none_input(self):
        assert safe_json_loads(None) is None

    def test_invalid_json(self):
        assert safe_json_loads("not json") is None

    def test_invalid_json_custom_default(self):
        assert safe_json_loads("not json", default=[]) == []

    def test_valid_number(self):
        assert safe_json_loads("42") == 42

    def test_type_error(self):
        assert safe_json_loads(123) is None


class TestSafeJsonDumps(unittest.TestCase):
    def test_dict(self):
        result = safe_json_dumps({"key": "value"})
        assert json.loads(result) == {"key": "value"}

    def test_list(self):
        result = safe_json_dumps([1, 2, 3])
        assert json.loads(result) == [1, 2, 3]

    def test_indent(self):
        result = safe_json_dumps({"a": 1}, indent=4)
        assert "    " in result

    def test_none(self):
        result = safe_json_dumps(None)
        assert result == "null"

    def test_non_serializable(self):
        result = safe_json_dumps(object())
        assert result == "{}"

    def test_unicode(self):
        result = safe_json_dumps({"emoji": "日本語"}, ensure_ascii=False)
        assert "日本語" in result


class TestLoadJsonFile(unittest.TestCase):
    def test_load_valid_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"key": "value"}, f)
            path = f.name
        try:
            result = load_json_file(path)
            assert result == {"key": "value"}
        finally:
            os.unlink(path)

    def test_missing_file(self):
        assert load_json_file("/nonexistent/path.json") is None

    def test_missing_file_custom_default(self):
        assert load_json_file("/nonexistent/path.json", default={}) == {}

    def test_invalid_json_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("not valid json")
            path = f.name
        try:
            assert load_json_file(path) is None
        finally:
            os.unlink(path)


class TestSaveJsonFile(unittest.TestCase):
    def test_save_dict(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = f.name
        try:
            result = save_json_file({"key": "value"}, path)
            assert result is True
            with open(path) as f:
                assert json.load(f) == {"key": "value"}
        finally:
            os.unlink(path)

    def test_save_list(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = f.name
        try:
            assert save_json_file([1, 2, 3], path) is True
        finally:
            os.unlink(path)

    def test_save_to_invalid_path(self):
        result = save_json_file({"key": "value"}, "/nonexistent_dir_xyz/file.json")
        assert result is False


class TestMergeJsonObjects(unittest.TestCase):
    def test_simple_merge(self):
        result = merge_json_objects({"a": 1}, {"b": 2})
        assert result == {"a": 1, "b": 2}

    def test_override_value(self):
        result = merge_json_objects({"a": 1}, {"a": 2})
        assert result["a"] == 2

    def test_deep_merge(self):
        obj1 = {"a": {"x": 1, "y": 2}}
        obj2 = {"a": {"y": 99, "z": 3}}
        result = merge_json_objects(obj1, obj2, deep=True)
        assert result["a"] == {"x": 1, "y": 99, "z": 3}

    def test_shallow_merge(self):
        obj1 = {"a": {"x": 1}}
        obj2 = {"a": {"y": 2}}
        result = merge_json_objects(obj1, obj2, deep=False)
        assert result["a"] == {"y": 2}

    def test_non_dict_first(self):
        result = merge_json_objects([1, 2], {"a": 1})
        assert result == {}

    def test_non_dict_second(self):
        result = merge_json_objects({"a": 1}, [1, 2])
        assert result == {"a": 1}

    def test_empty_dicts(self):
        assert merge_json_objects({}, {}) == {}


class TestExtractNestedValue(unittest.TestCase):
    def test_simple_key(self):
        assert extract_nested_value({"a": 1}, ["a"]) == 1

    def test_nested_key(self):
        data = {"a": {"b": {"c": 42}}}
        assert extract_nested_value(data, ["a", "b", "c"]) == 42

    def test_missing_key(self):
        assert extract_nested_value({"a": 1}, ["b"]) is None

    def test_missing_nested_key(self):
        assert extract_nested_value({"a": {"b": 1}}, ["a", "c"]) is None

    def test_custom_default(self):
        assert extract_nested_value({}, ["x"], default="fallback") == "fallback"

    def test_non_dict_in_path(self):
        assert extract_nested_value({"a": "string"}, ["a", "b"]) is None

    def test_empty_keys(self):
        data = {"a": 1}
        assert extract_nested_value(data, []) == data

    def test_unhashable_key_returns_default(self):
        # An unhashable key (list) triggers TypeError → except branch (lines 138-139)
        result = extract_nested_value({"a": 1}, [[]])
        assert result is None


class TestFlattenJson(unittest.TestCase):
    def test_simple(self):
        result = flatten_json({"a": 1, "b": 2})
        assert result == {"a": 1, "b": 2}

    def test_nested(self):
        result = flatten_json({"a": {"b": 1}})
        assert result == {"a_b": 1}

    def test_deeply_nested(self):
        result = flatten_json({"a": {"b": {"c": 42}}})
        assert result == {"a_b_c": 42}

    def test_custom_separator(self):
        result = flatten_json({"a": {"b": 1}}, separator=".")
        assert result == {"a.b": 1}

    def test_list_values(self):
        result = flatten_json({"a": [1, 2, 3]})
        assert "a_0" in result
        assert result["a_0"] == 1

    def test_list_with_dicts(self):
        result = flatten_json({"a": [{"x": 1}]})
        assert "a_0_x" in result

    def test_empty(self):
        assert flatten_json({}) == {}


if __name__ == "__main__":
    unittest.main()
