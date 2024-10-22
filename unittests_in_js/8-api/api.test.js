const chai = require("chai");
const supertest = require("supertest");
const { app, server } = require("./api.js"); // Import the server
const { expect } = chai;

const request = supertest(app);

describe("GET /", () => {
  after(() => {
    server.close(); // Close the server after all tests
  });

  it("should return 'Welcome to the payment system' with status code 200", (done) => {
    request.get("/")
      .then((res) => {
        expect(res.status).to.equal(200);
        expect(res.text).to.equal("Welcome to the payment system");
        done();
      })
      .catch((err) => done(err));
  });
});
