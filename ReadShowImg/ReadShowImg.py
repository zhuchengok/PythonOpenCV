import cv2
img1=cv2.imread(r'E:\GitHub\PythonOpenCV\ReadShowImg\dog.jpg',cv2.IMREAD_UNCHANGED)
img2=cv2.imread(r'E:\GitHub\PythonOpenCV\ReadShowImg\dog.jpg',cv2.IMREAD_GRAYSCALE)
img3=cv2.imread(r'E:\GitHub\PythonOpenCV\ReadShowImg\dog.jpg',cv2.IMREAD_COLOR)
img4=cv2.imread(r'E:\GitHub\PythonOpenCV\ReadShowImg\dog.jpg',cv2.IMREAD_ANYDEPTH)
img5=cv2.imread(r'E:\GitHub\PythonOpenCV\ReadShowImg\dog.jpg',cv2.IMREAD_ANYCOLOR)

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


#使用控制台show图片时，必须waitKey，否则图片显示一片灰色，属于阻塞状态。
#cv2.imshow('img1',img1)
#k=cv2.waitKey(0)

#方法一：固定窗口显示
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


#方法二：windows窗口显示
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#WINDOW_NORMAL 适合大尺寸图片
#WINDOW_AUTOSIZE
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

