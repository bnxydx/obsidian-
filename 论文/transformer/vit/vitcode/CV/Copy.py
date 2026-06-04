import numpy as np
import matplotlib.pyplot as plt


def expand_mirror_symmetric(matrix):
    H, W = matrix.shape
    result = np.zeros((H + 2, W + 2), dtype=matrix.dtype)
    result[1:1 + H, 1:1 + W] = matrix
    row = matrix[1, :]
    col = matrix[:, 1]

    def mirror_extend(arr):
        return np.concatenate(([arr[1]], arr, [arr[-2]]))

    row_ext = mirror_extend(row)
    col_ext = mirror_extend(col)

    result[0, :] = row_ext
    result[H + 1, :] = row_ext
    result[:, 0] = col_ext
    result[:, W + 1] = col_ext

    return result


if __name__ == '__main__':
    # m = np.random.randint(1, 10, size=(4, 5))
    # print(expand_mirror_symmetric(m))
    #
    n1 = np.random.normal(0,10,100)
    n2 = np.random.normal(0,100,100)

    print(n1)
    print(n2)

    # 使用条形图（先分箱，再用 bar 展示），两个分布共用相同的 bin 边界
    bins = 20
    min_v = min(n1.min(), n2.min())
    max_v = max(n1.max(), n2.max())
    edges = np.linspace(min_v, max_v, bins + 1)
    centers = (edges[:-1] + edges[1:]) / 2
    width = edges[1] - edges[0]

    counts1, _ = np.histogram(n1, bins=edges)
    counts2, _ = np.histogram(n2, bins=edges)

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.bar(centers, counts1, width=width, color='steelblue', alpha=0.85, edgecolor='black')
    plt.title('Normal(0, 10)')
    plt.xlabel('value')
    plt.ylabel('count')

    plt.subplot(1, 2, 2)
    plt.bar(centers, counts2, width=width, color='tomato', alpha=0.85, edgecolor='black')
    plt.title('Normal(0, 100)')
    plt.xlabel('value')
    plt.ylabel('count')

    plt.tight_layout()
    plt.savefig('bar.png', dpi=150)
    plt.close()

"""



    print("所有图片已保存：")
    print(f"   [1] 高斯噪声图     → {out_gaussian}")
    print(f"   [2] 椒盐噪声图     → {out_salt_pepper}")
    print(f"   [3] 高斯滤波去噪   → {out_gauss_denoised}")
    print(f"   [4] 中值滤波去噪   → {out_median_denoised}")
"""