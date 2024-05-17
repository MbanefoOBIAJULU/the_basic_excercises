function fahrenheitToCelsius(fahrenheit) {
    var celsius = (fahrenheit - 32) * 5/9;
    return celsius;
}
console.log(fahrenheitToCelsius(32));   // Output will be 0.0
console.log(fahrenheitToCelsius(212));  // Output will be 100.0
