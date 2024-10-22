const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, TotalShipping) {

    // Call calculateNum from Utils
    sum = Utils.calculateNumber('SUM', totalAmount, TotalShipping)
    console.log(`The total is: ${sum}`);
}

module.exports = sendPaymentRequestToApi;