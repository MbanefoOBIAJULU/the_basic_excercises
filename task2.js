 /*Question 1
 Create a function that will be able to convert figures from Fahrenheit to Celsius.*/

function fahrenheitToCelsius(fahrenheit) {
    var celsius = (fahrenheit - 32) * 5/9;
    return celsius;
}
console.log(fahrenheitToCelsius(32));   // FarToCel (0.0)
console.log(fahrenheitToCelsius(212));  //  FarToCel (100.0)

/*Question 2
Write a function min(x,y) which returns the least of two numbers x and y.
Eg. min(6, 3) == 3*/

function min(x, y) {
    return x < y ? x : y;
} 
console.log(min(6, 3)); // Min (3)
console.log(min(-2, 5)); // Min (-2)
console.log(min(10, 10)); // Min (10)


/*Question 4
Create a function that checks if a number, n is divisible by two numbers x and y.
 All inputs are positive, non-zero digits.*/

 function isDivisible(n, x, y) {
    return n % x === 0 && n % y === 0;
}

/*Question 5
Example usage:*/
console.log(isDivisible(10, 2, 5));  // Output: true (10 is divisible by both 2 and 5)
console.log(isDivisible(12, 3, 4));  // Output: true (12 is divisible by both 3 and 4)
console.log(isDivisible(7, 2, 3));   // Output: false (7 is not divisible by 2 and 3)

/*Question 6
Create a function that will output the first 100 prime numbers.*/

function generatePrimes(count) {
    let primes = [];
    let num = 2; // Starting from 2, the first prime number

    while (primes.length < count) {
        if (isPrime(num)) {
            primes.push(num);
        }
        num++;
    }

    return primes;
}

function isPrime(n) {
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    if (n % 2 === 0 || n % 3 === 0) {
        return false;
    }
    let i = 5;
    while (i * i <= n) {
        if (n % i === 0 || n % (i + 2) === 0) {
            return false;
        }
        i += 6;
    }
    return true;
}

/*Question 7
Example usage:*/
console.log(generatePrimes(100)); // Output: an array containing the first 100 prime numbers

//Create a function that will return a boolean specifying if a number is a prime number.

function isPrime(number) {
    // Check if number is less than 2
    if (number < 2) {
        return false;
    }
    // Check for divisibility by numbers from 2 to the square root of the number
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            return false; // Not a prime number
        }
    }
    return true; // Prime number
}

// Example usage:
console.log(isPrime(7)); // Output: true
console.log(isPrime(10)); // Output: false

/*Write a function called toUppercase that takes a string and returns that 
string with only the first letter capitalized. Make sure that it can take 
strings that are lowercase, UPPERCASE or BoTh.*/

function toUppercase(str) {
    if (typeof str !== "string" || str.length === 0) {
        return ""; // Return an empty string if input is not a string or is empty
    }
    
    // Convert the first character to uppercase and concatenate it with the rest of the string
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

// Example usage:
console.log(toUppercase("hello")); // Output: "Hello"
console.log(toUppercase("WORLD")); // Output: "World"
console.log(toUppercase("bOTh"));  // Output: "Both"


/*The marketing team is spending way too much time typing in hashtags.
 Let’s create a hashtag generator for them, our hashtag generator will meet the following criteria; 
It must start with a hash symbol, #.
Ignore all spaces in the input.
All words must have their first letter capitalized.
If the final result is going to be longer than 140 characters, it should return false.
If the input or result is an empty string, it should return false.
*/
function generateHashtag(s) {
    // Check if the input string is empty or consists of only spaces
    if (!s.trim()) {
        return false;
    }

    // Remove spaces and capitalize the first letter of each word
    const words = s.split(/\s+/);
    const hashtag = '#' + words.map(word => word.charAt(0).toUpperCase() + word.slice(1)).join('');

    // Check if the length of the hashtag is within the limit
    if (hashtag.length > 140) {
        return false;
    }

    return hashtag;
}

// Example usage:
const inputString = "create a hashtag generator for marketing team";
console.log(generateHashtag(inputString));
