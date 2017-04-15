import _smtp
import smtplib
import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit,
                             QPushButton, QApplication, QDesktopWidget,
                             qApp, QVBoxLayout, QGridLayout, QMessageBox)

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


class loginPage(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        username = QLabel('Username')
        password = QLabel('Password')

        self.userEntry = QLineEdit()
        self.pwdEntry = QLineEdit()
        self.pwdEntry.setEchoMode(QLineEdit.Password)

        login = QPushButton("Login", self)
        login.setStyleSheet("color:white;"
                            "background-color:#4b8ef9;"
                            "font: bold")
        login.clicked.connect(self.login)

        # clear = QPushButton("Clear", self)

        grid = QGridLayout()

        grid.addWidget(username, 1, 0)
        grid.addWidget(self.userEntry, 1, 1)

        grid.addWidget(password, 2, 0)
        grid.addWidget(self.pwdEntry, 2, 1)

        LayOut = QVBoxLayout()
        LayOut.addLayout(grid)
        LayOut.addWidget(login)

        self.setLayout(LayOut)
        self.setGeometry(400, 400, 400, 200)
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon('icon.png'))

        self.setFont(QFont('Microsoft Yahei', 10))

        self.center()
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def login(self):

        username = str(self.userEntry.text()).strip()
        passwd = str(self.pwdEntry.text()).strip()

        if len(username) == 0 or len(passwd) == 0 or '@' not in username:
            QMessageBox.warning('Warning:', 'Invalid email format.')
            self.clear()
            self.userEntry.focus_set()
            return
        try:
            proxy = _smtp.proxy(username, passwd)
            self.hide()
            self.mySendMail = mailBoxPage(proxy, username)

        except smtplib.SMTPConnectError:
            QMessageBox.warning(
                'ConnYection Error', "Can't connect to server!")
        except smtplib.SMTPAuthenticationError as auth:
            QMessageBox.warning(
                'Authentication error!', 'Invalid username or password!')
        except smtplib.SMTPHeloError as helo:
            QMessageBox.warning('Hello error!', helo)
        except smtplib.SMTPException as e:
            QMessageBox.warning('Connection error!', e)


class mailBoxPage(QWidget):

    def __init__(self, proxy, sender):
        super().__init__()

        self.proxy = proxy
        self.sender = sender

        self.authorEdit = QLineEdit("To: ")
        self.titleEdit = QLineEdit("Subject: ")
        self.textEdit = QTextEdit()
        self.sendButton = QPushButton("Send")

        self.authorEdit.setStyleSheet(
            "color: grey;"
            "border-width:0;"
            "margin-top: 5;"
            "margin-bottom: 4;"
            "padding-top:4;"
            "margin-left:15;margin-right:15")

        self.titleEdit.setStyleSheet(
            "color: grey;"
            "border-width:0;"
            "margin-top: 10;"
            "margin-bottom: 5;"
            "padding-top: 5;"
            "margin-left:15;"
            "margin-right:15;")

        self.textEdit.setStyleSheet(
            "color: black;"
            "border-width: 0;"
            "margin-bottom: 15;"
            "margin-left:15;"
            "margin-right:15")

        self.sendButton.setStyleSheet(
            "color: white;"
            "background-color: #4b8ef9;"
            "border-radius: 5px;"
            "border-color:#4b8ef9;"
            "margin-left:5;"
            "margin-right:660;"
            "margin-bottom:5;"
            "font: bold"
        )

        bodyLayout = QVBoxLayout()
        bodyLayout.addSpacing(0)
        bodyLayout.setContentsMargins(0, 10, 0, 0)
        bodyLayout.addWidget(self.authorEdit)
        bodyLayout.addWidget(self.titleEdit)
        bodyLayout.addWidget(self.textEdit)
        bodyLayout.addWidget(self.sendButton)

        self.setStyleSheet("background-color:#f5f5f5;"
                           "border-style: solid;"
                           "border-width: 2px;"
                           "border-color:  #c1c5c8;")
        self.setLayout(bodyLayout)
        self.setGeometry(300, 300, 750, 620)
        self.setWindowTitle('MailBox')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.lightGray, 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(0, 50, 750, 50)
        qp.drawLine(0, 90, 750, 90)
        qp.drawLine(0, 590, 750, 590)

    def sendMail(self):

        def wraper():
            sendToAdd = str(self.authorEdit.text()).strip()
            subjectInfo = str(self.titleEdit.text()).strip()
            sendTextInfo = str(self.textEdit.text())
            body = {"From": self.sender, "To": sendToAdd,
                    "Subject": subjectInfo, "Text": sendTextInfo}
            return body

        QMessageBox.information('Test', wraper())

        try:
            self.proxy.sendMail(wraper())

        except smtplib.SMTPSenderRefused as e:
            QMessageBox.warning('Invalid sender!', e)
            return
        except smtplib.SMTPRecipientsRefused as e:
            QMessageBox.warning('Invalid Recipients!', e)
            return
        except Exception as e:
            QMessageBox.warning('Failed!', e)
            return
        QMessageBox.information('Success!', 'Mail has been sent!')

    def newMail(self):
        self.authorEdit.clear()
        self.titleEdit.clear()
        self.textEdit.clear()
        return


class main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.add


if __name__ == '__main__':
    def pyqt_set_trace():
        '''Set a tracepoint in the Python debugger that works with Qt'''
        from PyQt5.QtCore import pyqtRemoveInputHook
        import pdb
        import sys
        pyqtRemoveInputHook()
        # set up the debugger
        debugger = pdb.Pdb()
        debugger.reset()
        # custom next to get outside of function scope
        debugger.do_next(None)  # run the next command
        # frame where the user invoked `pyqt_set_trace()`
        users_frame = sys._getframe().f_back
        debugger.interaction(users_frame, None)

    app = QApplication(sys.argv)
    login = loginPage()
    sys.exit(app.exec_())
