



from vehicle import Vehicle
from hub_camera import HubCamera

# Ports on the servo module that the servos are attached to
motion_servos = [0, 1, 2]

# Port on the servo module that the trapdoor servo is attached to
trapdoor_servo = 3

# Car that will be controlled
car = Vehicle(motion_servos=motion_servos, trapdoor_servo=trapdoor_servo)

# Camera module that will be used to determine mouse location
hub = HubCamera()

if __name__ == "__main__":
    print("Got here")
    print(hub.get_mouse_location())
