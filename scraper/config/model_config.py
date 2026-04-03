"""Model configuration management."""

import os
from pathlib import Path
from typing import Dict, Optional

import yaml


class ModelConfig:
    """Manages model configurations for different summarization modes."""

    def __init__(self, config_path: Optional[str] = None):
        """Initialize model configuration.

        Args:
            config_path: Path to the models.yaml config file.
                        If not provided, uses default location.
        """
        if config_path is None:
            # Default to config/models.yaml in the same directory
            config_dir = Path(__file__).parent
            config_path = config_dir / "models.yaml"

        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """Load configuration from YAML file."""
        if not self.config_path.exists():
            # Return default config if file doesn't exist
            return self._get_default_config()

        try:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Warning: Failed to load model config from {self.config_path}: {e}")
            return self._get_default_config()

    def _get_default_config(self) -> Dict:
        """Return default configuration if config file is not available."""
        return {
            "quality": {
                "default_model": "gemma3n:latest",
                "fallback_model": "llama3.2:1b"
            },
            "fast": {
                "default_model": "tinyllama:latest",
                "fallback_model": "tinyllama:1.1b"
            },
            "ci": {
                "primary_model": "llama3.2:1b",
                "fallback_model": "tinyllama:1.1b"
            },
            "digest": {
                "default_model": "gemma3:27b",
                "fallback_model": "llama3.2:1b"
            },
            "anthropic": {
                "default_model": "claude-3-haiku-20240307",
                "premium_model": "claude-3-opus-20240229"
            }
        }

    def get_model_for_mode(self, mode: str) -> str:
        """Get the default model for a given mode.

        Args:
            mode: The summarization mode ('quality', 'fast', 'ci', 'anthropic')

        Returns:
            The model name for the specified mode
        """
        mode_config = self.config.get(mode, {})
        return mode_config.get("default_model", "tinyllama:latest")

    def get_fallback_model(self, mode: str) -> str:
        """Get the fallback model for a given mode.

        Args:
            mode: The summarization mode ('quality', 'fast', 'ci', 'anthropic')

        Returns:
            The fallback model name for the specified mode
        """
        mode_config = self.config.get(mode, {})
        return mode_config.get("fallback_model", "tinyllama:1.1b")

    def get_ci_model(self) -> str:
        """Get the primary model for CI environment."""
        return self.get_model_for_mode("ci")

    def get_ci_fallback(self) -> str:
        """Get the fallback model for CI environment."""
        return self.get_fallback_model("ci")

    def get_anthropic_model(self, premium: bool = False) -> str:
        """Get the Anthropic API model.

        Args:
            premium: Whether to use the premium model

        Returns:
            The Anthropic model name
        """
        anthropic_config = self.config.get("anthropic", {})
        if premium:
            return anthropic_config.get("premium_model", "claude-3-opus-20240229")
        return anthropic_config.get("default_model", "claude-3-haiku-20240307")


# Global instance for easy access
_model_config = None


def get_model_config() -> ModelConfig:
    """Get the global model configuration instance."""
    global _model_config
    if _model_config is None:
        _model_config = ModelConfig()
    return _model_config
