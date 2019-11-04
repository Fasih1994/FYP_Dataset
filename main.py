import cv2
import os

size = 260
height, width = 650, 480

example_img_path = '/home/fashi/Figure_1.png'
example_img = cv2.imread(example_img_path)
example_img = cv2.resize(src=example_img, dsize=(height, width), interpolation=cv2.INTER_NEAREST)

base_path = 'data'
name = 'test'
base_path = os.path.join(base_path, name)
if not os.path.exists(base_path):
    os.mkdir(base_path)

start_point = (100, 100)
end_point = (start_point[0] + size, start_point[1] + size)
print(start_point, end_point)
capture = cv2.VideoCapture(0)
while capture.isOpened():

    ret, frame = capture.read()
    if ret is True:
        cv2.imshow('Reference Image', example_img)
        cv2.rectangle(frame, start_point, end_point, (255, 255, 64), thickness=3)
        cv2.imshow('Video Frame', frame)
        key = cv2.waitKey(1)
        if key != -1:
            key = chr(key)
            print(key)
            if key != 'j':
                img_path = os.path.join(base_path, key)
                if not os.path.exists(img_path):
                    os.makedirs(img_path)
                image = frame[start_point[1] + 3:end_point[1], start_point[0] + 3:end_point[0]]
                filename = '{}/{}.png'.format(img_path, len(os.listdir(img_path)))
                cv2.imwrite(filename=filename, img=image)
                print('image saved at ', filename)
            else:
                break

    else:
        break

capture.release()
cv2.destroyAllWindows()
