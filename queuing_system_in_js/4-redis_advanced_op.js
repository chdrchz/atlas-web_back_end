import { createClient } from "redis";

const client = createClient({
  host: "localhost",
  port: 6379,
});

client
  .connect()
  .then(() => {
    console.log("Redis client connected to the server");

    // Chain hSet operations
    return client
      .hSet("HolbertonSchools", "Portland", 50)
      .then((status) => {
        console.log(`Reply for Portland: ${status}`);
        return client.hSet("HolbertonSchools", "Seattle", 80);
      })
      .then((status) => {
        console.log(`Reply for Seattle: ${status}`);
        return client.hSet("HolbertonSchools", "New York", 20);
      })
      .then((status) => {
        console.log(`Reply for New York: ${status}`);
        return client.hSet("HolbertonSchools", "Bogota", 20);
      })
      .then((status) => {
        console.log(`Reply for Bogota: ${status}`);
        return client.hSet("HolbertonSchools", "Cali", 40);
      })
      .then((status) => {
        console.log(`Reply for Cali: ${status}`);
        return client.hSet("HolbertonSchools", "Paris", 2);
      })
      .then((status) => {
        console.log(`Reply for Paris: ${status}`);

        // get all values from the hash
        return client.hGetAll("HolbertonSchools");
      })
      .then((result) => {
        console.log("Hash Values:", result); // Log the entire hash
      })
      .catch((err) => {
        console.error("Error in Redis operations:", err);
      })
      .finally(() => {
        client.quit(); // Ensure the Redis connection is closed
      });
  })
  .catch((err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });
