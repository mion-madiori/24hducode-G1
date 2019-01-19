let five = require('johnny-five');
let mqtt = require('mqtt');

let client = mqtt.connect({
    host: 'mpd.lan',
    port: 1883
})

client.on('connect', () => {
    console.log('connected');

    client.subscribe(`laumio/status/advertise`)

    setInterval(() => {
        client.publish(`laumio/all/animate_rainbow`)
    }, 2000);
    client.publish(`laumio/all/animate_rainbow`);

    client.publish(`laumio/all/discover`);

})

client.on('message', (topic, msg) => {
    console.log(`${msg.toString()}`);
})