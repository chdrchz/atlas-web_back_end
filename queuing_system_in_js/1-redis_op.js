import { createClient } from "redis";

const client = createClient({
  host: 'localhost',
  port: 6379,
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.connect().then(() => {
  // Display the value associated with the key passed
  displaySchoolValue("Holberton")
    .then(() => {
      // Try to set a key value pair
      return setNewSchool("HolbertonSanFrancisco", "100");
    })
    .then((status) => {
      if (status === "OK") {
        console.log(`reply: ${status}`);
      }
    })
    .then(() => {
      // Display the new value
      return displaySchoolValue("HolbertonSanFrancisco");
    })
    .catch((err) => {
      console.error("Error in Redis operations:", err);
    });
});

function setNewSchool(schoolName, value) {
  return client.set(schoolName, value);
};

function displaySchoolValue(schoolName) {
  return client.get(schoolName).then((value) => {
    console.log(value);
  });
};
