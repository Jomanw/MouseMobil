//Requires
const express = require('express');
const app = express();
const path = require('path');
const chalk = require('chalk');
const morgan = require('morgan');
const spawn = require("child_process").spawn;
var zerorpc = require("zerorpc");


var pythonProcess = spawn('python3', ['run.py', 'stop']);
var client = new zerorpc.Client();




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
  // pythonProcess = spawn('python3', ['run.py', 'test']);
  console.log("Function to start the car in controller mode should go here");
  rpcProcess = spawn('python3', ['test_rpc.py']);
  client.connect("tcp://0.0.0.0:1337");
  res.status = 200;
  res.end("Running car in test mode");
});

app.post('/setspeed', function (req, res, next) {
  console.log("Function to set the velocity of the cars");
  console.log(req);
  console.log(res);
  client.invoke("hello", req.x, function(error, res, more) {
    console.log("I'm here.");
    console.log(error);
    console.log(res);
  });
  res.status = 200;
  res.end("Updated speed of the car");
});


const port = 80;
//Run Server
app.listen(process.env.PORT || port, () => console.log(chalk.blue(`Listening intently on port ${port}`)));
