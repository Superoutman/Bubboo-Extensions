# Attribution

Upstream authors: John Gruber; Aristotle Pagaltzis; Nicholas Moore and contributors

Source: https://github.com/pilotmoon/PopClip-Extensions/tree/a8d8d085f61fe8624b8eed49883324213b4f43f4/source/TitleCase.popclipext

Upstream license: MIT (LICENSE.txt). Original credits and sources are retained.

Bubboo packaging maintainer: Superoutman.

Changes:
- Keep Config.yaml and titlecase.pl unchanged; add a PopClip Config.plist and zsh wrapper to pass text safely to the original Perl stdin.
- Use a Bubboo-maintained identifier. English title rules and original whitespace behavior are retained.
- Accept single-line selections up to 10000 characters. A wrapper rejects multiline/oversized input without output; do not rely on host regex filtering to hide the button.

Additional upstream MIT notice: [ap/titlecase LICENSE](https://github.com/ap/titlecase/blob/f152120e1e4ebebee6c6be06f3ddf03b86b35d06/LICENSE), included as TITLECASE-LICENSE.txt.
