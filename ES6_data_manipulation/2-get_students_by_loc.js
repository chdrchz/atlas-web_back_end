export default function getStudentsByLocation(students, city) {
  if (Object.getPrototypeOf(students) === Array.prototype) {
    return students.filter((items) => items.location === city);
  }
  return [];
}
