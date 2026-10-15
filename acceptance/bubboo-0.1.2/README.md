# Bubboo 0.1.2 compatibility acceptance

All 13 curated extensions passed actual TextEdit selection → Bubboo toolbar click → replacement or browser destination on the **Release build of Bubboo 0.1.2 (build 3)**. Minimum supported Bubboo version for this collection is **0.1.2**. Things 3 remains excluded.

[Download Bubboo 0.1.2](https://github.com/Superoutman/Bubboo/releases/tag/v0.1.2).

Environment: macOS 27.0.1, Apple Silicon, TextEdit and Chrome. macOS 14 is the deployment target, not a separately tested machine. Final executable SHA-256: `c346ef5ee8942ef1b1557adf2e92d62e087939f5ddc0a7a5686a6ceaac438926`.

- [Actual actions and outputs](gui-results.json): uppercase, lowercase, URL encode/decode, character count and nine browser actions.
- [Settings options](gui-options-results.json): Google, Translate, Maps and Wikipedia changed the next action URL and were restored to defaults.
- Browser destinations retained the Chinese and `&` query; Translate showed `Bubboo Chinese & test`, and the Maps Shanghai check showed 上海市. No challenge page was encountered.
- The official optimized build exposed an output-reader lifetime bug absent from Debug. Bubboo 0.1.2 fixes it; all 94 tests passed under both Debug and Release, along with 47 core checks. GUI acceptance was rerun against the fixed build.
- Original package contents and attribution are unchanged from the earlier collection. The original smoke/boundary evidence remains in [2026-10-15.md](../2026-10-15.md); it is historical development-build evidence, not substituted for this release regression.

This validates the listed paths, not every remote site's regional/account configuration. Upstream formats and licenses remain intact. Collection release v0.1.1 updates compatibility metadata; individual extension package versions remain 0.1.0 because their files have not changed.
