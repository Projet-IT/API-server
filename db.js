const sqlite = require('sqlite3')

function database () {
    return new sqlite.Database('./data.db', (err) => {
        if (err) {
            console.error(err.message);
        }
    })
}

module.exports = { database }