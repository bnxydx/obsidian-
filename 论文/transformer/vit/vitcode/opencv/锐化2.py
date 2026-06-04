import cv2
import numpy as np


# 创建一个3×3锐化卷积核（拉普拉斯增强）
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]], dtype=np.float32)

def main():
    img = cv2.imread("inimg/mm.jpg", cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("无法读取图像文件 `opencv/out_gray.jpg")

    # sharpened = sharpen_image(img, kernel)
    sharpened = cv2.filter2D(img,ddepth=-1,kernel=kernel)
    cv2.imwrite("outimg/out_sharpened8.jpg", sharpened)


if __name__ == "__main__":
    main()
