const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber()', () => {
  it('should return the sum of rounded a and rounded b', () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
  });

  it('should return the dividend of rounded a divided by rounded b', () => {
    expect(calculateNumber('DIVIDE', 4, 1.7)).to.equal(2);
    expect(calculateNumber('DIVIDE', 2.2, 1)).to.equal(2);
    expect(calculateNumber('DIVIDE', 10.1, 10.1)).to.equal(1);
    expect(calculateNumber('DIVIDE', 100, 0)).to.equal('Error');
  });

  it('should return the difference between rounded a minus rounded b', () => {
    expect(calculateNumber('SUBTRACT', 6, 2.8)).to.equal(3);
    expect(calculateNumber('SUBTRACT', 5, 2)).to.equal(3);
    expect(calculateNumber('SUBTRACT', 11, 5.4)).to.equal(6);
  });
});