import sys
import os
import bit
import rsa
from PyQt5 import uic
import vizer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QDialog
import rsacode1
print("started")

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.do_2.clicked.connect(self.done)
        self.lang = "rus"
        self.key = 1
        self.mode.clicked.connect(self.change)
        self.keys.hide()
        self.ru_radio.clicked.connect(self.set_ru_lang)
        self.ru_radio.setChecked(True)
        self.en_radio.clicked.connect(self.set_en_lang)
        self.en_radio.hide()
        self.ru_radio.hide()
        self.label_3.hide()
        self.list_tapped()
        self.method_list.activated.connect(self.list_tapped)
        self.method_list.setCurrentIndex(0)
        self.create_key_button.hide()
        self.create_key_button.clicked.connect(self.open_dialog)

    def set_ru_lang(self):
        self.lang = "rus"
        if self.method_list.currentIndex() == 1:
            self.keys.setText("пёс")

    def set_en_lang(self):
        self.lang = "eng"
        if self.method_list.currentIndex() == 1:
            self.keys.setText("dog")

    def list_tapped(self):
        if self.method_list.currentIndex() == 0:
            self.ru_radio.hide()
            self.en_radio.hide()
            self.keys.show()
            self.label_3.show()
            self.label_3.setText("Сдвиг:")
            self.keys.setText("2")
            self.create_key_button.hide()

        elif self.method_list.currentIndex() == 1:
            self.ru_radio.show()
            self.en_radio.show()
            self.keys.show()
            self.label_3.show()
            self.label_3.setText("Ключ:")
            if self.lang == "eng":
                self.keys.setText("dog")
            else:
                self.keys.setText("пёс")
            self.create_key_button.hide()

        elif self.method_list.currentIndex() == 2:
            self.ru_radio.hide()
            self.en_radio.hide()
            self.label_3.hide()
            self.keys.hide()
            self.create_key_button.show()

        elif self.method_list.currentIndex() == 3:
            self.ru_radio.hide()
            self.en_radio.hide()
            self.label_3.hide()
            self.keys.hide()
            self.create_key_button.hide()

    def open_dialog(self):
        ex1 = Dialog(parent=self)
        ex1.show()

    def done(self):
        if self.method_list.currentIndex() == 0:
            eng = 'abcdefghijklmnopqrstuvwxyz'
            ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            n = int(self.keys.text())
            s = self.input_text.text().strip()
            res = ""
            if self.key == 1:
                for c in s:
                    if c in eng:
                        res += eng[(eng.index(c) + n) % len(eng)]
                    elif c in eng.upper():
                        res += eng.upper()[(eng.upper().index(c) + n) % len(eng.upper())]
                    elif c in ru:
                        res += ru[(ru.index(c) + n) % len(ru)]
                    elif c in ru.upper():
                        res += ru.upper()[(ru.upper().index(c) + n) % len(ru.upper())]
                    else:
                        res += c
            else:
                for c in s:
                    if c in eng:
                        res += eng[(eng.index(c) - n) % len(eng)]
                    elif c in eng.upper():
                        res += eng.upper()[(eng.upper().index(c) - n) % len(eng.upper())]
                    elif c in ru:
                        res += ru[(ru.index(c) - n) % len(ru)]
                    elif c in ru.upper():
                        res += ru.upper()[(ru.upper().index(c) - n) % len(ru.upper())]
                    else:
                        res += c
            self.output_text.setText(res)
        elif self.method_list.currentIndex() == 1:
            if self.lang == "eng":
                self.lang = 'abcdefghijklmnopqrstuvwxyz'
            else:
                self.lang = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            text = self.input_text.text().lower()
            keyword = self.keys.text().lower()
            if self.key == 1:
                self.output_text.setText(vizer.viz(text, keyword, self.lang))
            else:
                self.output_text.setText(vizer.viz_enc(text, keyword, self.lang))

        elif self.method_list.currentIndex() == 2:
            if self.key == 1:
                self.output_text.setText(rsacode1.rsa_encode_p(self.input_text.text()))
            else:
                rsacode1.rsa_decode_p(self.input_text.text())
                self.output_text.setText(rsacode1.rsa_decode_p(self.input_text.text()))

        elif self.method_list.currentIndex() == 3:
            if self.key == 1:
                self.output_text.setText(bit.text_to_bits(self.input_text.text()))

            else:
                self.output_text.setText(bit.text_from_bits(''.join(self.input_text.text().split(" "))))

    def change(self):
        self.key *= -1
        if self.key == -1:
            self.mode.setText("Режим: Расшифровка")
        else:
            self.mode.setText("Режим: Шифрование")


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        uic.loadUi('dialog.ui', self)
        self.bitsize = 512
        self.generate_key.clicked.connect(self.save_keys)
        self.folder_open_button.clicked.connect(self.open_folder)
        self.keysize.activated.connect(self.change_vaules)

    def open_folder(self):
        os.startfile(os.path.realpath("keys"))

    def change_vaules(self):
        if self.keysize.currentIndex() == 0:
            self.bitsize = 512
            self.time_gen.setText("Среднее время генерации ключей: 0.11 сек")
        elif self.keysize.currentIndex() == 1:
            self.bitsize = 1024
            self.time_gen.setText("Среднее время генерации ключей: 0.79 сек")
        elif self.keysize.currentIndex() == 2:
            self.bitsize = 2048
            self.time_gen.setText("Среднее время генерации ключей: 6.55 сек")
        self.max_sim.setText(f'Максимальный размер текста: {int((self.bitsize * 0.32) // 3 - 11)} символов ')

    def save_keys(self):
        print("Начал сохранение")
        rsacode1.rsa_generate_keys(self.bitsize)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())