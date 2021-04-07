import sys
import random
import string
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-'}

class window(QWidget):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)

        #initialising window
        self.setGeometry(300, 200, 500, 600)
        self.setFixedSize(500,600)
        self.setWindowTitle("Morse Code Learner")
        self.setStyleSheet("background-color:#383A59")

        #main label
        self.letter_lab = QLabel(self)
        self.generateAlphabets()
        self.letter_lab.resize(40, 50)
        self.letter_lab.setAlignment(Qt.AlignCenter)
        self.letter_lab.move(250-20, 200-25)
        self.letter_lab.setFont(QFont('Andale Mono', 50, QFont.Bold))
        self.letter_lab.setStyleSheet("border: 3px solid blue;color:#FFFFFF")

        #text input box
        self.textbox = QLineEdit(self)
        regex = QRegExp("[.-]+")
        validator = QRegExpValidator(regex)
        self.textbox.setValidator(validator)
        self.textbox.move(250-100, 250-25)
        self.textbox.resize(200,50)
        self.textbox.setFont(QFont('Andale Mono', 30, QFont.Bold))
        self.textbox.setStyleSheet("color:#FFFFFF")

        #submit button
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.move(150-10,300)
        self.submit_button.resize(100, 50)
        self.submit_button.setFont(QFont('Andale Mono', 25, QFont.Bold))
        self.submit_button.setStyleSheet("QPushButton {background-color: green; color: #FFFFFF;}")
        self.submit_button.clicked.connect(self.on_click_submit)

        #next button
        self.next_button = QPushButton('Next', self)
        self.next_button.move(250+10,300)
        self.next_button.resize(100, 50)
        self.next_button.setFont(QFont('Andale Mono', 25, QFont.Bold))
        self.next_button.setStyleSheet("QPushButton {background-color: blue; color: #FFFFFF;}")
        self.next_button.clicked.connect(self.generateAlphabets)
        
    @pyqtSlot()
    def on_click_submit(self):
        textboxValue = self.textbox.text()
        if textboxValue == "":
            QMessageBox.information(self, 'info', 'Please Enter Valid Morse String', QMessageBox.Ok)
        else:
            valid = self.morse_validator(textboxValue)
            if valid == True:
                self.generateAlphabets()
            else:

                pass
        self.textbox.setText("")

    def generateAlphabets(self):
        letter = random.choice(list(MORSE_CODE_DICT.keys()))
        self.letter_lab.setText(letter)
    
    def morse_validator(self, input_text):
        current_letter = self.letter_lab.text()
        return MORSE_CODE_DICT[current_letter]==input_text


def main():
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()