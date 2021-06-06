import sys
import qtawesome
from PyQt5 import QtWidgets,QtGui,QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QAction,qApp
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class UI_MainFrame(object):
    def __init__(self):
        super().__init__()
        self.initFrame()
    def initFrame(self):
        self.resize(1600, 900)
        self.centerFrame()
        self.setWindowTitle('浙江理工大学人脸识别课堂签到系统')  # 设置标题
        self.setWindowIcon(QIcon('icon/icon.png'))  # 设置logo
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # 初始化菜单
        # self.initMenu()
        # 初始化状态栏
        # self.initStatusBar()
        # 初始化主体
        self.initUI()
        # 美化主体
        self.beautifyUI()
        self.show()

    def initUI(self):
        self.main_widget = QWidget(self)  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QWidget(self)  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.middle_widget = QWidget(self)  # 创建中间部件
        self.middle_widget.setObjectName('middle_widget')
        self.middle_layout = QtWidgets.QGridLayout()
        self.middle_widget.setLayout(self.middle_layout)  # 设置中间部件布局为网格

        self.right_widget = QtWidgets.QWidget(self)  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()  # 创建右侧部件的网格布局层
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 4)  # 左侧部件在第0行第0列，占12行4列
        self.main_layout.addWidget(self.middle_widget, 0, 4, 12, 8)  # 中间部件在第0行第2列，占12行8列
        self.main_layout.addWidget(self.right_widget, 0, 12, 12, 4)  # 右侧部件在第0行第3列，占12行4列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_layout.setContentsMargins(0, 0, 0, 0)  # 设置左边布局 左右间距为0 去掉间隙  左 上 右 下
        self.middle_layout.setContentsMargins(0, 0, 0, 0)  # 设置中边布局 左右间距为0 去掉间隙  左 上 右 下
        self.right_layout.setContentsMargins(0, 0, 0, 0)  # 设置右边布局 左右间距为0 去掉间隙  左 上 右 下

        self.main_layout.setSpacing(0)  # 们通过设置布局内部件的间隙来把那条缝隙去除掉：
        self.right_layout.setSpacing(0)
        self.middle_layout.setSpacing(0)
        self.left_layout.setSpacing(0)

        # 在左侧菜单模块中，继续使用网格对部件进行布局。在左侧菜单的布局中添加按钮部件QPushButton()左侧菜单的按钮、
        # 菜单列提示和整个窗口的最小化和关闭按钮。

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("IMAGE")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("MODEL")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("SIGN IN")
        self.left_label_3.setObjectName('left_label')

        self.pushButton_8 = QtWidgets.QPushButton(qtawesome.icon('fa5s.video', color='white'), "打开摄像头")
        self.pushButton_8.setObjectName('left_button')
        self.pushButton_5 = QtWidgets.QPushButton(qtawesome.icon('fa5s.camera', color='white'), "拍照保存")
        self.pushButton_5.setObjectName('left_button')
        self.pushButton_4 = QtWidgets.QPushButton(qtawesome.icon('fa5s.eye', color='white'), "人脸识别")
        self.pushButton_4.setObjectName('left_button')

        self.pushButton_9 = QtWidgets.QPushButton(qtawesome.icon('fa5s.database', color='white'), "在线模式")
        self.pushButton_9.setObjectName('left_button')
        self.pushButton_3 = QtWidgets.QPushButton(qtawesome.icon('fa5s.unlink', color='white'), "离线模式")
        self.pushButton_3.setObjectName('left_button')
        self.pushButton_6 = QtWidgets.QPushButton(qtawesome.icon('fa5s.cubes', color='white'), "双线模式")
        self.pushButton_6.setObjectName('left_button')

        self.pushButton_1 = QtWidgets.QPushButton(qtawesome.icon('fa5s.folder-open', color='white'), "开始签到")
        self.pushButton_1.setObjectName('left_button')
        self.pushButton_2 = QtWidgets.QPushButton(qtawesome.icon('fa5s.file-excel', color='white'), "结束签到")
        self.pushButton_2.setObjectName('left_button')
        self.pushButton_7 = QtWidgets.QPushButton(qtawesome.icon('fa5s.sliders-h', color='white'), "签到统计")
        self.pushButton_7.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 在这里，我们使用qtawesome这个第三方库来实现按钮中的Font Awesome字体图标的显示。
        # 然后将创建的按钮添加到左侧部件的网格布局层中：

        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_mini, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.pushButton_8, 2, 0, 1, 3)
        self.left_layout.addWidget(self.pushButton_5, 3, 0, 1, 3)
        self.left_layout.addWidget(self.pushButton_4, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.pushButton_9, 6, 0, 1, 3)
        self.left_layout.addWidget(self.pushButton_3, 7, 0, 1, 3)
        self.left_layout.addWidget(self.pushButton_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.pushButton_1, 10, 0, 1, 3)
        self.left_layout.addWidget(self.pushButton_2, 11, 0, 1, 3)
        self.left_layout.addWidget(self.pushButton_7, 12, 0, 1, 3)

        # 进行设置右侧控件

        self.label_5 = QtWidgets.QLabel('\nZ S T U\nFace Recognition\nSign-in System')
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setFont(QFont("Roman times", 18, QFont.Bold))
        self.label_5.setStyleSheet("QLabel{background:darkgray;}"
                                   "QLabel{color:white;font-size:80px;font-weight:bold;font-family:Roman times;}"
                                   )
        self.label_5.setMinimumSize(QtCore.QSize(1080, 600))
        self.label_5.setMaximumSize(QtCore.QSize(1080, 600))
        # self.label_5.setScaledContents(True)  #让照片能够在label上面自适应大小
        self.label_5.setObjectName('lable_')

        self.middle_layout.addWidget(self.label_5, 1, 0, 3, 16)  # 显示摄像头画面的lable


        self.label_7 = QtWidgets.QLabel('')
        self.label_7.setObjectName('lable_')
        self.label_2 = QtWidgets.QLabel('')
        self.label_2.setObjectName('lable_')
        self.label_6 = QtWidgets.QLabel('')
        self.label_6.setObjectName('lable_')
        self.label_1 = QtWidgets.QLabel('')
        self.label_1.setObjectName('lable_')
        self.label_4 = QtWidgets.QLabel('')
        self.label_4.setObjectName('lable_')
        self.label_3 = QtWidgets.QLabel('')
        self.label_3.setObjectName('lable_')

        list_label = [self.label_7, self.label_2, self.label_6, self.label_4, self.label_3, self.label_1]

        self.middle_layout.addWidget(self.label_7, 5, 0, )
        self.middle_layout.addWidget(self.label_2, 5, 1, )
        self.middle_layout.addWidget(self.label_6, 5, 2, )
        self.middle_layout.addWidget(self.label_1, 5, 3, )
        self.middle_layout.addWidget(self.label_4, 5, 4, )
        self.middle_layout.addWidget(self.label_3, 5, 5, )

        for labe_size in list_label:
            labe_size.setMinimumSize(QtCore.QSize(149, 210))
            labe_size.setMaximumSize(QtCore.QSize(149, 210))

        self.label_7.setPixmap(QPixmap('icon/icon.png'))  # 把照片放到label_7上面去
        self.label_7.setScaledContents(True)
        # for lables in list_label:
        #     lables.setPixmap(QPixmap('shishi.jpg'))
        #     lables.setScaledContents(True)

        self.progressBar = QtWidgets.QProgressBar()  #
        self.progressBar.setValue(100)
        self.progressBar.setFixedHeight(11)  # 设置进度条高度
        self.progressBar.setTextVisible(False)  # 不显示进度条文字
        self.progressBar.setVisible(False)

        self.middle_layout.addWidget(self.progressBar, 0, 0, 1, 16)  # 进度条

        self.label_8 = QtWidgets.QLabel('实时签到:')
        self.label_8.setObjectName('lable_')
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setFont(QFont("Roman times", 8, QFont.Bold))
        self.label_8.setStyleSheet('''QLabel{
                                    background:Gray;
                                    border:none;
                                    color:white;
                                    font-size:20px;
                                    font-weight:bold;
                                    font-family:Roman times;
                                    padding:5px;
                                    }
                                   ''')
        self.right_layout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QtWidgets.QLabel('')
        self.label_9.setObjectName('lable_')
        self.label_9.setAlignment(Qt.AlignLeft)
        self.label_9.setFont(QFont("Roman times", 6, QFont.Bold))
        self.label_9.setStyleSheet('''QLabel{
                                    background:Gray;
                                    border:none;
                                    color:white;
                                    font-size:15px;
                                    font-weight:bold;
                                    font-family:Roman times;
                                    padding:5px;
                                    }
                                   ''')
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)
        self.right_layout.addWidget(self.label_9, 1, 0, 11, 1)

    # 美化
    def beautifyUI(self):
        self.left_close.setFixedSize(30, 30)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(30, 30)  # 设置按钮大小
        self.left_mini.setFixedSize(30, 30)  # 设置最小化按钮大小

        # 然后，通过setStyleSheet()方法，设置按钮部件的QSS样式，在这里，左侧按钮默认为淡绿色，
        # 鼠标悬浮时为深绿色；中间按钮默认为淡黄色，鼠标悬浮时为深黄色；右侧按钮默认为浅红色，鼠标悬浮时为红色。
        # 所以它们的QSS样式设置如下所示：
        self.left_close.setStyleSheet('''
                                    QPushButton{
                                        background:#F76677;
                                        border-radius:15px;
                                    }
                                    QPushButton:hover{
                                        background:red;
                                    }
                                ''')
        self.left_visit.setStyleSheet('''
                                    QPushButton{
                                        background:#F7D674;
                                        border-radius:15px;
                                    }
                                    QPushButton:hover{
                                        background:yellow;
                                    }
                                ''')
        self.left_mini.setStyleSheet('''
                                    QPushButton{
                                        background:#6DDF6D;
                                        border-radius:15px;
                                    }
                                    QPushButton:hover{
                                        background:green;
                                    }
                                ''')
        # 左侧菜单按钮
        # 因为最后的图形界面中，左侧的部件背景是灰色的，
        # 所以我们需要将左侧菜单中的按钮和文字颜色设置为白色，并且将按钮的边框去掉，在left_widget中设置qss样式为：
        self.left_widget.setStyleSheet('''
                            QPushButton{
                                border:none;
                                color:white;
                                padding-left:5px;
                                height:35px;
                                font-size:15px;
                                padding-right:10px;}
                            QPushButton#left_label{
                                border:none;
                                border-bottom:1px solid white;
                                font-size:20px;
                                font-weight:700;
                                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                            }
                            QWidget#left_widget{
                                background:Gray;
                                border-top:1px solid white;
                                border-bottom:1px solid white;
                                border-left:1px solid white;
                                border-top-left-radius:10px;
                                border-bottom-left-radius:10px;
                            }
                            QPushButton#left_button:hover{ color:white;
                                    border:2px solid #F3F3F5;
                                    border-radius:15px;
                                    background:black;}
                        ''')

        self.middle_widget.setStyleSheet('''
                            QWidget#middle_widget{
                                color:#232C51;
                                background:darkGray;
                            }
                        ''')
        self.right_widget.setStyleSheet('''
                            QWidget#right_widget{
                                background:Gray;
                                border-top:1px solid white;
                                border-bottom:1px solid white;
                                border-right:1px solid white;
                                border-top-right-radius:10px;
                                border-bottom-right-radius:10px;
                            }
                        ''')
        # 进度条 美化
        self.progressBar.setStyleSheet('''
                        QProgressBar::chunk {
                            background-color: green;
                        }
                    ''')
    def initMenu(self):
        # exit Action
        exitAction = QAction(QIcon('icon/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        # 添加事件
        fileMenu.addAction(exitAction)
    def initStatusBar(self):
        self.statusBar().showMessage('Ready')
    def centerFrame(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 下面这三个函数通过重写 能够实现隐藏边框进行拖动窗口
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI_MainFrame()
    sys.exit(app.exec_())
