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
 //identify the data types of the following
 boy = 'true'
 console.log(typeof('boy')) // its a string
 
 boy = false
 console.log(typeof(boy)) // its a boolean

 boy = 1.5
 console.log(typeof(boy)) // its a number

 boy = 2
 console.log(typeof(boy)) // its a number

 boy = undefined
 console.log(typeof(boy)) //its undefined

boy = {foo: "bar."}
console.log(typeof(boy)) // its an object