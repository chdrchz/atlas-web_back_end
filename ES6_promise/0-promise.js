function getResponseFromAPI() {
    const p = new Promise((resolve, reject) => {
        let num = 1 + 1
        if (num == 2) {
            resolve('Success')
        } else {
            reject('Failure')
        }
    });
}