import cv2

DB_PATH = "../face_database.pkl"
IMAGE_DIR = "../face_images/"
SIMILARITY_THRESHOLD = 0.7
SHELLY_URL = '192.168.33.1'

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,30)
fontScale              = 1
fontColor              = (0,0,255)
thickness              = 1
lineType               = 2