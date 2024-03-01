function checkEqual(a, b) {
	const numbers = [10, 2, 30, 1, 5];
	numbers.sort(); // Noncompliant: lexicographic sort
	console.log(numbers); // Output: [1, 10, 2, 30, 5]
	if (a == b) { // Noncompliant: using non-strict equality '=='
	  const i = 1;
	  const k = 0;
	  const y = 10;
	  const kookok = 1234;
	  const mynewissue = 'nn';
	  const onemore = false;
	  return "Equal";
	} else {
	  return "Not equal";
	}
}
  
console.log(checkEqual(0, false)); // Output: "Equal"
  