const axios = require('axios');
const { expect, assert } = require('chai');

const url = 'http://localhost:7865/'

describe('API index page integration test', () => {
    it('should return a successful status code and the landing message', () => {
        axios.get(url).then((res) => {
            assert.equal(res.status, 200);
            assert.equal(res.data, 'Welcome to the payment system');
        });
    });
});
