// Nested JavaScript file for testing recursive inclusion
function greetUser(name) {
    console.log(`Hello, ${name}! This is from nested_file.js`);
}

// Export for module usage
module.exports = { greetUser };