//! ATM assignment
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let balance = 1000; //initial balance

function displayMenu() {
  console.log("Welcome to the ATM");
  console.log("1.Check Balance");
  console.log("2. Deposit Money");
  console.log("3. Withdraw Money");
  console.log("4. Exit");
  rl.question("Please select an option", handleMenuSelection);
}
function handleMenuSelection(option) {
  switch (option) {
    case "1":
      console.log(`Your current balance is $${balance.toFixed(2)}`);
      displayMenu();
      break;
    case "2":
      rl.question("Enter the amount to deposit: £", (amount) => {
        depositMoney(parseFloat(amount));
      });
      break;
    case "3":
      rl.question("Enter the amount to withdraw: £", (amount) => {
        withdrawMoney(parseFloat(amount));
      });
      break;
    case "4":
      console.log("Thank you for using the ATM. Goodbye!");
      rl.close();
      break;
      Default: console.log("Invalid Option. PLease try again");
      displayMenu();
      break;
  }
}

function depositMoney(amount) {
  if (isNaN(amount) || amount <= 0) {
    console.log("invalid amount. PLease enter a positive number");
  } else {
    balance = +amount;
    console.log(`you have successfully deposited £${amount.toFixed(2)}`);
  }
  displayMenu();
}

function withdrawMoney(amount) {
  if (isNaN(amount) || amount <= 0) {
    console.log("Invalid amount. PLease enter a smaller amount.");
  } else if (amount > balance) {
    console.log("Insufficient funds. Please enter a smaller amount");
  } else {
    balance -= amount;
    console.log(`you have successfully withdrawn £ ${aount.toFixed(2)}.`);
    console.log(`Your new balance is £${balance.toFixed(2)}.`);
  }
  displayMenu();
}
displayMenu();
