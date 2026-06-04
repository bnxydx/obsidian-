import cv2
import numpy as np


def gray_trans(in_img='input.jpg', out_img='out_gray.jpg'):
    image = cv2.imread(in_img)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(out_img, gray_image)


def add_gaussian_noise(image, mean=0, sigma=25):
    """添加高斯噪声"""
    noise = np.random.normal(mean, sigma, image.shape)
    noisy = image + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)


def add_salt_pepper_noise(image, salt_ratio=0.02, pepper_ratio=0.02):
    """添加椒盐噪声"""
    noisy = image.copy()
    h, w = image.shape[:2]

    # 盐噪声（白色）
    num_salt = int(salt_ratio * h * w)
    coords = [np.random.randint(0, i, num_salt) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = 255

    # 椒噪声（黑色）
    num_pepper = int(pepper_ratio * h * w)
    coords = [np.random.randint(0, i, num_pepper) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = 0

    return noisy


def denoise_pipeline(in_path='input.jpg',
                     out_gaussian='noisy_gaussian.jpg',
                     out_salt_pepper='noisy_salt_pepper.jpg',
                     out_gauss_denoised='denoised_gaussian.jpg',
                     out_median_denoised='denoised_median.jpg',
                     gauss_sigma=25,
                     sp_ratio=0.02,
                     gauss_kernel=(5, 5),
                     median_kernel=5):
    """
    完整去噪流水线
    """
    # 1. 读取原图（灰度）
    img = cv2.imread(in_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"错误：无法读取图片 {in_path}")
        return

    # 2. 添加高斯噪声
    noisy_gauss = add_gaussian_noise(img, mean=0, sigma=gauss_sigma)

    # 3. 添加椒盐噪声
    noisy_sp = add_salt_pepper_noise(img, salt_ratio=sp_ratio, pepper_ratio=sp_ratio)

    # 4. 高斯滤波去高斯噪声
    denoised_gauss = cv2.GaussianBlur(noisy_gauss, gauss_kernel, 0)

    # 4. 高斯滤波去椒盐噪声
    gaosiqujiaoyan = cv2.GaussianBlur(noisy_sp, gauss_kernel, 0)

    # 5. 中值滤波去椒盐噪声
    denoised_median = cv2.medianBlur(noisy_sp, median_kernel)

    # 5. 中值滤波去高斯噪声
    zhongzhiqugaosi = cv2.medianBlur(noisy_gauss, median_kernel)

    # 6. 保存四张图
    cv2.imwrite(out_gaussian, noisy_gauss)
    cv2.imwrite(out_salt_pepper, noisy_sp)
    cv2.imwrite(out_gauss_denoised, denoised_gauss)
    cv2.imwrite(out_median_denoised, denoised_median)
    cv2.imwrite('gaosiqujiaoyan.jpg',gaosiqujiaoyan)
    cv2.imwrite('zhongzhiqugaosi.jpg',gaosiqujiaoyan)
# ==================== 直接运行 ====================
if __name__ == '__main__':
    denoise_pipeline(
        in_path='input.jpg',  # ← 改成你的图片路径
        out_gaussian='noisy_gaussian.jpg',
        out_salt_pepper='noisy_salt_pepper.jpg',
        out_gauss_denoised='denoised_gaussian.jpg',
        out_median_denoised='denoised_median.jpg',
        gauss_sigma=25,  # 高斯噪声强度
        sp_ratio=0.02,  # 椒盐噪声比例（2%）
        gauss_kernel=(5, 5),  # 高斯核大小
        median_kernel=5  # 中值滤波核大小（必须为奇数）
    )
