#!/usr/bin/node

const num = process.argv[2];
const nu = parseInt(num);

// Define a function to calculate the factorial
function fact (n) {
  // Use isNaN() to check if n is not a number, not typeof n === NaN
  if (isNaN(n)) {
    return 1;
  } else if (n < 0) {
    return 'Factorial is not defined for negative numbers.';
  } else if (n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

// Call the fact function to calculate the factorial
const factorial = fact(nu);

// Check if the result is a number before printing it
if (typeof factorial === 'number') {
  console.log(factorial);
} else {
  console.error(factorial); // Print error message for invalid input
}
