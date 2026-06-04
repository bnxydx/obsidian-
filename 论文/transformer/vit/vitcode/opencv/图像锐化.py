import cv2
import numpy as np


# 创建一个3×3锐化卷积核（拉普拉斯增强）
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]], dtype=np.float32)

def main():
    img = cv2.imread("inimg/sx.jpg", cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("无法读取图像文件 `mm.jpg`")

    # 计算图像的拉普拉斯边缘（保持浮点，允许负值）
    edges = cv2.filter2D(img.astype(np.float32), cv2.CV_32F, kernel)

    # 将边缘叠加回原图
    sharpened = np.clip(img.astype(np.float32) + edges, 0, 255).astype(np.uint8)

    # cv2.imwrite("out_edges.png", cv2.convertScaleAbs(edges))
    cv2.imwrite("outimg/out_sharpened8.jpg", sharpened)


if __name__ == "__main__":
    main()
