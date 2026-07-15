---
title: How I made a Rust hot path 27x faster, and the AI fix I refused to merge - DEV Community
url: https://dev.to/zacharylee/how-i-made-a-rust-hot-path-27x-faster-and-the-ai-fix-i-refused-to-merge-3llg
date: 2026-07-14
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-07-16T03:39:41.270869
---

# How I made a Rust hot path 27x faster, and the AI fix I refused to merge - DEV Community

# How I made a Rust hot path 27x faster, and the AI fix I refused to merge

## Background
- KeyEcho is a desktop app that plays a mechanical‑keyboard sound on each key press.  
- After two years of maintenance‑free use, version 0.0.5 was released in July 2024.  
- The author returned in 2024 and delivered version 1.0 in a single PR (130 files, ~11 k lines added, ~9 k lines removed).

## Hot‑path description
- A global keyboard hook enqueues the first key‑down of each press.  
- An audio thread dequeues events, maps the key to a slice of the selected sound pack, and plays it.  
- Anything left in this path (decoding, allocation, copying, locking) is paid on every keystroke.

## v0.0.5 performance and limitations
- Already fast: Tauri + Rust, small binary, lossless WAV, LRU cache for decoded audio.  
- Still copied ~66 KiB of samples per key and used a global mutex for pack switching and volume.  
- Cache misses caused on‑the‑fly decoding.

## Rebuild strategy (four moves)
1. **Pre‑decode when a pack is selected**  
   - Each sound pack (folder with `asound.ogg` and `config.json`) is fully decoded once at load time.  
2. **Deduplicate identical slices**  
   - Keys sharing the same `[start_ms, duration_ms]` reuse a single `AudioSource` stored in an `Arc<[f32]>`.  
3. **Zero‑copy playback**  
   - Lookup returns a clone of the `Arc`, which only bumps the reference count; no sample data is copied.  
4. **Drop the global mutex**  
   - Current sound is held in an `ArcSwapOption<KeySound>` and volume in an `AtomicU32`.  
   - Lookups become lock‑free loads.

### Guardrails for pre‑decoding
- Bounded event queue provides back‑pressure during bursts.  
- Pack size limited to 10 MiB of decoded samples; oversized packs are rejected.

## Benchmarks
| Path | v0.0.5 | v1.0 | Speed change |
|------|--------|------|--------------|
| Cached lookup, average slice | 1184 ns/op, 66.84 KiB copied | 43.5 ns/op, 0 bytes copied | 27.2× faster |
| Cached lookup, largest slice | 1638 ns/op, 98.88 KiB copied | 43.1 ns/op, 0 bytes copied | 38.0× faster |
| Press/release gate | 58.8 ns/tap, 2 messages | 54.7 ns/tap, 1 message | half the messages |

*Benchmarks are micro‑benchmarks of the lookup path, not full speaker latency.*

## Why Rust made this safe
- The borrow checker and type system act as the first reviewer for AI‑generated code.  
- Errors such as incorrect aliasing or missing `Send/Sync` bounds are caught at compile time, preventing unsafe runtime behavior.

## Role of the AI agent
- Assisted with Tauri 1→2 migration (config, permissions, updater, plugins).  
- Audited the old playback path and guided the pre‑decode, shared‑buffer, lock‑free redesign.  
- Triaged the backlog, identifying high‑value issues (including a paid request that became the first paying customer).  
- Enforced disciplined benchmarking and documentation.  
- The author gave high‑level goals; the agent performed the detailed work and verification.

## The change that looked clean but wasn’t merged
- CI for Linux armv7 failed because `libgit2` could not fetch a git dependency.  
- The agent suggested dropping the git pin on the audio crate and using the crates.io release, which fixed CI.  
- The author rejected it because the pinned version (`cpal` 0.18) provides default‑device rerouting needed for seamless audio output when headphones are unplugged or a Bluetooth speaker is switched.  
- Keeping the pin preserves this functionality, even though the fix would have made CI pass.