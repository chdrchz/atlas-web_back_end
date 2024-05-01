getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        const success = true;
        if (success) {
            resolve({ data: "Sample response data" });
        } else {
            reject("Error: Failed to get response from API");
        }
    });
}