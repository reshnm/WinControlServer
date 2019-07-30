const express = require('express');
const bodyParser = require("body-parser");
const util = require('util');
const exec = util.promisify(require('child_process').exec);

const app = express();
const PORT = 3000;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


async function runCmd(cmd, res) {
    try {
        const { stdout, stderr } = await exec(cmd);
        res.end(JSON.stringify({
            stdout: stdout,
            stderr: stderr
        }));
    } catch(e) {
        res.status(500)
        res.end(JSON.stringify(e));
    }
}


app.get('/', (req, res) => {
    res.end();
});

app.post('/shutdown', (req, res) => {
    const shutdownTimeout = req.body.timeout;
    const force = req.body.force

    if (shutdownTimeout != undefined && !isNaN(shutdownTimeout)) {
        var cmd = 'shutdown -s';

        if (force) {
            cmd += ' -f';
        }

        if (shutdownTimeout > 0) {
            cmd += ' -t ' + shutdownTimeout;
        }

        runCmd(cmd, res);
    } else {
        res.status(400);
        res.end(JSON.stringify({ error: 'invalid request' }));
    }
});

app.post('/restart', (req, res) => {
    runCmd('shutdown -r', res);
});

app.get('/processlist', (req, res) => {
    runCmd('tasklist', res);
});

app.post('/killprocess', (req, res) => {
    const pid = req.body.pid;

    if (pid != undefined && !isNaN(pid)) {
        runCmd('Taskkill /PID ' + pid + ' /F', res);
    } else {
        res.status(400);
        res.end(JSON.stringify({ error: 'invalid request' }));
    }
});

app.listen(PORT, () => {
    console.log(`Started on port ${PORT}`);
})