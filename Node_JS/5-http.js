import express from 'express';
import http from 'http';
import fs from 'fs';
import { promisify } from 'util';

const readFile = promisify(fs.readFile);
const app = express();
const port = 1245;

// Helper function to read and process the student data
async function countStudents(path) {
    try {
        const data = await readFile(path, 'utf-8');
        const lines = data.split('\n').filter(line => line.trim() !== '');
        const students = lines.slice(1); // Skip the header row

        if (students.length === 0) {
            return 'No students found in the file';
        }

        let totalStudents = students.length;
        let output = `Number of students: ${totalStudents}\n`;

        const fields = {};

        students.forEach((student) => {
            const [firstname, , , field] = student.split(',').map(entry => entry.trim());

            if (!fields[field]) {
                fields[field] = [];
            }

            fields[field].push(firstname);
        });

        for (const field in fields) {
            const fieldStudents = fields[field];
            output += `Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}\n`;
        }

        return output.trim();
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

// Create an HTTP service
http.createServer(app).listen(port, () => {
    console.log(`Server running on port ${port}`);
});

// Define route for '/'
app.get("/", (req, res) => {
    res.send("Hello Holberton School!");
});

// Define route for '/students'
app.get("/students", async (req, res) => {
    const databasePath = process.argv[2]; // Path to the CSV file passed as a command-line argument

    try {
        const studentList = await countStudents(databasePath);
        res.send(`This is the list of our students\n${studentList}`);
    } catch (error) {
        res.send("This is the list of our students\nCannot load the database");
    }
});
