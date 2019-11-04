import cv2
from imutils import paths

imagePaths = list(paths.list_images("data/Ahmed"))
for path in imagePaths:
    image = cv2.imread(path)
    fliped = cv2.flip(image, 1)
    cv2.imwrite(path, fliped)
    print("Flipped :", path)