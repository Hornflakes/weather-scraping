from kivy.core.window import Window
from kivy.config import Config
from ctypes import windll, c_int64

Window.size = (520, 320)
Config.set("graphics", "resizable", False)
Config.set("input", "mouse", "mouse,multitouch_on_demand")
windll.user32.SetProcessDpiAwarenessContext(c_int64(-4))

from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from scraper import dataToExcel


class WeatherScrapingApp(MDApp):
    def build(self):
        self.dateRangePicker()

    def dateRangePicker(self):
        datePicker = MDDatePicker()
        datePicker.overlay_color = (0, 0, 0, 0)
        datePicker.auto_dismiss = False
        datePicker.bind(on_save=self.onDateSelect, on_cancel=self.onCancel)
        datePicker.open()

    def onDateSelect(self, _, value, __):
        dataToExcel()
        print(value)
        self.stop()

    def onCancel(self, *_):
        self.stop()


app = WeatherScrapingApp()
app.run()
