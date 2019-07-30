const Service = require('node-windows').Service;

const controlServerService = new Service({
    name:'Remote Control Server',
    description: 'HTTP Server for executing commands.',
    script: 'index.js'
});

controlServerService.on('install', () => {
    controlServerService.start();
});

controlServerService.install();
