import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    if (typeof floors !== 'number' || floors <= 0) {
      throw new Error('Floors must be a positive, non-zero number');
    }

    super(sqft);
    this._floors = floors;
  }

  // getters
  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  // evacuation message method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
