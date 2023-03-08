from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.camera import Camera
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivy.metrics import dp
from googletrans import Translator
import pytesseract as pytess
pytess.pytesseract.tesseract_cmd = r'Trow\\Tesseract-OCR\\tesseract.exe'
from PIL import Image
import cv2
import time
import datetime
Builder.load_file("Trow.kv")


class MainMenu(MDScreen):
    pass

class PhotoTranslate(MDScreen):
    def capture(self):
        self.camera = self.ids['cam']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.camera.export_to_png(f"{timestr}.png")
        img = Image.open(f"{timestr}.png")
        self.translation = pytess.image_to_string(img)
        img_reverse = img.transpose(Image.FLIP_LEFT_RIGHT)
        self.translation_reverse = pytess.image_to_string(img_reverse)
        if self.translation != ' '.join([x[::-1] for x in self.translation_reverse.split(' ')]):
            img_2 = Image.open(f"{timestr}.png")
            img_2 = img_2.transpose(Image.FLIP_LEFT_RIGHT)
            self.translation = pytess.image_to_string(img_2)
        self.ids.photo_untranslated.text = f"{self.translation}"
        print(self.ids.photo_untranslated.text)

    # def reverseOutput(self):
    #     reverse = ' '.join([x[::-1] for x in self.translation.split(' ')])
    #     self.ids.photo_untranslated.text = f"{reverse}"

class TextTranslate(MDScreen):
    def translation(self, **kwargs):
        self.camera = self.ids['cam']


class TranslateHistory(MDScreen):
    pass

class Main(MDApp):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        sm = MDScreenManager()
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(PhotoTranslate(name='photo_translate'))
        sm.add_widget(TextTranslate(name='text_translate'))
        sm.add_widget(TranslateHistory(name='history'))
        return sm

if __name__ == '__main__':
    Main().run()