let sampleWord = "8pass99";
let pwRegex = /(?=\w{6,})(?=\D*\d{2,})/; // Change this line
let result = pwRegex.test(sampleWord);
let match = sampleWord.match(pwRegex);
console.log(result)
console.log(match)