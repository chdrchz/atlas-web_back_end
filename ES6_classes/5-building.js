export default class Building {
  // constructor method
  constructor(sqft) {
    // verify class
    if (new.target === Building) {
      throw new Error('Abstract classes cannot be instantiated directly');
    }

    // verify sqft
    if (typeof sqft !== 'number' || sqft < 0) {
      throw new Error('Sqft must be a positive or zero number');
    }
    this._sqft = sqft;
  }

  // getters
  get sqft() {
    return this._sqft;
  }

  // abstract method
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
