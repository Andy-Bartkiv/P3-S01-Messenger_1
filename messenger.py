from PyQt5 import QtWidgets
from PyQt5 import QtCore
import clientui
import requests
import time
import datetime

class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле clientui.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.pushButton.pressed.connect(self.button_pushed)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def button_pushed(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        text = self.MessageWindow.toPlainText()

        self.send_message(username, password, text)

        self.MessageWindow.setText('')

    def send_message(self,username, password, text):
        message = {'username': username, 'password': password, 'text': text}
        try:
            response = requests.post('http://127.0.0.1:5000/send', json = message)
            if response.status_code == 401:
                self.show_text('Wrong Password')
            elif response.status_code != 200:
                self.show_text('Server Connection Error: POST')
        except:
            self.show_text('Server Connection Error: POST')

    def update_messages(self):
        try:                
            response = requests.get(
                'http://127.0.0.1:5000/msgs', 
                params={'after': self.after})
            data = response.json()
            for message in data['messages']:
                self.print_message(message)
                self.after = message['time']
        except:
            print('Server Connection Error: GET')

    def print_message(self, message):
        username = message['username']
        message_time = message['time']
        text = message['text']
        dt = datetime.datetime.fromtimestamp(message_time)
        self.show_text(f"{dt.strftime('%X')} {username} {'>>>'} {text} \n")
 
    def show_text(self, text):
        self.textBrowser.append(text)
        self.textBrowser.repaint()

app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec_()
  
