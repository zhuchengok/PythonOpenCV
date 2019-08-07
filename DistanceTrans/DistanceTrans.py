import cv2
img1=cv2.imread(r'E:\GitHub\PythonOpenCV\DistanceTrans\reel01.jpg')
#img1=cv2.imread(r'E:\GitHub\PythonOpenCV\DistanceTrans\dog.jpg',cv2.IMREAD_GRAYSCALE)

#图片路径不得有中文，否则后面对图片操作会产生错误，如下面resize产生错误
#cv2.error: OpenCV(4.1.0) C:\projects\opencv-python\opencv\modules\imgproc\src\resize.cpp:3718: error: (-215:Assertion failed) !ssize.empty() in function 'cv::resize'

#重新设置图片尺寸
#img1 = cv2.resize(img1,(300,300),interpolation=cv2.INTER_AREA)

#参数说明
#参数说明
#IMREAD_UNCHANGED 按原样返回图片
#IMREAD_GRAYSCALE 将图片转为灰阶图片返回
#IMREAD_COLOR     默认彩色打开图片
#IMREAD_ANYDEPTH  返回对应深度的图像16或32，否则返回8位图像
#IMREAD_ANYCOLOR  返回对应的格式图像

#使用相对路径
#img1=cv2.imread(r'.\CellImg.bmp',cv2.IMREAD_GRAYSCALE) 

#使用控制台show图片时，必须waitKey，否则图片显示一片灰色，属于阻塞状态。
#cv2.imshow('img1',img1)
#k=cv2.waitKey(0)

img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

#img_RGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#img_HSV = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
#img_YcrCb = cv2.cvtColor(img1, cv2.COLOR_BGR2YCrCb)
#img_HLS = cv2.cvtColor(img1, cv2.COLOR_BGR2HLS)
#img_XYZ = cv2.cvtColor(img1, cv2.COLOR_BGR2XYZ)
#img_LAB = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)
#img_YUV = cv2.cvtColor(img1, cv2.COLOR_BGR2YUV)

ret,binary=cv2.threshold(img_gray,175,255,cv2.THRESH_BINARY)
ret,binaryinv=cv2.threshold(img_gray,175,255,cv2.THRESH_BINARY_INV)
#ret,trunc=cv2.threshold(img_gray,175,255,cv2.THRESH_TRUNC)
#ret,tozero=cv2.threshold(img_gray,175,255,cv2.THRESH_TOZERO)
#ret,tozeroinv=cv2.threshold(img_gray,175,255,cv2.THRESH_TOZERO_INV)

#opening = cv2.morphologyEx(binaryinv, cv2.MORPH_OPEN, kernel, iterations=2)
dist_img = cv2.distanceTransform(binaryinv,cv2.DIST_L2,3)

dist1 = cv2.convertScaleAbs(dist_img)
dist2 = cv2.normalize(dist_img,None,255,0,cv2.NORM_MINMAX,cv2.CV_8UC1)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',dist1)
#cv2.imshow('image',dist2)
cv2.waitKey(0)
cv2.destroyAllWindows()








