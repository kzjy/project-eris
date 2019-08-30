import pyttsx3

class Speaker: 

    def __init__(self):
        self.engine = pyttsx3.init()
        self.setup_voice()
    
    def setup_voice(self, voice=1):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
    
    def say(self, content):
        self.engine.say(content)
        self.engine.runAndWait()
    
    def stop(self):
        self.engine.stop()

