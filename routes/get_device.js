const db = require('../db')

function routes(fastify){
    fastify.get('/', async (request, reply) => {


        let db = this.database()
        db.serialize(() => {
            db.prepare(
                `CREATE TABLE IF NOT EXISTS "server" ("server_type" TEXT NOT NULL,"name"TEXT NOT NULL,"id"INTEGER NOT NULL,PRIMARY KEY("id" AUTOINCREMENT));`
            ).run().finalize();

            db.all(`SELECT * FROM server ORDER BY server_type ASC`, (err, rows) => {

                for (let element of rows){
                    console.log(element)
                }

            });

            db.close();
        });

        return {
            devices: [
                "test",
                "test2",
                "test3"
            ]
        }
    })
}

module.exports = { routes }