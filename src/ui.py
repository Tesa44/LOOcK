import cv2
from config import font, fontScale, thickness, lineType
def show_controls(frame, fontColor):
    cv2.putText(frame, "[a] to add reference",
                (10, 350),
                font,
                fontScale,
                fontColor,
                thickness + 1,
                lineType)

    cv2.putText(frame, "[u] to unlock lock",
                (10, 400),
                font,
                fontScale,
                fontColor,
                thickness + 1,
                lineType)

    cv2.putText(frame, "[q] to quit",
                (10, 450),
                font,
                fontScale,
                fontColor,
                thickness + 1,
                lineType)

def showText(frame, text, x1, y2, fontColor):
    cv2.putText(frame, str(text),
                (x1, y2),
                font,
                fontScale,
                fontColor,
                thickness + 1,
                lineType)