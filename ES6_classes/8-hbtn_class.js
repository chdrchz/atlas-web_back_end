export default class HolbertonClass {
  // constructor
  constructor(size, location) {
    // verify size
    if (typeof size !== 'number' || size <= 0) {
      throw new Error('Size must be a positive, non-zero number');
    }

    // verify location
    if (typeof location !== 'string' || location.length <= 0) {
      throw new Error('Location must be a non-empty string');
    }

    this._size = size;
    this._location = location;
  }

  // getters
  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  // setters
  set size(newSize) {
    if (typeof newSize !== 'number' || newSize <= 0) {
      throw new Error('Size must be a non-zero number');
    }
    this._size = newSize;
  }

  set location (newLocation) {
    if (typeof newLocation !== 'string' || newLocation.length <= 0) {
      throw new Error('Location must be a non empty string');
    }
    this._location = newLocation;
  }

  // string representation
  [Symbol.toPrimitive](type) {
    if (type === 'string') {
      return this._location;
    }
    if (type === 'number') {
      return this._size;
    }
    if (type === 'undefined') {
      throw new Error('Type must be a valid number or string');
    }
    return null;
  }
}
