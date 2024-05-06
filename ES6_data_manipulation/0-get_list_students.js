export default function getListStudents() {
    const studentOne = { firstName: "Guillaume", id: 1, location: 'San Fransisco' };
    const studentTwo = { firstName: "James", id: 2, location: 'Columbia' };
    const studentThree = { firstName: "Serena", id: 5, location: 'San Fransisco' };

    const studentArray = {studentOne, studentTwo, studentThree};
    return studentArray;
}