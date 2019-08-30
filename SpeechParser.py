
class SpeechParser:
    
    def __init__(self):
        self.dict = []
    
    def parse(self, string):
        if "goodbye" in string:
            return None
    
    def wake(self, speech, bot):
        if speech is not None:
            print(speech)
            if "wake up eris" in speech:
                bot.converse()
