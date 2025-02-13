import cv2 
from util import get_limits
from PIL import Image

yellow = [0, 255, 255] # yellow in BGR colorspace
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit = get_limits(color=yellow)
    mask = cv2.inRange(hsv_frame, lower_limit, upper_limit)
    mask_ = Image.fromarray(mask) # cvt image from np.array to pillow format
    bounding_box = mask_.getbbox()
    if bounding_box is not None:
        x1, y1, x2, y2 = bounding_box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3) 
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) % 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
