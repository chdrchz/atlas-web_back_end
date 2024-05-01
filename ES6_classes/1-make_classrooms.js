export default class ClassRoom {
    //initialize class
    constructor(maxStudentsSize) {
      this._maxStudentsSize = maxStudentsSize;
    }

    //initialize new rooms with a specific size 
    initializeRooms() {
        const rooms = [
            new ClassRoom(19),
            new ClassRoom(20),
            new ClassRoom(34),
        ];
    }
  }