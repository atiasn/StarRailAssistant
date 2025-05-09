from PySide6.QtCore import Slot, QTimer, Qt, Signal
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QDialogButtonBox, QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget, QGridLayout, \
    QSpacerItem, QSizePolicy, QFrame, QLCDNumber, QHBoxLayout, QPushButton, QListWidget, QStackedWidget, QTextBrowser, \
    QMessageBox, QLineEdit

from SRACore.utils import WindowsPower
from SRACore.utils.Configure import load, save
from SRACore.utils.WindowsProcess import Popen


class DownloadDialog(QDialog):
    def __init__(self, parent, name, url):
        super().__init__(parent)
        self.setFont(QFont("MicroSoft YaHei", 13))
        self.setWindowIcon(QIcon("res/SRAicon.ico"))
        self.setWindowTitle("确认下载")
        self.url = url
        layout = QVBoxLayout(self)
        label = QLabel(f"确认要下载 {name} 吗", self)
        layout.addWidget(label)

        button_box = QDialogButtonBox(self)
        button_box.addButton("确认", QDialogButtonBox.ButtonRole.AcceptRole)
        button_box.addButton("取消", QDialogButtonBox.ButtonRole.RejectRole)
        button_box.accepted.connect(self.accept)
        button_box.accepted.connect(self.ensure)
        button_box.rejected.connect(self.reject)

        layout.addWidget(button_box)
        self.setLayout(layout)

    def ensure(self):
        command = f"SRAUpdater -u {self.url} -np"
        Popen(command)


class AnnouncementDialog(QWidget):
    action = Signal(int)

    def __init__(self, parent=None, title="title", text="text", announcement_type="Any", icon="res/SRAicon.ico"):
        super().__init__(parent)
        self.setFont(QFont("MicroSoft YaHei", 13))
        self.setWindowTitle(title)
        self.type = announcement_type
        # self.setWindowIcon(QIcon("res/SRAicon.ico"))
        # self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint,False)
        self.resize(500, 500)
        self.setLayout(QVBoxLayout())
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 600, 600))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setFixedSize(100, 100)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setStyleSheet(f"border-image: url({icon}) 0 0 0 0 stretch stretch;")

        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        button_box = QDialogButtonBox(self.scrollAreaWidgetContents)
        button_box.addButton("确认", QDialogButtonBox.ButtonRole.AcceptRole)
        button_box.addButton("不再提醒", QDialogButtonBox.ButtonRole.RejectRole)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.gridLayout.addWidget(button_box, 1, 2, 1, 1)

        self.label = QTextBrowser(self.scrollAreaWidgetContents)
        self.label.setOpenExternalLinks(True)
        self.label.setAutoFillBackground(True)
        # self.label.setWordWrap(True)

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label.setText(text)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout().addWidget(self.scrollArea)

    @Slot()
    def accept(self):
        self.action.emit(1)

    @Slot()
    def reject(self):
        self.action.emit(0)


class AnnouncementBoard(QDialog):
    def __init__(self, parent=None, title="announcements"):
        super().__init__(parent)

        # 主布局
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)
        self.resize(600, 500)
        self.setWindowTitle(title)
        self.setFont(QFont("MicroSoft YaHei", 13))
        self.setWindowIcon(QIcon("res/SRAicon.ico"))
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)

        # 左侧标题栏
        self.title_list = QListWidget()
        self.title_list.setSpacing(10)
        self.title_list.setFixedWidth(100)  # 固定宽度
        self.title_list.currentRowChanged.connect(self.on_title_clicked)

        # 右侧内容栏
        self.content_stack = QStackedWidget()

        # 添加到主布局
        self.main_layout.addWidget(self.title_list)
        self.main_layout.addWidget(self.content_stack)

        # 存储标题和内容的映射
        self.title_content_map = {}

    def add(self, dialog: AnnouncementDialog):
        """
        添加一个公告条目
        """
        # 将标题添加到左侧标题栏
        title = dialog.windowTitle()
        dialog.setParent(self)
        self.title_list.addItem(title)

        # 将内容添加到右侧内容栏
        self.content_stack.addWidget(dialog)

        # 保存标题和内容的映射关系
        self.title_content_map[title] = dialog
        dialog.action.connect(self.action_handle)

    def on_title_clicked(self, index):
        """
        当用户点击左侧标题栏时，切换右侧内容栏
        """
        self.content_stack.setCurrentIndex(index)

    def setDefault(self, index: int):
        self.title_list.setCurrentRow(index)

    def action_handle(self, action):
        self.close()
        if action == 0:
            version = load("version.json")
            version[f"Announcement.DoNotShowAgain"] = True
            save(version, "version.json")


class ShutdownDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("关机")
        self.setWindowIcon(QIcon("res/SRAicon.ico"))
        self.resize(342, 246)
        self.verticalLayout = QVBoxLayout()
        self.setLayout(self.verticalLayout)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.label = QLabel(self.frame)
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("您的计算机将在倒计时结束后关机，\n如果要取消关机，请按“取消”")
        self.verticalLayout_2.addWidget(self.label)

        self.lcdNumber = QLCDNumber(self.frame)
        self.lcdNumber.setAutoFillBackground(True)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self.lcdNumber.setProperty(u"value", 60)

        self.verticalLayout_2.addWidget(self.lcdNumber)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setFont(font)
        self.pushButton.setText("取消")
        self.pushButton.clicked.connect(WindowsPower.shutdown_cancel)
        self.pushButton.clicked.connect(self.close)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout.addWidget(self.frame)

        self.timer = QTimer(self)
        self.pushButton.clicked.connect(self.timer.stop)
        self.timer.timeout.connect(self.update_countdown)
        self.time_left = 60
        self.timer.start(1000)

    def update_countdown(self):
        """更新倒计时"""
        self.time_left -= 1
        if self.time_left < 0:
            self.timer.stop()
            self.lcdNumber.display(00)
            self.close()  # 显示00表示倒计时结束
        else:
            self.lcdNumber.display(self.time_left)


class ExceptionMessageBox(QMessageBox):
    def __init__(self, exception, value, traceback):
        super().__init__()
        self.setWindowTitle("喜报")
        self.setWindowIcon(QIcon("res/SRAicon.ico"))
        self.setIcon(QMessageBox.Icon.Critical)
        self.setFont(QFont("MicroSoft YaHei", 12))
        self.setText("SRA崩溃了! 由于以下未处理的异常: \n"
                     f"    {exception}: {value} \n"
                     "如果无法自行解决，请联系开发者！")
        self.setDetailedText(traceback)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)


class InputDialog(QDialog):
    def __init__(self, parent,title:str,text:str):
        super().__init__(parent)
        self.isAccept = False
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("res/SRAicon.ico"))
        self.setLayout(QVBoxLayout())
        self.label = QLabel(self)
        self.label.setText(text)
        self.layout().addWidget(self.label)
        self.line_edit = QLineEdit(self)
        self.layout().addWidget(self.line_edit)
        self.button_box = QDialogButtonBox()
        self.button_box.addButton(QPushButton("确认"),QDialogButtonBox.ButtonRole.AcceptRole)
        self.button_box.addButton(QPushButton("取消"),QDialogButtonBox.ButtonRole.RejectRole)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout().addWidget(self.button_box)

    def accept(self):
        super().accept()
        self.isAccept=True

    @staticmethod
    def getText(parent:QWidget,title:str,text:str):
        dialog = InputDialog(parent,title,text)
        dialog.exec()
        return dialog.line_edit.text(),dialog.isAccept

class MessageBox(QDialog):
    def __init__(self,parent,title,text):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("res/SRAicon.ico"))
        self.setLayout(QVBoxLayout())
        self.label=QLabel(self)
        self.label.setWordWrap(True)
        self.label.setText(text)
        self.layout().addWidget(self.label)
        self.ok_button=QPushButton("确认")
        self.ok_button.clicked.connect(self.accept)
        self.layout().addWidget(self.ok_button)

    @staticmethod
    def info(parent:QWidget,title:str,text:str):
        msg=MessageBox(parent,title,text)
        msg.exec()