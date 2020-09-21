from gtts import gTTS
from io import BytesIO
from pygame import mixer

def speak(message):
    # Use gTTS to Store Speech on Buffer
    tts = gTTS(text=message, lang='en-us')
    mp3 = BytesIO()
    tts.write_to_fp(mp3)
    mp3.seek(0)

    # Play from Buffer
    mixer.init()
    mixer.music.load(mp3)
    mixer.music.play()
