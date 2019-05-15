"""
Class for accessing the Hub Camera of the MouseMobil. Functionality include:
- Initializing and Accessing the Camera Stream
- Getting Mouse X and Y Positions
"""

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (480, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(480, 480))

# allow the camera to warmup
time.sleep(0.1)

# Initialize some constants
MOUSE_SIZE_THRESHOLD = 10


class HubCamera():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.mouse_present = False
        self.door_open = True
        self.camera_stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)

    def mouse_present(self):
        """
        Tells if a mouse is in the hub or not

        Returns a boolean: True if mouse is present, false otherwise
        """
        return self.mouse_present

    def get_mouse_location(self):
        """
        Gives the (x, y) location of the mouse inside the hub

        Returns: 2-tuple of the location inside the mouse, where the
        (x, y) values range from 0 to 1
        """
        image = next(self.camera_stream).array

        cv2.imshow("Frame", image)

        # TODO: Write code that gets the center of the mouse from the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY_INV)

        image, contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # Find object with the biggest bounding box
        mx = (0,0,0,0)      # biggest bounding box so far
        mx_area = 0
        for cont in contours:
            x,y,w,h = cv2.boundingRect(cont)
            area = w*h
            if area > mx_area:
                mx = x,y,w,h
                mx_area = area
        x,y,w,h = mx

        if mx_area > MOUSE_SIZE_THRESHOLD:
            self.mouse_present = True
        else:
            self.mouse_present = False

        self.x = x + (w / 2)
        self.y = y + (h / 2)

        # If we want to also print out the image with the contours and the crop, for debugging:
        if False:
            # Output to files, just to see the output
            roi=img[y:y+h,x:x+w]
            cv2.imwrite('Image_crop.jpg', roi)

            cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)
            cv2.imwrite('Image_cont.jpg', img)

        # Need to clear the buffer for the video capture, otherwise it'll throw an error
        rawCapture.truncate(0)

        return self.x, self.y
