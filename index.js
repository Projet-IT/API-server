// Require libs
const fastify = require('fastify')({ logger: true })
const fs = require('fs')

// setup routes
for (let routes of fs.readdirSync('./routes/')){
    let router_file = require('./routes/' + routes)
    router_file.routes(fastify)
}

// Run
const start = async () => {
    try {
        await fastify.listen(3000)
    } catch (err) {
        fastify.log.error(err)
        process.exit(1)
    }
}
start()