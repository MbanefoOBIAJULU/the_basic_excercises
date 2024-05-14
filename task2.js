//Create a function that will be able to convert figures from Fahrenheit to Celsius.

function fahrenheitToCelsius(fahrenheit) {
    var celsius = (fahrenheit - 32) * 5/9;
    return celsius;
}
console.log(fahrenheitToCelsius(32));   // Output will be 0.0
console.log(fahrenheitToCelsius(212));  // Output will be 100.0

/*Write a function min(x,y) which returns the least of two numbers x and y.
Eg. min(6, 3) == 3*/

function min(x, y) {
    return x < y ? x : y;
}

// Example usage:
console.log(min(6, 3)); // Output: 3
console.log(min(-2, 5)); // Output: -2
console.log(min(10, 10)); // Output: 10


/*Create a function that checks if a number, n is divisible by two numbers x and y.
 All inputs are positive, non-zero digits.*/

 function isDivisible(n, x, y) {
    return n % x === 0 && n % y === 0;
}

// Example usage:
console.log(isDivisible(10, 2, 5));  // Output: true (10 is divisible by both 2 and 5)
console.log(isDivisible(12, 3, 4));  // Output: true (12 is divisible by both 3 and 4)
console.log(isDivisible(7, 2, 3));   // Output: false (7 is not divisible by 2 and 3)

//Create a function that will output the first 100 prime numbers.

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

// Example usage:
console.log(generatePrimes(10)); // Output: an array containing the first 100 prime numbers

//Create a function that will return a boolean specifying if a number is a prime number.


//Write a function called toUppercase that takes a string and returns that string with only the first letter capitalized. Make sure that it can take strings that are lowercase, UPPERCASE or BoTh.


/*The marketing team is spending way too much time typing in hashtags. Let’s create a hashtag generator for them, our hashtag generator will meet the following criteria; 
It must start with a hash symbol, #.
Ignore all spaces in the input.
All words must have their first letter capitalized.
If the final result is going to be longer than 140 characters, it should return false.
If the input or result is an empty string, it should return false.
*/