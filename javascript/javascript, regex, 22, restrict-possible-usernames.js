let username = "Oceans11";
let userCheck = /^[A-Za-z]([A-Za-z]+|\d(?=\d+))\d*$/g; // Change this line
let result = userCheck.test(username);
let match = username.match(userCheck);

console.log(result);
console.log(match)