const service = require('node-windows').Service;

const controlServerService = new Service({
    name:'Control Server',
    description: 'HTTP Server for executing commands.',
    script: 'index.js'
});

controlServerService.on('install', () => {
    controlServerService.start();
});

controlServerService.install();
