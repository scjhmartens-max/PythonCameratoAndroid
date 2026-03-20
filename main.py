from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse
from kivy.core.window import Window

class CameraApp(App):
    def build(self):
        self.layout = FloatLayout()

        # 1. Camera (vult scherm)
        self.camera = Camera(play=True, resolution=(1280, 720), allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.camera)

        # 2. Preview Image (opacity=0 maakt het onzichtbaar)
        self.preview = Image(opacity=0, allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.preview)

        # 3. Grote ronde sluiterknop
        self.capture_btn = Button(size_hint=(None, None), size=('120dp', '120dp'),
                                  pos_hint={'center_x': 0.5, 'y': 0.05}, background_color=(0,0,0,0))
        
        with self.capture_btn.canvas:
            self.btn_color = Color(1, 1, 1, .8)
            self.btn_circle = Ellipse(size=self.capture_btn.size, pos=self.capture_btn.pos)
        
        self.capture_btn.bind(pos=self.update_ui_elements, size=self.update_ui_elements)
        self.capture_btn.bind(on_press=self.process_action)
        self.layout.add_widget(self.capture_btn)

        # 4. Slider voor helderheid (alleen zichtbaar bij preview)
        self.slider = Slider(min=0, max=2, value=1, size_hint=(0.8, None), height='50dp',
                            pos_hint={'center_x': 0.5, 'top': 0.9}, opacity=0, disabled=True)
        self.slider.bind(value=self.update_brightness)
        self.layout.add_widget(self.slider)

        # 5. Annuleer knop (rood, linksboven)
        self.cancel_btn = Button(text="X", size_hint=(None, None), size=('50dp', '50dp'),
                                 pos_hint={'x': 0.05, 'top': 0.95}, opacity=0, disabled=True,
                                 background_color=(1, 0, 0, 1))
        self.cancel_btn.bind(on_press=self.reset_ui)
        self.layout.add_widget(self.cancel_btn)

        return self.layout

    def update_ui_elements(self, instance, value):
        self.btn_circle.pos = instance.pos
        self.btn_circle.size = instance.size

    def process_action(self, instance):
        if self.camera.play:
            # Foto maken en preview tonen
            self.camera.export_to_png("temp.png")
            self.preview.source = "temp.png"
            self.preview.reload() # Forceer verversing van het plaatje
            self.preview.opacity = 1
            self.camera.play = False
            
            # UI wisselen naar bewerk-modus
            self.slider.opacity = 1
            self.slider.disabled = False
            self.cancel_btn.opacity = 1
            self.cancel_btn.disabled = False
            self.btn_color.rgb = (0, 1, 0) # Knop wordt groen voor 'Opslaan'
        else:
            # Bewerkt resultaat opslaan
            self.preview.export_as_image().save("definitieve_foto.png")
            self.reset_ui()

    def update_brightness(self, instance, value):
        # Past de kleur-multiplier aan
        self.preview.color = (value, value, value, 1)

    def reset_ui(self, *args):
        self.preview.opacity = 0
        self.slider.opacity = 0
        self.slider.disabled = True
        self.slider.value = 1
        self.cancel_btn.opacity = 0
        self.cancel_btn.disabled = True
        self.btn_color.rgb = (1, 1, 1) # Knop weer wit
        self.camera.play = True

if __name__ == '__main__':
    CameraApp().run()
