export default function getListStudents() {
    const studentOne = {firstname: 'Guillaume', id: 1, location: 'San Fransisco'};
    const studentTwo = {firstname: 'James', id: 2, location: 'Columbia'};
    const studentThree = {firstname: 'Serena', id: 5, location: 'San Fransisco'};

    const studentArray = {studentOne, studentTwo, studentThree};
    return studentArray;
}