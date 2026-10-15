// #popclip
// name: Remove Spaces
// identifier: com.superoutman.bubboo.extension.removespaces
// description: Remove spaces from the selected text.
// icon: remspace.png
exports.action = input => popclip.pasteText(input.text.replace(/\s/g, ''));
