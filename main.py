from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

try:
    from plyer import flashlight, tts
    HAS_PLYER = True
except:
    HAS_PLYER = False

class JarvisLayout(BoxLayout):
    def __init__(self, **kw):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kw)
        self.add_widget(Label(text='JARVIS • ONLINE', font_size=30, color=(0,1,1,1), bold=True))
        self.status = Label(text='Pronto chefe. Comandos: hora, ligar lanterna, desligar lanterna', font_size=16)
        self.add_widget(self.status)
        self.input_cmd = TextInput(hint_text='Digite sua ordem...', size_hint_y=None, height=50, multiline=False)
        self.input_cmd.bind(on_text_validate=self.executar)
        self.add_widget(self.input_cmd)
        btn = Button(text='EXECUTAR ORDEM', size_hint_y=None, height=60, background_color=(0,0.8,0.8,1))
        btn.bind(on_press=self.executar)
        self.add_widget(btn)
        self.falar('Jarvis online')

    def falar(self, txt):
        self.status.text = txt
        if HAS_PLYER:
            try: tts.speak(txt)
            except: pass

    def executar(self, *args):
        cmd = self.input_cmd.text.lower()
        self.input_cmd.text = ''
        if not cmd: return
        if 'hora' in cmd:
            self.falar(f"São {datetime.now().strftime('%H:%M')}, chefe")
        elif 'liga' in cmd and 'lanterna' in cmd:
            try: flashlight.on(); self.falar('Lanterna ligada')
            except: self.falar('Lanterna ligada (simulado)')
        elif 'desliga' in cmd and 'lanterna' in cmd:
            try: flashlight.off(); self.falar('Lanterna desligada')
            except: self.falar('Lanterna desligada')
        elif 'oi' in cmd or 'ola' in cmd:
            self.falar('Olá chefe, pronto pra missão')
        else:
            self.falar(f'Entendi: {cmd}')

class JarvisApp(App):
    def build(self): return JarvisLayout()

JarvisApp().run()
