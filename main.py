from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from scan_qr import scan_qr_code
from paired_device import save_device, load_device

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.device_info = load_device()

        self.text_input = TextInput(hint_text='Type here...', multiline=True)
        self.add_widget(self.text_input)

        self.send_btn = Button(text='Send to Laptop')
        self.send_btn.bind(on_press=self.send_text)
        self.add_widget(self.send_btn)

        self.qr_btn = Button(text='Scan QR to Pair')
        self.qr_btn.bind(on_press=self.pair_device)
        self.add_widget(self.qr_btn)

    def send_text(self, instance):
        if self.device_info:
            print(f"Sending to {self.device_info}: {self.text_input.text}")
            # ఇక్కడ socket.send() లాజిక్ చేర్చాలి
        else:
            print("No device paired yet.")

    def pair_device(self, instance):
        device = scan_qr_code()
        if device:
            save_device(device)
            self.device_info = device
            print("Device paired successfully.")

class RemoteTypingApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    RemoteTypingApp().run()
