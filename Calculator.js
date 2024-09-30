//!Calculator assignment.
const readline = require("readline");

// Create an interface to read from the terminal
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Function to calculate
function calculate(num1, num2, operator) {
  switch (operator) {
    case "+":
      return num1 + num2;
    case "-":
      return num1 - num2;
    case "*":
      return num1 * num2;
    case "/":
      if (num2 === 0) {
        return "Error: Division by zero!";
      }
      return num1 / num2;
    default:
      return "Error: Unsupported operator!";
  }
}

rl.question("Enter first number: ", (input1) => {
  const num1 = parseFloat(input1);
  if (isNaN(num1)) {
    console.log("Error: Invalid number!");
    rl.close();
    return;
  }

  rl.question("Enter operator (+, -, *, /): ", (operator) => {
    rl.question("Enter second number: ", (input2) => {
      const num2 = parseFloat(input2);
      if (isNaN(num2)) {
        console.log("Error: Invalid number!");
        rl.close();
        return;
      }

      const result = calculate(num1, num2, operator);
      console.log(`Result: ${result}`);
      rl.close();
    });
  });
});
//! simple calculator
/*function add(a, b) {
  return a + b;
}
console.log(add(2, 5));

function subtract(a, b) {
  return a - b;
}
console.log(subtract(2, 5));

function mulitply(a, b) {
  return a * b;
}
console.log(mulitply(5, 10));

function divide(a, b) {
  return a / b;
}
console.log(divide(10, 2));*/
