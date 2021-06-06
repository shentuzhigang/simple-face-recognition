from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.QtGui import *
import os
import sys
import cv2  #打开摄像头
import numpy
from PIL import Image, ImageDraw, ImageFont  #图像处理
from datetime import datetime  #可以用于获取当前的时间
import face_recognition   #人脸识别模块
import traceback  #异常处理
from UI_MainFrame import UI_MainFrame
from FaceTools import FaceTools


class MainFrame(QMainWindow,UI_MainFrame):
    def __init__(self):
        super(MainFrame,self).__init__()
        # self.timer_camera = QTimer()  # 需要定时器刷新摄像头界面
        self.cap = cv2.VideoCapture()  # 打开摄像头
        self.cap_flag = False
        self.face_recognize = False
        self.sign_in = False
        self.known_face_names = []
        self.known_face_encodings = []
        self.sign_in_over = []
        self.face_tools = FaceTools()
        self.initAction()
        self.show()

    def initAction(self):
        # 信号槽设置  ------------------------------

        self.left_close.clicked.connect(self.close_window)  # 关闭窗口
        self.left_mini.clicked.connect(self.Min_window)  # 最小化窗口
        self.left_visit.clicked.connect(self.MaxAndNorm_window)  #最大化窗口
        # 对打开摄像头1 按钮进行连接函数  lamda
        self.pushButton_8.clicked.connect(self.btn_camera_click)
        # 拍照按钮 连接函数
        self.pushButton_5.clicked.connect(self.btn_photo_face_click)
        # 人脸识别按钮连接函数 调用btn_face_recognition_click
        self.pushButton_4.clicked.connect(self.btn_face_recognition_click)


        self.pushButton_9.clicked.connect(self.btn_database_click) # 连接数据库
        self.pushButton_3.clicked.connect(self.btn_file_click)  # 打开文件
        self.pushButton_6.clicked.connect(self.btn_allface_click)  # 连接数据库并且打开文件

        self.pushButton_1.clicked.connect(self.btn_signin_click)  # 签到
        self.pushButton_2.clicked.connect(self.btn_signover_click)  # 结束
        self.pushButton_7.clicked.connect(self.btn_signcount_click)  # 统计

    def close_window(self):
        if self.cap.isOpened() == True:
            QMessageBox.information(self, 'warning', '请先关闭摄像头再退出')
        else:
            self.close()

    def Min_window(self):
        self.showMinimized()

    def MaxAndNorm_window(self):
        if self.isMaximized()==True:
            self.showNormal()
        else:
            self.showMaximized()

    def btn_camera_click(self):  # 打开摄像头 按钮函数
        self.progressBar.setValue(0)
        self.progressBar.setVisible(True)
        self.progressBar.setValue(10)
        if  self.cap.isOpened() == True:
            # self.cap.release()  # 关闭摄像头 对cap进行释放
            self.cap_flag = False
            self.progressBar.setValue(30)
        else:
            self.cap.open(0,cv2.CAP_DSHOW)
            self.progressBar.setValue(30)
            self.cap_flag = True
            try:
                self.open_camera()
            except Exception as err:
                print(err)
                print(traceback.format_exc())
                QMessageBox.about(self, 'warning', '摄像头不能正常打开')
            finally:
                self.progressBar.setVisible(False)

    def btn_photo_face_click(self):  # 实现保存截图的功能 图片保存在了 video_screenshot 文件夹里面  名字是根据时间命名
        if self.cap.isOpened() == False:
            QMessageBox.information(self, "Warning",self.tr("请先打开摄像头!"))
        else:
            photo_save_path = os.path.join(os.path.dirname(os.path.abspath('__file__')),'video_screenshot\\')
            print(photo_save_path + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg")
            # self.time_flag.append(datetime.now().strftime("%Y%m%d%H%M%S")
            try:
                self.showImage.save(photo_save_path + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg")
            except Exception as err:
                QMessageBox.information(self, "Warning", self.tr("拍照错误!"))
                # print(err)
                # print(traceback.format_exc())
            QMessageBox.information(self, "Information", self.tr("拍照成功!"))

    def btn_face_recognition_click(self):  # 人脸识别按钮  通过video_btn的值来控制
        if self.cap.isOpened() == False:
            QMessageBox.information(self, "Warning",self.tr("请先打开摄像头!"))
        elif self.known_face_names==[]:
            QMessageBox.information(self, "Warning", self.tr("请先加载数据!"))
        else:
            self.face_recognize = not self.face_recognize
            if self.face_recognize:
                self.pushButton_4.setText(u'关闭识别')
            else:
                self.pushButton_4.setText(u'人脸识别')
            print("face_recognition_open")

    def btn_database_click(self):
        print("1")
        try:
            self.known_face_names, self.known_face_encodings = self.face_tools.load_faceofdatabase()
        except Exception as err:
            print(err)
            print(traceback.format_exc())

    def btn_file_click(self):
        self.known_face_names, self.known_face_encodings = self.face_tools.load_faceoffile()

    def btn_allface_click(self):
        file_known_face_names, file_known_face_encodings = self.face_tools.load_faceoffile()
        database_known_face_names, database_known_face_encodings = self.face_tools.load_faceofdatabase()
        self.known_face_names = file_known_face_names + database_known_face_names
        print(self.known_face_names)
        self.known_face_encodings = file_known_face_encodings + database_known_face_encodings

    def btn_signin_click(self):
        self.label_9.clear()
        self.sign_in_over = []
        self.sign_in = True

    def btn_signover_click(self):
        self.sign_in = False

    def btn_signcount_click(self):
        print("counting")

    def open_camera(self):
        self.progressBar.setValue(50)
        print('打开摄像头')
        self.pushButton_8.setText(u'关闭摄像头')
        self.progressBar.setValue(100)
        self.progressBar.setVisible(False)
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        while (self.cap.isOpened() and self.cap_flag):
            ret, frame = self.cap.read()
            QApplication.processEvents()

            # sp = frame.shape
            # print(sp)
            # sz1 = sp[0]  # height(rows) of image
            # sz2 = sp[1]  # width(colums) of image
            # sz3 = sp[2]  # the pixels value is made up of three primary colors
            # print('width: %d \nheight: %d \nnumber: %d' % (sz1, sz2, sz3))

            if self.face_recognize == True:
                # 改变摄像头图像的大小，图像小，所做的计算就少
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # opencv的图像是BGR格式的，而我们需要是的RGB格式的，因此需要进行一个转换。
                rgb_small_frame = small_frame[:, :, ::-1]

                if process_this_frame:
                    QApplication.processEvents()
                    # 根据encoding来判断是不是同一个人，是就输出true，不是为flase
                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                    face_names = []
                    for face_encoding in face_encodings:
                        # 默认为unknown
                        matches = face_recognition.compare_faces(
                                                        self.known_face_encodings,
                                                        face_encoding,
                                                        tolerance=0.4)
                        # 阈值太低容易造成无法成功识别人脸，太高容易造成人脸识别混淆 默认阈值tolerance为0.6
                        name = "Unknown"
                        # If a match was found in known_face_encodings, just use the first one.
                        # If a match
                        if True in matches:
                            # use the known face with the smallest distance to face
                            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                            best_match_index = numpy.argmin(face_distances)
                            if matches[best_match_index]:
                                name = self.known_face_names[best_match_index]
                        face_names.append(name)
                process_this_frame = not process_this_frame
                # 将捕捉到的人脸显示出来
                self.set_name = set(face_names)
                # 把名字先设为了一个 集合 把重复的去掉 再设为tuple 以便于下面显示其他信息和记录 调用
                self.set_names = tuple(self.set_name)
                print(self.set_names)  # 把人脸识别检测到的人 用set_names 这个集合收集起来
                # Display the results
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # 显示信息
                    self.show_info(name)

                    # 由于我们检测到的帧被缩放到1/4大小，所以要缩小面位置
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    color=(0, 0, 255)
                    # 签到模块
                    if self.sign_in == True:
                        if name in self.sign_in_over:
                            color=(0, 255, 0)
                        else:
                            if name != "Unknown":
                                self.sign_in_over.append(name)
                                if len(self.sign_in_over) % 20 ==0:
                                    self.label_9.setText("")
                                self.label_9.setText(self.label_9.text() +
                                                     datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": " +
                                                     name + "<font color=green>已签到</font>" + "<br>")
                                # self.label_9.setScaledContents(True)
                    # 矩形框
                    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left - 1, bottom + 35), (right + 1, bottom), color, cv2.FILLED)

                    # 由于 opencv无法显示汉字 之前使用的方法当照片很小时会报错，此次采用了另一种方法使用PIL进行转换
                    # cv2和PIL中颜色的hex码的储存顺序不同
                    cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    pilimg = Image.fromarray(cv2img)
                    draw = ImageDraw.Draw(pilimg)  # 图片上打印
                    # 参数1：字体文件路径，参数2：字体大小
                    font = ImageFont.truetype("font/msyh.ttf", 27, encoding="utf-8")
                    str_len = len(name)
                    # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
                    draw.text(((left + right)/2 - str_len * 9, bottom), name, (220, 20, 60),font=font)

                    # PIL图片转cv2 图片
                    frame = cv2.cvtColor(numpy.array(pilimg), cv2.COLOR_RGB2BGR)

            show_video = cv2.resize(frame, (960, 720))
            show_video = cv2.cvtColor(show_video, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
            # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
            self.showImage = QImage(show_video.data, show_video.shape[1], show_video.shape[0], QImage.Format_RGB888)
            self.label_5.setPixmap(QPixmap.fromImage(self.showImage))

        #  因为他最后会存留一张 图像在lable上需要对 lable_5进行清理
        self.label_5.setPixmap(QPixmap(""))
        try:
            self.cap.release()
            self.close_camera()
        except:
            QMessageBox.about(self, 'warning', '摄像头不能正常关闭')
        finally:
            self.progressBar.setVisible(False)

    def close_camera(self):
        self.progressBar.setValue(30)
        if self.cap.isOpened() == False:
            print('关闭摄像头')
            self.progressBar.setValue(50)
            self.pushButton_8.setText(u'打开摄像头')
            self.label_5.setPixmap(QPixmap(""))
            self.progressBar.setValue(80)
            self.label_5.setText('\nZ S T U\nFace Recognition\nSign-in System')
            # self.timer_camera.stop()
        self.progressBar.setValue(100)
        self.progressBar.setVisible(False)

    def show_info(self,id):
        result = self.face_tools.sreach_stuinfo(id)
        self.label_1.setText(result[2])
        self.label_2.setText(result[0])
        self.label_3.setText(result[4])
        self.label_4.setText(result[3])
        self.label_6.setText(result[1])
        self.label_7.setPixmap(QPixmap("photo/me.jpg"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainFrame()
    sys.exit(app.exec_())