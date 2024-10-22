const Utils = {
  calculateNumber: function (type, a, b) {
    const allowedTypes = ["SUM", "SUBTRACT", "DIVIDE"];

    // If type is not a valid type
    if (!allowedTypes.includes(type)) {
      console.log(
        "Type is not valid. Must be either 'SUM', 'SUBTRACT', or 'DIVIDE'. Re-enter Type."
      );
      return null;
    }

    // If type is SUM
    if (type === "SUM") {
      return Math.round(a) + Math.round(b);
    }

    // If type is SUBTRACT
    if (type === "SUBTRACT") {
      return Math.round(a) - Math.round(b);
    }

    // If type is DIVIDE
    if (type === "DIVIDE") {
      if (Math.round(b) !== 0) {
        return Math.round(a) / Math.round(b);
      } else {
        return "Error";
      }
    }
  },
};

// Export the Utils module
module.exports = Utils;
