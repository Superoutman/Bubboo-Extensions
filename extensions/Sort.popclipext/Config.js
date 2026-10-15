// #popclip
// name: Sort
// identifier: com.superoutman.bubboo.extension.sort
// description: Sort the selected lines alphabetically.
// icon: sort.png
exports.action = input => {
const lines = input.text.match(/[^\r\n]+/g) || []
lines.sort((a, b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' }))
popclip.pasteText(lines.join('\n'))

};
