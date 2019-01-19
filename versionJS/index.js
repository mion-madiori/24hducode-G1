let five = require('johnny-five');
let mqtt = require('mqtt');

let client = mqtt.connect({
    host: 'mpd.lan',
    port: 1883
})

client.on('connect', () => {
    console.log('connected');

    client.publish(`laumio/status/advertise`)

    client.subscribe(`laumio/all/discover`);
    client.publish(`/laumio/all/animate_rainbow`);

})

client.on('message', (msg) => {
    console.log(`message: ${msg}`);
    
})