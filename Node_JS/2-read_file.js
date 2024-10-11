import fs from 'fs';

export function countStudents(path) {
    try {
        // Read the file synchronously
        const data = fs.readFileSync(path, 'utf-8');

        // Split the data into lines, handle different line endings
        const lines = data.split(/\r?\n/).filter(line => line.trim() !== ''); // Ignore empty lines
        const students = lines.slice(1); // Skip the first line (headers)

        if (students.length === 0) {
            console.log('No students found in the file');
            return;
        }
 
        console.log(`Number of students: ${students.length}`);
        const fields = {};

        // Process each student
        students.forEach((student) => {
            const [firstname, lastname, age, field] = student.split(',');

            // Trim whitespace in case the CSV contains extra spaces
            const cleanFirstname = firstname.trim();
            const cleanField = field.trim();

            // Initialize field array if it doesn't exist
            if (!fields[cleanField]) {
                fields[cleanField] = [];
            }

            // Add student's first name to the field
            fields[cleanField].push(cleanFirstname);
        });

        // Log the number of students in each field and their names
        for (const field in fields) {
            const fieldStudents = fields[field];
            console.log(`Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}`);
        }

    } catch (err) {
        throw new Error("Cannot load the database");
    }
}