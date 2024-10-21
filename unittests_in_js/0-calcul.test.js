const assert = require('assert');
const calculateNumber = require('./0-calcul.js')

// Test Suite
describe('calculateNumber', function() {
    it ('should return 4 when args are 1 and 3', function() {
        assert.Equal(calculateNumber(1, 3), 4);
    });

    it ('should return 5 when args are 1 and 3.7', function() {
        assert.Equal(calculateNumber(1, 3.7), 5);
    });

    it ('should return 5 when args are 1.2 and 3.7', function() {
        assert.Equal(calculateNumber(1.2, 3.7), 5);
    });

    it ('should return 6 when args are 1.5 and 3.7', function() {
        assert.Equal(calculateNumber(1.5, 3.7), 6);
    });
})