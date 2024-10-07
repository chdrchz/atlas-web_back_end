# MySQL Project: Constraints, Indexes, Stored Procedures, Views, and Triggers

## Table of Contents

1. [General Overview](#general-overview)
2. [Project Objectives](#project-objectives)
3. [Requirements](#requirements)
4. [File Structure](#file-structure)
5. [How to Run the SQL Scripts](#how-to-run-the-sql-scripts)
6. [Learning Objectives](#learning-objectives)
7. [Resources](#resources)

## General Overview

This project focuses on implementing advanced features in MySQL 8.0 such as constraints, indexes, stored procedures, functions, views, and triggers. Each SQL file is written with proper comments explaining the task, and follows best practices for SQL syntax, including the use of uppercase keywords and maintaining proper file structure.

## Project Objectives

By the end of this project, you should be able to explain the following concepts without relying on external references:

- How to create tables with constraints.
- How to optimize queries by adding indexes.
- How to implement stored procedures and functions in MySQL.
- How to implement views in MySQL.
- How to implement triggers in MySQL.

## Requirements

- All files will be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0**.
- Each SQL file must end with a new line.
- Every SQL query must have a comment just before it, explaining the purpose of the query.
- All files should start with a comment describing the task being performed.
- SQL keywords such as `SELECT`, `WHERE`, `INSERT`, etc., should always be written in **UPPERCASE**.
- A `README.md` file at the root of the project folder is mandatory.
- The length of each file will be tested using the `wc` command.

## How to Run the SQL Scripts

1. Ensure that **MySQL 8.0** is installed and running on **Ubuntu 20.04 LTS**.
2. Open a terminal and log in to MySQL:
   ```bash
   sudo mysql -uroot -p
   ```
3. To execute a script, use the following command:
   ```bash
   SOURCE /path/to/your_script.sql;
   ```
4. Ensure that your script files are properly formatted and contain comments before each SQL query.

## Learning Objectives

### Creating Tables with Constraints:

- How to define **primary keys**, **foreign keys**, **unique constraints**, and **default values** in MySQL tables.

### Optimizing Queries with Indexes:

- How to create and use **indexes** to improve query performance.

### Stored Procedures and Functions:

- Understanding the difference between **stored procedures** and **functions**, and how to create them in MySQL.

### Views in MySQL:

- What are **views** and how to implement them for simplifying query structures.

### Triggers in MySQL:

- How to use **triggers** to automate tasks in response to table events such as `INSERT`, `UPDATE`, or `DELETE`.

## Resources

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Official MySQL Tutorial](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/)
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
