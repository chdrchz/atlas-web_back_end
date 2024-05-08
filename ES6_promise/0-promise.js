export default function getResponseFromAPI() {
  const promise = new Promise((resolve) => {
    resolve('Resolved!');
  });
  return promise;
}
