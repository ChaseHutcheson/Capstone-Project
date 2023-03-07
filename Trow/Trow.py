from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from googletrans import Translator
import time
Builder.load_file("Trow.kv")


class MainMenu(Screen):
    pass

class PhotoTranslate(Screen):
    def capture(self):
        camera = self.ids['cam']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TextTranslate(Screen):
    def translation(self):
        text = self.ids.text_untranslated.text
        translator = Translator()
        translation = translator.translate(f'{text}', dest='es')
        self.ids.text_translated.text = f"{translation.text}"

class TranslateHistory(Screen):
    pass

class Main(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(PhotoTranslate(name='photo_translate'))
        sm.add_widget(TextTranslate(name='text_translate'))
        sm.add_widget(TranslateHistory(name='history'))
        return sm

if __name__ == '__main__':
    Main().run()