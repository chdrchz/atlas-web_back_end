function calculateNumber(type, a, b) {
    const allowedTypes = [
        "SUM",
        "SUBTRACT",
        "DIVIDE"
    ];

    // If type is not a valid type
    if (!allowedTypes.includes(type)) {
        console.log("Type is not valid. Must be either 'SUM', 'SUBTRACT', 'DIVIDE'. Re-enter Type.");
        return null;
    }

    // If type is SUM
    if (type === allowedTypes[0]) {
        return Math.round(a) + Math.round(b);
    }

    // If type is SUBTRACT
    else if (type === allowedTypes[1]) {
        return Math.round(a) - Math.round(b);
    }

    // If type is DIVIDE
    else if (type === allowedTypes[2]) {
        if (Math.round(b) !== 0) {
            return Math.round(a) / Math.round(b);
        } else {
            return ("Error");
        }
    }
}


module.exports = calculateNumber;