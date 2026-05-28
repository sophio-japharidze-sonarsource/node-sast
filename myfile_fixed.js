function checkEqual(a, b) {
  const numbers = [10, 2, 30, 1, 5];
  numbers.sort((a, b) => (a - b)); // Noncompliant: lexicographic sort
  console.log(numbers); // Output: [1, 10, 2, 30, 5]
  // TODO fix this
  if (a === b) {
    return "Equal";
  } else {
    return "Not equal";
  }
}

console.log(checkEqual(0, false)); // Output: "Not equal"
