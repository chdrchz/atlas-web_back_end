export default function getStudentIdsSum(students) {
    // check arg is an array before using reduce
    if (Object.getPrototypeOf(students) === Array.prototype) {
        // filter students by id
      const ids = students.map((items) => items.id);
      const reducer = (sum, currentValue) => sum + currentValue;
      return ids.reduce(reducer, 0);
    }
    return [];
  }