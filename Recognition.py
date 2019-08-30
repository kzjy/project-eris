import speech_recognition as sr

class VoiceRecognizer: 

    def __init__(self):
        self.r = sr.Recognizer()
        self.set_energy_threshold()
    
    def set_energy_threshold(self, auto=False):
        """
        Set energy threshold for microphone
        """
        if auto:
            with sr.Microphone() as source:
                self.r.adjust_for_ambient_noise(source)
        else:
            self.r.dynamic_energy_threshold = False
            self.r.energy_threshold = 2000

    def listen(self, callback):
        """
        Start listening for commands 
        """
        mic = sr.Microphone()
        stop_listening = self.r.listen_in_background(mic, callback)
    
