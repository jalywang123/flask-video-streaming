import cv2
from base_camera import BaseCamera
import cube_finder
import time

class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            #time.sleep(0.05)
 
            _, raw_cap = camera.read()

            returned = cube_finder.process_image(raw_cap)
            img = getattr(returned,'frame')
	    #img = raw_cap
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
