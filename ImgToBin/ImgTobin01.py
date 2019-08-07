import cv2
img1=cv2.imread(r'E:\GitHub\PythonOpenCV\ImgToBin\dog.jpg',cv2.IMREAD_GRAYSCALE)

#图片路径不得有中文，否则后面对图片操作会产生错误，如下面resize产生错误
#cv2.error: OpenCV(4.1.0) C:\projects\opencv-python\opencv\modules\imgproc\src\resize.cpp:3718: error: (-215:Assertion failed) !ssize.empty() in function 'cv::resize'

#重新设置图片尺寸
#img1 = cv2.resize(img1,(300,300),interpolation=cv2.INTER_AREA)

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
cv2.imshow('img1',img1)
cv2.imwrite('E:\GitHub\PythonDoSomething\opcv_pic_to_bin\dog_gray.jpg',img1)

ret,binary=cv2.threshold(img1,175,255,cv2.THRESH_BINARY)
ret,binaryinv=cv2.threshold(img1,175,255,cv2.THRESH_BINARY_INV)
ret,trunc=cv2.threshold(img1,175,255,cv2.THRESH_TRUNC)
ret,tozero=cv2.threshold(img1,175,255,cv2.THRESH_TOZERO)
ret,tozeroinv=cv2.threshold(img1,175,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('binary',binary)
cv2.imwrite(r'E:\GitHub\PythonOpenCV\ImgToBin\dog_binary.jpg',binary)

cv2.imshow('binaryinv',binaryinv)
cv2.imwrite(r'E:\GitHub\PythonOpenCV\ImgToBin\dog_binaryinv.jpg',binaryinv)

cv2.imshow('trunc',trunc)
cv2.imwrite(r'E:\GitHub\PythonOpenCV\ImgToBin\dog_trunc.jpg',trunc)

cv2.imshow('tozero',tozero)
cv2.imwrite(r'E:\GitHub\PythonOpenCV\ImgToBin\dog_tozero.jpg',tozero)

cv2.imshow('tozeroinv',tozeroinv)
cv2.imwrite(r'E:\GitHub\PythonOpenCV\ImgToBin\dog_tozeroinv.jpg',tozeroinv)
#将图片保存到指定位置



