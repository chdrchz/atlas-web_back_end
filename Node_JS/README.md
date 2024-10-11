# Node.js and Express Project

## Description

This project focuses on building a web server using Node.js and Express.js, along with utilizing various features of Node.js to interact with the file system, access command-line arguments, and environment variables. The project also involves using tools such as Babel for ES6 support and Nodemon to improve development workflow. All code will be tested with Jest and linted using ESLint.

## Learning Objectives

By completing this project, you will learn how to:

- Run JavaScript using Node.js
- Use Node.js modules
- Read files using a specific Node.js module
- Access command-line arguments and environment variables using `process`
- Create a small HTTP server with Node.js
- Create a small HTTP server with Express.js
- Implement advanced routes with Express.js
- Use ES6 with Node.js through Babel-node
- Speed up development with Nodemon

## Requirements

- All files will be interpreted/compiled on **Ubuntu 18.04 LTS** using Node.js version **12.x.x**
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Your code should have the `.js` extension
- Code must be tested with **Jest** using the command `npm run test`
- Code must be linted using **ESLint**
- Project must pass all tests and lint checks (`npm run full-test`)

## Provided Files

- `database.csv`: contains a list of users and their respective fields.
  ```csv
  firstname,lastname,age,field
  Johann,Kerbrou,30,CS
  Guillaume,Salou,30,SWE
  Arielle,Salou,20,CS
  Jonathan,Benou,30,CS
  Emmanuel,Turlou,40,CS
  Guillaume,Plessous,35,CS
  Joseph,Crisou,34,SWE
  Paul,Schneider,60,SWE
  Tommy,Schoul,32,SWE
  Katie,Shirou,21,CS
  ```

## Setup

1. Clone the repository.
2. Install the dependencies by running:
   ```bash
   npm install
   ```

## Running the Project

- To start the development server with ES6 support and automatic restarts:
  ```bash
  npm run dev
  ```
- To run tests:
  ```bash
  npm run test
  ```
- To run linting checks:
  ```bash
  npm run lint
  ```

## Author

- Savanna Davis
