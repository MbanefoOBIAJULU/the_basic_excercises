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

//question 4

console.log('5' + 10)  //its a string concatenation.

//question 5

console.log(parseInt('5') + 10); // explicit coercion.

//question 6

console.log(`The value of ${Number('5')} + 10 is ${Number('5') + 10}.`);

//question 7 

let foo = ['a', 'b', 'c','d'];
console.log(foo.length);  // => 4
console.log(foo[5]);      // will this result in an error?
// javascript doesnt return an error message like other languages

//question 8
//Create an array named names that contains a list of pet names

names = ['uloma', 'chuka', 'ken', 'collins', 'obi'];

//question 9

let pets = {
    "Fluffy": "Cat",
    "Buddy": "Dog",
    "Nibbles": "Rabbit"
};

//question 10 

'foo' === 'Foo' // case is different , its False

//question 11
//What value does the following expression evaluate to?

parseInt('3.1415') // = 3. 

//question 12
//What value does the following expression evaluate to?

'12' < '9' // false


