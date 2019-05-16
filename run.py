# from vehicle import Vehicle
# from hub_camera import HubCamera
import sys
import zerorpc
# sys.exit()

# Threshold for movement for the mouse
movement_threshold = .1

# Ports on the servo module that the servos are attached to
motion_servos = [0, 1, 2]

# Port on the servo module that the trapdoor servo is attached to
trapdoor_servo = 3

# Car that will be controlled
# car = Vehicle(motion_servos=motion_servos, trapdoor_servo=trapdoor_servo)

# Camera module that will be used to determine mouse location
# hub = HubCamera()

if __name__ == "__main__":

    # If a stop signal is sent, this script will stop the car and exit.
    if len(sys.argv) > 1 and sys.argv[1] == 'stop':
        # car.stop_car()
        print("Stopped car.")
        sys.exit()

    # If an open signal is sent, this script will open the door.
    if len(sys.argv) > 1 and sys.argv[1] == 'open':
        # car.open_door()
        sys.exit()

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        # car.open_door()

        class HelloRPC(object):
            def hello(self, x):

                return "Hello, %s" %(str(x),)

        s = zerorpc.Server(HelloRPC())
        s.bind("tcp://mousemobil.ddns.net:4242")
        s.run()



    if len(sys.argv) > 1 and sys.argv[1] == 'autonomous':
        # car.open_door()
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
