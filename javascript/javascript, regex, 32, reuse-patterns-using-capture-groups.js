let repeatNum = "42 42 42";
let reRegex = /^(\d+)(\s)\1\2\1$/g; // Change this line
let result = reRegex.test(repeatNum);
let match = repeatNum.match(reRegex);

console.log(result);
console.log(match);