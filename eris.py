import speech_recognition as sr
from Recognition import VoiceRecognizer as recognizer 
from Speech import Speaker as speaker
from SpeechParser import SpeechParser as parser
from Common import *
import sys, time, os

class Eris: 

    def __init__(self, speaker, parser, recognizer):

        # Interaction components 
        self.speaker = speaker
        self.recognizer = recognizer
        self.parser = parser

        # Conversation records
        self.records = Record()

        # mode can be one of ["standby", "converse", "terminate"]
        self.mode = "standby"

    def start(self):
        """
        Start up Eris
        """
        self.speaker.say("Hello Kelvin")
        self.recognizer.listen(self.new_phrase)
        
        # infinite loop waiting for activity 
        last_spoken = self.records.get_most_recent_item()
        while self.mode is not "terminate":

            # check for new speech input
            if self.records.get_most_recent_item() is not None and last_spoken != self.records.get_most_recent_item():
                self.switch_mode("converse")
                # Start conversation with timeout of 10 seconds of inactivity
                last_spoken = self.records.get_most_recent_item()
                self.converse(last_spoken)

            # sleep to reduce cpu usage
            time.sleep(1)
            continue

    def converse(self, last_spoken, timeout=10):
        """
        Go into conversation mode to take in and execute commands
        """
        while (time.time() - last_spoken[1]) < timeout:
            # New activity
            if last_spoken != self.records.get_most_recent_item():
                # update last spoken
                last_spoken = self.records.get_most_recent_item()
                # TODO do the command
                self.speaker.say(last_spoken[0])
            
            time.sleep(1)
        
        # timeout after 10 seconds, changing to standby
        self.switch_mode("standby")
        print('standby')

    def new_phrase(self, recognizer, audio):
        """
        Callback function when new phrase is detected
        """
        try:
            print('detected')
            # Push speech input to conversation record
            text = recognizer.recognize_google(audio)
            print(text)
            self.records.push((text, time.time()))

        except sr.UnknownValueError: 
            print('Could not understand audio')
        except sr.RequestError: 
            print('Could not request result from API')
    
    def switch_mode(self, mode):
        """
        Switch current mode, wipe previous conversation record if going on standby
        """
        if mode == "standby":
            self.records.empty()
        self.mode = mode
        
    def terminate(self):
        self.speaker.say("Goodbye Kelvin")
        sys.exit()

if __name__ == "__main__":
    parser, speaker, recognizer = parser(), speaker(), recognizer()
    eris = Eris(speaker, parser, recognizer)
    eris.start()