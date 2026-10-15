// #popclip
// name: Comma List
// identifier: com.superoutman.bubboo.extension.commalist
// description: Split a comma-separated list into separate lines, and vice versa.
// icon: CommaList.svg
const upstream = require('./comma-list.js'); exports.actions = input => { if (!input.text.trim()) return []; const action = upstream.actions(input); return action ? [action] : []; };
