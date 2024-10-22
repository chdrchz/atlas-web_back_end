const chai = require("chai");
const sendPaymentRequestToApi = require("./4-payment.js");
const { expect } = chai;

describe("sendPaymentRequestToApi", () => {
    it("should call Utils.calculateNumber with SUM and arguments 100, 20", () => {
        result = sendPaymentRequestToApi(100, 20);
        console.log(`The total is: ${result}`);
    });
    it("should call Utils.calculateNumber with SUM and arguments 10, 10", () => {
        result = sendPaymentRequestToApi(10, 10);
        console.log(`The total is: ${result}`);
    });
});