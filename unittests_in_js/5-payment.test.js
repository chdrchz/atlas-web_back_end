const chai = require("chai");
const sinon = require("sinon");
const sendPaymentRequestToApi = require("./4-payment.js");
const { expect } = chai;

describe("sendPaymentRequestToApi", () => {
    beforeEach(() => {
        // Create a stub for calculateNumber and force it to return 10
        spy = sinon.spy(Utils, "calculateNumber").returns(10);
      });
    
      afterEach(() => {
        // Restore the original function after each test
        spy.restore();
      });

    it("should call Utils.calculateNumber with SUM and arguments 100, 20", () => {
        result = sendPaymentRequestToApi(100, 20);
        console.log(`The total is: ${result}`);
    });
    it("should call Utils.calculateNumber with SUM and arguments 10, 10", () => {
        result = sendPaymentRequestToApi(10, 10);
        console.log(`The total is: ${result}`);
    });
});