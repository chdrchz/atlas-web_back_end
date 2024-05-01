export default class ClassRoom {
    constructor(maxStudentsSize) {
        if (typeof maxStudentsSize !== number) {
            throw new error('Not a number');
        }
        this.__maxStudentsSize = maxStudentsSize;
    }
}