# ASCII = ''.join(chr(x) for x in range(128))
# extended_ASCII = ''.join(chr(x) for x in range(256))
# dictionary = {i: chr(i) for i in range(128)}
# alphabet = {i: ord(i) for i in ASCII}
import sys
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_vigenere


class Vigenere:
    text = str
    key = str
    cipher = []
    original = []
    bit = 128
    keys = 0

    def __init__(self, text='', key='', cipher='', bit=128):
        self.text = text
        self.key = key
        self.original = list(text)
        self.cipher = list(cipher)
        self.bit = bit
        self.keys = len(key)

    def generate_key(self, text):
        self.key = list(self.key)
        if len(text) == len(self.key):
            return self.key
        else:
            for i in range(len(text) - len(self.key)):
                self.key.append(self.key[i % len(self.key)])
        return "".join(self.key)

    def encrypt(self):
        self.cipher = []
        if len(self.text) == len(self.key):
            for i in range(len(self.text)):
                self.cipher.append(chr((ord(self.text[i]) + ord(self.key[i])) % self.bit))
            self.original = []
            return "".join(self.cipher)
        else:
            self.key = self.generate_key(self.text)
            for i in range(len(self.text)):
                self.cipher.append(chr((ord(self.text[i]) + ord(self.key[i])) % self.bit))
            self.original = []
            return "".join(self.cipher)

    def decrypt(self):
        self.original = []
        if len(self.cipher) == len(self.key):
            for i in range(len(self.cipher)):
                self.original.append(chr((ord(self.cipher[i]) - ord(self.key[i]) + self.bit) % self.bit))
            return "".join(self.original)
        else:
            self.key = self.generate_key(self.cipher)
            for i in range(len(self.cipher)):
                self.original.append(chr((ord(self.cipher[i]) - ord(self.key[i]) + self.bit) % self.bit))
            return "".join(self.original)

    def possible_keys(self):
        return self.bit ** self.keys + self.bit


# Create app
app = QtWidgets.QApplication(sys.argv)
# init
vigenere = QtWidgets.QMainWindow()

ui = Ui_vigenere()
ui.setupUi(vigenere)
vigenere.show()

# logic
message = Vigenere(key='World')


def update_label(value):
    message.bit = value
    ui.bit_lbl.setText(str(value))
    return ui.cipher.setText(message.encrypt())


ui.bit_slider.valueChanged.connect(update_label)


def set_key():
    message.key = ui.key.toPlainText()
    return ui.cipher.setText(message.encrypt())


def set_text():
    message.text = ui.text.toPlainText()
    return ui.cipher.setText(message.encrypt())


ui.key.textChanged.connect(set_key)
ui.text.textChanged.connect(set_text)

sys.exit(app.exec_())
