export default function concatArrays(array1, array2, string) {
  const combinedArray = [...array1, ...array2, ...string];
  return combinedArray;
}
