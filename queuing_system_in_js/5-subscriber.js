import { createClient } from "redis";

const client = createClient({
  host: "localhost",
  port: 6379,
});

client.connect().then(() => {
  console.log("Redis client connected to the server");

  // Set up the subscription handler here
  client
    .subscribe("holberton school channel", (err) => {
      if (err) {
        console.error("Failed to subscribe to channel:", err);
      }
    })
    .then(() => {
      // Set up a message handler
      client.on("message", (channel, message) => {
        console.log(`Received message from ${channel}: ${message}`);

        if (message === "KILL_SERVER") {
          client.unsubscribe(channel);
          client.quit();
        }
      });
    });
});
