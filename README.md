# MouseMobil™
While human transportation systems have soared in progress over the past century, mouse transportation systems have stagnated. We're making a small vehicle (think shoebox-sized) that attracts mice inside and uses a camera to allow a mouse to control the velocity of the vehicle, in the hopes of creating a more inclusive world for our small and furry friends.

## How it Works
This device uses bait and a trapdoor to trap a mouse inside a central hub, which sits on multiple wheels controlled by servos. We use a camera on the top of this hub to determine the mouse's location relative to the center of the hub, and move the car in the direction that the mouse moves towards. So if the mouse moved to the front of the car, the car would move forward. After a certain period of time, we let the mouse out.

While the funnest mode is when the vehicle is controlled by a mouse, you also have the option of controlling the vehicle with your phone. To do this, you go to a URL that you point the MouseMobil to, and control the motion with an on-screen joystick. You can also do other things from here, like open the door and run the car in autonomous mode.

Under the hood, the Raspberry Pi is running a Node/Express server which controls the car. There are several python scripts which control the camera and motors, and the server activates / communicates with these control scripts as necessary. We use ZeroRPC's remote prodedure call functionality to communicate with these scripts to move the car in the manual-control mode, and in the mouse-driven mode, we simply launch one of these scripts and simply let it run.

### Main Technical Components:
#### Hardware:
- Raspberry Pi Model 3 B+
- PiCamera (Wide Angle Lens)
- 3x Continuous Rotation Servo Motors
- Continuous Rotation Servo Motor with Feedback
- Adafruit 16-Channel Servo Driver
- 14.8V 5000mAh 50C LiPo Battery

#### Software:
- Node.js
- Express.js
- Adafruit Servo Control Library
- OpenCV
- React / Webpack
- ZeroRPC

#### Bill of Materials:
Coming Soon :)

#### Video:
Coming Soon :)

## Credits
Credit goes to Tiffany Tao, Elizabeth Vasquez, and Jordan Wick for putting in the work to bring this project to life. Thanks to the MIT ProjX Team (projx.mit.edu) for supplying all of the funding for this project.
