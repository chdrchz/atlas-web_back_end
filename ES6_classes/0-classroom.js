export default class ClassRoom {
    constructor(maxStudentsSize) {
        if (typeof maxStudentsSize !== number) {
            throw new error('Not a number');
        }
        this._maxStudentsSize = maxStudentsSize;
    }
}