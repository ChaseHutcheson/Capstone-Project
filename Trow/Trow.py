from kivy import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'minimum_width', '375')
Config.set('graphics', 'minimum_height', '667')
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
import time
Builder.load_file("Trow.kv")


class MainMenu(MDScreen):
    pass

class PhotoTranslate(MDScreen):
    def set_language(self, value):
        if value == "English":
            self.selected_language = "en"
        elif value == "German":
            self.selected_language = "de"
        elif value == "Spanish":
            self.selected_language = "es"
        elif value == "French":
            self.selected_language = "fr"
        elif value == "Italian":
            self.selected_language = "it"
        elif value == "Select Languages":
            self.selected_language = "en"
        
    def capture(self):
        camera = self.ids['cam']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png(f"{timestr}.png")
        img = Image.open(f"{timestr}.png")
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        text = pytess.image_to_string(img)
        translator = Translator()
        try: 
            translated = translator.translate(f'{text}', dest=self.selected_language)
        except AttributeError:
            translated = translator.translate(f'{text}', dest=self.selected_language)
        self.ids.photo_untranslated.text = f"{translated.text}"
        print(self.ids.photo_untranslated.text)

class TextTranslate(MDScreen):
    def set_language(self, value):
        if value == "English":
            self.selected_language = "en"
        elif value == "German":
            self.selected_language = "de"
        elif value == "Spanish":
            self.selected_language = "es"
        elif value == "French":
            self.selected_language = "fr"
        elif value == "Italian":
            self.selected_language = "it"
        elif value == "Select Languages":
            self.selected_language = "en"

    def translation(self): 
        text = self.ids.text_untranslated.text
        translator = Translator()
        translation = translator.translate(f'{text}', dest=self.selected_language)
        self.ids.text_translated.text = f"{translation.text}"


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