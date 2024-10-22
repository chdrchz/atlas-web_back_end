const chai = require("chai");
const sinon = require("sinon");
const Utils = require('./utils');
const sendPaymentRequestToApi = require("./5-payment.js");
const { expect } = chai;

describe("sendPaymentRequestToApi", () => {
    let spy;

    beforeEach(() => {
        // Create a spy
        spy = sinon.spy(Utils, "calculateNumber")
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