const assert = require('assert');
const calculateNumber = require('./1-calcul.js')

describe('calculateNumber()', () => {
  it('should return the sum of rounded a and rounded b', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
  });

  it('should return the dividend of rounded a divided by rounded b', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 4, 1.7), 2);
    assert.strictEqual(calculateNumber('DIVIDE', 2.2, 1), 1);
    assert.strictEqual(calculateNumber('DIVIDE', 10.1, 10.1), 1);
    assert.strictEqual(calculateNumber('DIVIDE', 100, 0), 'Error');
  });

  it('should return the difference between rounded a minus rounded b', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 6, 2.8), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', 5, 2), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', 11, 5.4), 6);
  });
});