export default class HolbertonCourse {
  // constructor method for obj creation
  constructor(name, length, students) {
    // verify name
    if (typeof name !== 'string' || name.trim().length === 0) {
      throw new Error('Name must be a non-empty string');
    }

    // verify length
    if (typeof length !== 'number' || length <= 0) {
      throw new Error('Length must be a positive number');
    }

    // verify students
    if (!Array.isArray(students) || students.some((student) => typeof student !== 'string' || student.trim().length === 0)) {
      throw new Error('Students must be a non-empty array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  // getters
  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  // setters
  set name(newName) {
    if (typeof newName !== 'string' || newName.trim().length === 0) {
      throw new Error('Name must be a non-empty string');
    }
    this._name = newName;
  }

  set length(newLength) {
    if (typeof newLength !== 'number' || newLength <= 0) {
      throw new Error('Length must be a positive number');
    }
    this._length = newLength;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents) || newStudents.some((student) => typeof student !== 'string' || student.trim().length === 0)) {
      throw new Error('Students must be an array with non empty strings');
    }
    this._students = newStudents;
  }
}
