const sqlite = require('../db')

function routes(fastify){
    fastify.get('/', async (request, reply) => {

        let db = sqlite.database()

        db.serialize(() => {
            db.prepare(
                `create table if not exists devices
                (
                    id integer
                        constraint devices_pk
                            primary key autoincrement
                );`
            ).run().finalize();

            db.all(`SELECT id FROM devices`, (err, rows) => {

                reply.send(rows)

                for (let element of rows){
                    console.log(element)
                }

            });

            db.close();
        });
    })
}

module.exports = { routes }