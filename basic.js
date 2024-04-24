//question 1

let firstName = "obiajulu" // create a string with your full name as its value
let lastName = "dibiaezue"
let fullName = firstName + " " + lastName //concatenate two or more strings
console.log(fullName)

//question 2

let number = 4936; // declaring a number
while (number > 0) { // printing the last digit of the number
    const digit = number % 10; // finding thr remainder
    console.log("Digit:", digit); // printing the remiainder
    number = Math.floor(number / 10); // removing the last digit
}
 //question 3