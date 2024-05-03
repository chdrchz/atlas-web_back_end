export default class HolbertonCourse {
  // constructor method for obj creation
  constructor (name, length, students) {
    // verify name
    if (typeof name !== 'string' || name.trim().length === 0) {
      throw new Error('Name must be a non-empty string');
    }

    // verify length
    if (typeof length !== 'number' || length <= 0) {
      throw new Error('Length must be a positive number');
    }

    // verify students
    if (!Array.isArray(students) || students.some(student => typeof student !== 'string' || student.trim().length === 0)) {
      throw new Error('Students must be a non-empty array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  // getters
  get name () {
    return this._name;
  }

  get length () {
    return this._length;
  }

  get students () {
    return this._students;
  }

  // setters
  set name (newName) {
    this._name = newName;
  }

  set length (newLength) {
    this._length = newLength;
  }

  set students (newStudents) {
    this._students = newStudents;
  }
}
