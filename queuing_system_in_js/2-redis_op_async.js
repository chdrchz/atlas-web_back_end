import { createClient } from "redis";

const client = createClient({
  host: "localhost",
  port: 6379,
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.connect().then(async () => {
  try {
    // Display the value associated with the key passed
    await displaySchoolValue("Holberton");

    // Try to set a key and check the status code
    const status = await setNewSchool("HolbertonSanFrancisco", "100");
    if (status === "OK") {
      console.log(`reply: ${status}`);
      // Display the new value
      await displaySchoolValue("HolbertonSanFrancisco");
    } else {
      console.error("Failed to set the value for HolbertonSanFrancisco.");
    }
  } catch (err) {
    console.error("Error in Redis operations:", err);
  }
});

async function setNewSchool(schoolName, value) {
  const status = await client.set(schoolName, value);
  return status;
}

async function displaySchoolValue(schoolName) {
  const value = await client.get(schoolName);
  console.log(value);
}
