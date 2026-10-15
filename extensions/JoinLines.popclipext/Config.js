// #popclip
// name: Join Lines
// identifier: com.superoutman.bubboo.extension.joinlines
// description: Replace line breaks with spaces.
// icon: JoinLines.svg
const upstream = require('./join-lines.js'); exports.action = input => popclip.pasteText(upstream.action(input));
