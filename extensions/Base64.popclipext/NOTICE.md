# Attribution

Upstream authors: Nicholas Moore and contributors

Source: https://github.com/pilotmoon/PopClip-Extensions/tree/a8d8d085f61fe8624b8eed49883324213b4f43f4/source/Base64.popclipext

Upstream license: MIT (LICENSE.txt). Original credits and sources are retained.

Bubboo packaging maintainer: Superoutman.

Changes:
- Preserve original Config.json in upstream/ and retain base64.js/base64.ts unchanged. Adapt the JSON manifest to explicit shell actions supported by Bubboo 0.1.4.
- Use system Perl MIME::Base64 and Encode for UTF-8 conversion, with strict invalid-input rejection. No external dependencies or network.
- Provide Standard Encode (padded), URL-safe Encode (unpadded), and Decode as separate buttons, replacing the upstream variant/padding options. Decode accepts both variants; arbitrary variant/padding combinations are not exposed.
- Use a Bubboo-maintained identifier.

Decode intentionally rejects malformed/non-canonical input, Unicode noncharacters rejected by system Encode, and control characters other than tab/newline/carriage return. Failure leaves the selection untouched.
