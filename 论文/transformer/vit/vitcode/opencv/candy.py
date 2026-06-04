import cv2
import numpy as np


gauss_kernel = (7,7)


def sobel_gradients(img: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    kernelx = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]], dtype=np.float32)
    kernely = kernelx.T
    gx = cv2.filter2D(img, cv2.CV_32F, kernelx)
    gy = cv2.filter2D(img, cv2.CV_32F, kernely)
    magnitude = np.hypot(gx, gy)
    angle = np.rad2deg(np.arctan2(gy, gx)) % 180
    return magnitude, angle


def non_max_suppression(mag: np.ndarray, angle: np.ndarray) -> np.ndarray:
    h, w = mag.shape
    suppressed = np.zeros_like(mag, dtype=np.float32)

    angle_quantized = np.round(angle / 45) * 45 % 180

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            direction = angle_quantized[i, j]
            neighbors = []
            if direction == 0:
                neighbors = [mag[i, j - 1], mag[i, j + 1]]
            elif direction == 45:
                neighbors = [mag[i - 1, j + 1], mag[i + 1, j - 1]]
            elif direction == 90:
                neighbors = [mag[i - 1, j], mag[i + 1, j]]
            else:  # 135°
                neighbors = [mag[i - 1, j - 1], mag[i + 1, j + 1]]

            if mag[i, j] >= max(neighbors):
                suppressed[i, j] = mag[i, j]

    return suppressed


def double_threshold_hysteresis(img: np.ndarray,
                                low_ratio: float = 0.1,
                                high_ratio: float = 0.3) -> np.ndarray:
    high_thresh = img.max() * high_ratio
    low_thresh = high_thresh * low_ratio

    strong = 255
    weak = 75

    res = np.zeros_like(img, dtype=np.uint8)
    strong_i, strong_j = np.where(img >= high_thresh)
    weak_i, weak_j = np.where((img >= low_thresh) & (img < high_thresh))

    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak

    h, w = img.shape
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if res[i, j] == weak:
                if np.any(res[i - 1:i + 2, j - 1:j + 2] == strong):
                    res[i, j] = strong
                else:
                    res[i, j] = 0

    return res


def main():
    in_img = cv2.imread('inimg/sx.jpg', cv2.IMREAD_GRAYSCALE)
    if in_img is None:
        raise FileNotFoundError('找不到输入图像 inimg/sx.jpg')

    # 高斯平滑，降噪
    blurred = cv2.GaussianBlur(in_img, gauss_kernel, 0)

    # Sobel 梯度
    mag, angle = sobel_gradients(blurred)

    # 非极大值抑制
    nms = non_max_suppression(mag, angle)

    # 滞后阈值
    edges = double_threshold_hysteresis(nms)

    cv2.imwrite('outimg/canny_edges3.png', edges)


if __name__ == '__main__':
    main()