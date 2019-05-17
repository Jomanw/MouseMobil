//Requires
const express = require('express');
const app = express();
const path = require('path');
const chalk = require('chalk');
const morgan = require('morgan');
const spawn = require("child_process").spawn;
var zerorpc = require("zerorpc");
const config = require("./config.json");
app.use(express.urlencoded());
app.use(express.json());



var pythonProcess = spawn('python3', ['test_rpc.py', 'stop']);

// var rpcProcess = spawn('python3', ['test_rpc.py']);
pythonProcess.stderr.on('data', function(data) {
  console.log(data.toString());
});
var client = new zerorpc.Client();
// setTimeout(function () {
//   client.connect('tcp://' + '127.0.0.1' + ':1337');
// }, 5000);
// client.invoke("hello", "RPC", function(error, res, more) {
//   console.log("I'm here.");
//   console.log(error);
//   console.log(res);
// });




//Static Routes
app.use('/dist', express.static(path.join(__dirname, 'dist')));
app.use(morgan('dev')) // logging
//Main App Route
app.get('/', (req, res, next) => res.sendFile(path.join(__dirname, 'index.html')));



// Endpoints for the ControlButtons to hit, to control the physical vehicle
app.post('/stopcar', function (req, res, next) {
  pythonProcess.kill('SIGKILL');
  pythonProcess = spawn('python3', ['run.py', 'stop']);
  console.log("Function to stop the car should go here");
  res.status = 200;
  res.end("Stopped Car");
});

app.post('/opendoor', function (req, res, next) {
  pythonProcess.kill('SIGKILL');
  pythonProcess = spawn('python3', ['run.py', 'open']);
  console.log("Function to open the door should go here");
  res.status = 200;
  res.end("Stopped Car");
});

app.post('/runautonomous', function (req, res, next) {
  pythonProcess.kill('SIGKILL');
  pythonProcess = spawn('python3', ['run.py', 'autonomous']);
  console.log("Function to start the car in autonomous mode should go here");
  res.status = 200;
  res.end(" Ran car in autonomous mode");
});

app.post('/runtest', function (req, res, next) {
  pythonProcess.kill('SIGKILL');
  pythonProcess = spawn('python3', ['run.py', 'test']);
  console.log("Function to start the car in controller mode should go here");
  // rpcProcess = spawn('python3', ['run.py', 'test']);
  pythonProcess.stdout.on('data', function(data) {
    console.log(data.toString());
  });
  // client.connect('tcp://' + config.url + ':1337');
  client.connect('tcp://127.0.0.1:1337');
  res.status = 200;
  res.end("Running car in test mode");
});

app.post('/setspeed', function (req, res) {
  console.log("Function to set the velocity of the cars");
  client.invoke("hello", [req.body.x, req.body.y], function(error, res, more) {
    console.log(res);
  });
  res.status = 200;
  res.end("Updated speed of the car");
});


const port = 80;
//Run Server
app.listen(process.env.PORT || port, () => console.log(chalk.blue(`Listening intently on port ${port}`)));
