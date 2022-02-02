const db = require('../db')

function routes(fastify){
    fastify.get('/devices', async (request, reply) => {
        return {
            config: {
                range: 5,
                name: "test name",
                status: true
            }
        }
    })
}

module.exports = { routes }