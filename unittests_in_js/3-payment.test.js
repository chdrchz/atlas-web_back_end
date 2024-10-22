const chai = require("chai");
const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment.js");
const { expect } = chai;

describe("sendPaymentRequestToApi", () => {
  let spy;

  beforeEach(() => {
    // Create a spy for calculateNumber
    spy = sinon.spy(Utils, "calculateNumber");
  });

  afterEach(() => {
    // Restore the original function after each test
    spy.restore();
  });

  it("should call Utils.calculateNumber with SUM and arguments 100, 20", () => {
    sendPaymentRequestToApi(100, 20);

    // Check that Utils.calculateNumber was called once
    expect(spy.calledOnce).to.be.true;

    // Check that Utils.calculateNumber was called with 'SUM', 100, 20
    expect(spy.calledWith("SUM", 100, 20)).to.be.true;
  });
});
