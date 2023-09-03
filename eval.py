import cv2 as cv

og = cv.imread('C:/Users/USER/Downloads/plsmo_512.jpg')
edited = cv.imread('plsmo_512_1.jpg')
psnr1 = cv.PSNR(edited, og)

print(f'RL PSNR: {psnr1}')

    