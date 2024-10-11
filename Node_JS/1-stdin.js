import readline from 'readline';

// Create an interface
const read = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Prompt the user
read.question("Welcome to Holberton School, what is your name?\n", (name) => {
    console.log(`Your name is: ${name}`);
    console.log("This important software is now closing");
    read.close();
})