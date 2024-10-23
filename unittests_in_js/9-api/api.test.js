const request = require("request");
const assert = require("assert");

const url = "http://localhost:7865";

describe("Index Page", () => {
  it("should return status code 200", (done) => {
    request(url, (error, response, body) => {
      assert.strictEqual(response.statusCode, 200);
      done();
    });
  });

  it("should return the correct message", (done) => {
    request(url, (error, response, body) => {
      assert.strictEqual(body, "Welcome to the payment system");
      done();
    });
  });
});

describe("Cart Page", () => {
  it("should return status code 200 when id is a number", (done) => {
    request(url, (error, response, body) => {
      assert.strictEqual(response.statusCode, 200);
      done();
    });
  });

  it("should return status code 404 when id is not a number", (done) => {
    request(url, (error, response, body) => {
      assert.strictEqual(response.statusCode, 404);
      done();
    });
  });
});
