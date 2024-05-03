import Currency from './3-currency';

export default class Pricing {
  // constructor method
  constructor(amount, currency) {
    if (typeof amount !== 'number' || amount < 0) {
      throw new Error('Amount must be a positive or zero number');
    }
    if (!(currency instanceof Currency)) {
      throw new Error('Currency must be an instance of class Currency');
    }
    this._amount = amount;
    this._currency = currency;
  }

  // getters
  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  // setters
  set amount(newAmount) {
    if (typeof newAmount !== 'number' || newAmount < 0) {
      throw new Error('Amount must be a positive or zero number');
    }
    this._amount = newAmount;
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) {
      throw new Error('Currency is not an instance of class Currency');
    }
    this._currency = newCurrency;
  }

  // displays formatted price and currency
  displayFullPrice() {
    return (`${this.amount} ${this.currency.name} (${this.currency.code})`);
  }

  // multiplies amount and conversion rate
  static convertPrice(conversionRate, amount) {
    if (typeof conversionRate !== 'number' || conversionRate <= 0) {
      throw new Error('Conversion rate must be a positive number');
    }
    return conversionRate * amount;
  }
}
