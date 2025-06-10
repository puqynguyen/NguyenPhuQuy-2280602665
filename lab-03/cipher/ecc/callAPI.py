import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'ui')))
from ecc import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnGenKey.clicked.connect(self.call_api_generate_key)
        self.ui.btnSign.clicked.connect(self.call_api_sign)
        self.ui.btnVerify.clicked.connect(self.call_api_verify)
        
    def call_api_generate_key(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.post(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        payload = {
            "message": self.ui.txtInfor.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtSign.setText(data['signature'])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("ERROR WHILE CALLING API")
        except requests.exceptions.RequestException as e:
            print("ERROR: %s" % e)

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        payload = {
            "message": self.ui.txtInfor.toPlainText(),
            "signature": self.ui.txtSign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data['is_verified']:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified FAIL")
                    msg.exec_()
            else:
                print("ERROR WHILE CALLING API")
        except requests.exceptions.RequestException as e:
            print("ERROR: %s" % e)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())