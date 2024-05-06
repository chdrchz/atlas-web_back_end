export default class Car {
  // constructor method
  constructor(brand, motor, color) {
    // verify brand
    if (typeof brand !== 'string' || brand.length <= 0) {
      throw new Error('Brand must be a non empty string');
    }

    // verify motor
    if (typeof motor !== 'string' || motor.length <= 0) {
      throw new Error('Motor must be a non empty string');
    }

    // verify color
    if (typeof color !== 'string' || color.length <= 0) {
      throw new Error('Color must be a non empty string');
    }

    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // getters
  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  // setters
  set brand(newBrand) {
    if (typeof newBrand !== 'string' || newBrand.length <= 0) {
      throw new Error('Brand must be a non empty string');
    }
    this._brand = newBrand;
  }

  set motor(newMotor) {
    if (typeof newMotor !== 'string' || newMotor.length <= 0) {
      throw new Error('Motor must be a non empty string');
    }
    this._motor = newMotor;
  }

  set color(newColor) {
    if (typeof newColor !== 'string' || newColor.length <= 0) {
      throw new Error('Color must be a non empty string');
    }
    this._color = newColor;
  }

  cloneCar() {
    return new this.constructor;
  }
}
