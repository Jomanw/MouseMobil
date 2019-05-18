import sys
import zerorpc
import json

with open('./config.json') as f:
  config = json.load(f)

print(config)

# Threshold for movement for the mouse
movement_threshold = .1

# Ports on the servo module that the servos are attached to
motion_servos = [0, 1, 2]

# Port on the servo module that the trapdoor servo is attached to
trapdoor_servo = 3




if __name__ == "__main__":

    if config['enable_hardware']:
        from vehicle import Vehicle
        # from hub_camera import HubCamera
        # Car that will be controlled
        car = Vehicle(motion_servos=motion_servos, trapdoor_servo=trapdoor_servo)

        # Camera module that will be used to determine mouse location
        # hub = HubCamera()

    # If a stop signal is sent, this script will stop the car and exit.
    if len(sys.argv) > 1 and sys.argv[1] == 'stop':
        if config['enable_hardware']:
            car.stop_car()
        print("Stopped car.")
        sys.exit()

    # If an open signal is sent, this script will open the door.
    if len(sys.argv) > 1 and sys.argv[1] == 'open':
        if config['enable_hardware']:
            car.open_door()
        print("Opened door.")
        sys.exit()

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        if config['enable_hardware']:
            car.open_door()
        print("Starting Test Loop.")

        class HelloRPC(object):
            def hello(self, velocity):
                x = velocity[0]
                y = velocity[1]
                if x == 0 and y == 0:
                    car.stop_car()
                else:
                    car.set_speed_expo(x, y)
                # print("X: %.3f, Y: %.3f" %(x, y))
                return "X: %.3f, Y: %.3f" %(x, y)

        s = zerorpc.Server(HelloRPC())
        s.bind("tcp://0.0.0.0:1337")
        s.run()



    if len(sys.argv) > 1 and sys.argv[1] == 'autonomous':
        if config['enable_hardware']:
            car.open_door()
            while True:
                x, y = hub.get_mouse_location()

                # Wait until mouse is present
                if not hub.mouse_present():
                    continue

                # Ok, here we know a mouse is present:
                if car.door_open():
                    car.close_door()

                if abs(x) < movement_threshold and abs() < movement_threshold:
                    car.stop_car()
                else:
                    car.set_speed(x, y)
