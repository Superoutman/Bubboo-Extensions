# Batch 3 acceptance — Bubboo 0.1.4 (5)

25 candidates reviewed: **16 verified, 9 blocked**. The original matrix had fewer than 20 remaining candidates, so the same criteria were applied to additional common upstream extensions. Only verified packages enter release assets and the download table.

Tested on macOS 27.0.1 arm64 with the unchanged signed/notarized Bubboo 0.1.4 (5), executable SHA256 `b8a27108ca88f6af06a742686229bf28ad85757dd67e67ed4f6115312b5e6372`. No main App rebuild or release.

- 10 real TextEdit GUI replacement cases across 8 text extensions passed: import, explicit enable, selection, floating-toolbar AXPress, document readback (`text-gui-results.json`). Covers Unicode/emoji, multiline, natural sorting, comma-list split/join and full/half width both ways.
- 12 web extensions were imported and invoked from the real toolbar; 8 displayed query-relevant browser results (`web-gui-results.json`). URL opening alone is not a pass. Only default search sites were tested; optional regional sites and IMDbPro are not certified. No purchases, login or account changes.
- 30 production executor checks passed: 10 text actions each tested with switched-app fallback, noneditable-target fallback, and untrusted execution rejection (`executor-results.json`). Injected focus fixtures and an isolated named pasteboard; real GUI replacement is separately tested. JavaScript uses the shipped signed helper; FullHalfWidth uses system Perl.
- All 16 final release archives were re-imported into the running App; installed file hashes match source trees (`archive-import-results.json`).
- Five original-matrix candidates stopped at the production parser capability gate (`parser-blocked.json`); they were not counted as completed GUI acceptance.
- Adapters remain standard PopClip `.popclipext` / `.popclipextz`, not a new format. Modified entries have Bubboo IDs, original sources preserved, and changes recorded in NOTICE/UPSTREAM. Source hashes verified in `upstream-preservation.json`; demonstration media omitted. Amazon icon: Dave Gandy, CC BY 4.0 (see package Readme/NOTICE); code MIT.
- CommaList's single dynamic action is wrapped into the array expected by Bubboo. JoinLines explicitly sends its returned string to pasteText. Reverse/Sort adapt the input API; original transformation rules remain. Host regex visibility is not asserted. macOS 14 and Intel were not physically tested.

| Candidate | Decision | Evidence / limit |
| --- | --- | --- |
| Capitalize | verified | Real TextEdit replacement passed; see text-gui-results.json. |
| SentenceCase | verified | Real TextEdit replacement passed; see text-gui-results.json. |
| JoinLines | verified | Real TextEdit replacement passed; see text-gui-results.json. |
| RemoveSpaces | verified | Real TextEdit replacement passed; see text-gui-results.json. |
| Reverse | verified | Real TextEdit replacement passed; see text-gui-results.json. |
| Sort | verified | Real TextEdit replacement passed; see text-gui-results.json. |
| CommaList | verified | Real TextEdit replacement passed; see text-gui-results.json. |
| FullHalfWidth | verified | Real TextEdit replacement passed; see text-gui-results.json. |
| GoogleImages | verified | Images results for red panda, including Wikipedia and National Geographic. |
| MDNWebDocs | blocked | Search page opened but no actual result list was visible. |
| PubMed | verified | Search results for cancer with article listings. |
| IMDb | verified | Inception (2010) and related title results. Default www.imdb.com tested; IMDbPro not tested. |
| JD | blocked | Redirected to login; no authenticated search acceptance. |
| Taobao | blocked | URL opened, but browser tool site-safety policy denied page observation; no workaround attempted. |
| Amazon | verified | Keyboard result count and product listings. Default amazon.com tested; UK option not tested. |
| Ebay | verified | Keyboard result count and item listings. Default ebay.com tested; other regional options not tested. |
| Goodreads | verified | Dune and Dune series book listings. |
| Ecosia | blocked | Redirected to Bing home without the selected query. |
| StartPage | verified | macOS web results including Apple and Wikipedia. |
| UrbanDictionary | verified | hello definition entries. |
| WordCount | blocked | Production parser rejects unsupported display token. |
| Bear | blocked | Production parser rejects unsupported macOS Service action. |
| Drafts | blocked | Production parser rejects unsupported macOS Service action. |
| Reminders | blocked | Production parser cannot find a supported configuration. |
| ChatGPTWebsite | blocked | Production parser rejects TypeScript entry. |
