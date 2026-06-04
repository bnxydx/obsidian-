import cv2
import numpy as np

kernel = np.array([
    [0,1,0],
    [1,-4,1],
    [0,1,0]
],dtype=np.float32)

def main():
    img = cv2.imread('inimg/sx.jpg', cv2.IMREAD_GRAYSCALE)
    s = cv2.filter2D(img,ddepth=-1,kernel=kernel)
    cv2.imwrite("outimg/as.jpg", s)

if __name__ == '__main__':
    main()