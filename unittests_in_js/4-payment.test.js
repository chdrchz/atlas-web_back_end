const chai = require("chai");
const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment.js");
const { expect } = chai;

describe("sendPaymentRequestToApi", () => {
  let stub;

  beforeEach(() => {
    // Create a stub for calculateNumber and force it to return 10
    stub = sinon.stub(Utils, "calculateNumber").returns(10);
  });

  afterEach(() => {
    // Restore the original function after each test
    stub.restore();
  });

  it("should call Utils.calculateNumber with SUM and arguments 100, 20", () => {
    sendPaymentRequestToApi(100, 20);

    // Check that Utils.calculateNumber was called once
    expect(stub.calledOnce).to.be.true;

    // Check that Utils.calculateNumber was called with 'SUM', 100, 20
    expect(stub.calledWith("SUM", 100, 20)).to.be.true;
  });
});