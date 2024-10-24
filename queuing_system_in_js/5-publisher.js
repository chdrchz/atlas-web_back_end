import { createClient } from "redis";

const client = createClient({
  host: "localhost",
  port: 6379,
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.connect().then(() => {
    console.log("Redis client connected to the server");
  
    const messages = [
      { message: "Holberton Student #1 starts course", time: 100 },
      { message: "Holberton Student #2 starts course", time: 200 },
      { message: "KILL_SERVER", time: 300 },
      { message: "Holberton Student #3 starts course", time: 400 },
    ];
  
    messages.forEach(({ message, time }) => {
      publishMessage(message, time);
    });
  }).catch(err => {
    console.error("Error connecting to Redis:", err);
  });

function publishMessage(message) {
  setTimeout(() => {
    console.log(`About to send: ${message}`);
    client.publish("holberton school channel", message);
  });
}
