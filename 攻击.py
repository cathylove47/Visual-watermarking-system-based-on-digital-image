import cv2
from PIL import Image
import numpy as np
from skimage import util


"""
读取图片函数,返回ndarray
"""
def read_image(image_path):
    img = cv2.imread(image_path)
    return img
"""
对img进行椒盐噪声处理
"""
def jiaoyan_attack(img):
    noise_gs_img = util.random_noise(img, mode='s&p', seed=None, clip=True)
    noise_gs_img = np.array(255 * noise_gs_img, dtype='uint8')
    return noise_gs_img
"""
对img进行高斯噪声处理
"""
def gaussian_attack(img):
    noise_gs_img = util.random_noise(img, mode='gaussian', seed=None, clip=True)
    noise_gs_img = np.array(255 * noise_gs_img, dtype='uint8')
    return noise_gs_img

"""
这是一个测试用例
"""
if __name__ == '__main__':
    img = read_image('image_with_mark1.png')
    noise_gs_img = gaussian_attack(img)
    cv2.imshow('noise_gs_img', noise_gs_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('noise_gs_img.png', noise_gs_img)