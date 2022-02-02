function database () {
    return new sqlite.Database('./data.db', (err) => {
        if (err) {
            console.error(err.message);
        }
    })
}