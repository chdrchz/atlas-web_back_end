export default class Airport {
  // constructor method
  constructor(name, code) {
    // verify name
    if (typeof name !== 'string' || name.length <= 0) {
      throw new Error('Name must be a non-empty string');
    }

    // verify code
    if (typeof code !== 'string' || code.length <= 0) {
      throw new Error('Code must be a non-empty string');
    }

    this._name = name;
    this._code = code;
  }

  // getters
  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  // setters
  set name(newName) {
    if (typeof newName !== 'string' || newName.length <= 0) {
      throw new Error('Name must be a non-empty string');
    }
    this._name = newName;
  }

  set code(newCode) {
    if (typeof newCode !== 'string' || newCode.length <= 0) {
      throw new Error('Code must be a non-empty string');
    }
    this._code = newCode;
  }

  // string representation
  printSymbol() {
    return `${this._code}`;
  }
}
