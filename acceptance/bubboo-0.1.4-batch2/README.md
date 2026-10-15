# Batch 2 acceptance — Bubboo 0.1.4 (5)

Tested on macOS 27.0.1 arm64 with the unmodified signed/notarized release executable:
`b8a27108ca88f6af06a742686229bf28ad85757dd67e67ed4f6115312b5e6372`.
No new main App release or runtime change was required.

| Extension | Curated version | Minimum Bubboo | Scope |
| --- | --- | --- | --- |
| Title Case | 0.1.0 | 0.1.4 | Original English title rules via system Perl. Single line, up to 10000 characters. Original leading/trailing whitespace trimming is retained. |
| Base64 | 0.1.0 | 0.1.4 | Standard padded encode, URL-safe unpadded encode, and strict UTF-8 decode. Three action buttons replace upstream variant/padding options; not full option parity. |

Both are clearly identified adaptations with separate Bubboo identifiers, original `.popclipext` packaging, upstream source files, authors and MIT notices preserved. Source preservation hashes are in `upstream-preservation.json`; Title Case includes its additional upstream MIT license.

- Final `.popclipextz` archives were re-imported through the running App; both installed trees match their source packages and existing approval is retained for unchanged content.
- Real App import, explicit enable, TextEdit selection, floating-toolbar AXPress, and actual document replacement: 15 final GUI cases passed (`gui-results.json`). Covers title rules, Unicode/emoji, multiline Base64, both encoding variants, decoding, invalid input, and multiline title rejection.
- Invalid Base64 shows the App's failure alert and leaves the document unchanged. The alert is dismissed before continuing; no stale-toolbar result is counted as successful.
- Host regex filtering did not hide the multiline title action on this tested system. The adapter therefore independently rejects multiline/oversized input without output. This is intentional failure behavior; do not claim automatic hiding or multiline title support. Base64 validation likewise does not rely on toolbar filtering.
- Local adapter tests cover empty input, padding, UTF-8, URL-safe characters, line breaks, shell metacharacters, malformed and non-canonical encoding, invalid UTF-8, control characters and title length (`adapter-results.json`). Reproduce on macOS: `python3 scripts/test_adapters.py`.
- Production executor integration: 12 checks passed for switched-app / noneditable-target copy fallback and untrusted execution rejection (`executor-results.json`). This uses injected focus fixtures and a real isolated named pasteboard; GUI replacement is separately evidenced above.
- Only synthetic text was used. No target note/task accounts, external services, secrets or private application source code are included.

System Perl and its bundled MIME::Base64 / Encode modules were used; no Homebrew, pip, npm or network dependencies. macOS 14 and Intel were not physically tested. Other initial matrix candidates remain deferred; Things 3 is still skipped.
