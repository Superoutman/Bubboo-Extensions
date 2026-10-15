// #popclip
// name: Reverse
// identifier: com.superoutman.bubboo.extension.reverse
// description: Reverse the order of the selected lines.
// icon: reverse.png
exports.action = input => {
const lines = input.text.match(/[^\r\n]+/g) || []
lines.reverse()
popclip.pasteText(lines.join('\n'))

};
