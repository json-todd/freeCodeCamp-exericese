let hello = "   Hello, World!  ";
let wsRegex = /(\s)+\1/g; // Change this line
let match = hello.match(wsRegex)
let result = hello.replace(wsRegex,''); // Change this line

console.log(match)
console.log(result)