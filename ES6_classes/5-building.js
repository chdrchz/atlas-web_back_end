export default class Building {
  constructor(sqft) {
    // any class extending Building must implement below method
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }

    this._sqft = sqft;
  }

  // getters
  get sqft() {
    return this._sqft;
  }
}
