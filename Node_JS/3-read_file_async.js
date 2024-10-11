import fs from 'fs';

export function countStudents(path) {
    return new Promise((resolve, reject) => {
        // Attempt to read the file asynchronously
        fs.readFile(path, 'utf-8', (err, data) => {
            if (err) {
                // If an error occurs, reject the Promise with a custom error
                reject(new Error('Cannot load the database'));
                return;
            }

            // Split the data into lines, filtering out empty lines
            const lines = data.split('\n').filter(line => line.trim() !== '');
            const students = lines.slice(1); // Skip the first line (headers)

            if (students.length === 0) {
                console.log('No students found in the file');
                return; // No need to call resolve here
            }

            console.log('After!');
            console.log(`Number of students: ${students.length}`);

            const fields = {};

            // Process each student
            students.forEach((student) => {
                const [firstname, lastname, age, field] = student.split(',').map(entry => entry.trim());

                if (!fields[field]) {
                    fields[field] = [];
                }

                fields[field].push(firstname);
            });

            // Log the number of students per field and their names
            for (const field in fields) {
                const fieldStudents = fields[field];
                console.log(`Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}`);
            }

            console.log('Done!');
            resolve();
        });
    });
}