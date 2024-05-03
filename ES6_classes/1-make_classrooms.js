import ClassRoom from "./0-classroom";

 export function initializeRooms() {
    const sizes = [19, 20, 34];
    const classSizes = [];
    for (const size of sizes) {
        classSizes.push(new ClassRoom.size);
    }
    return classSizes;
}
