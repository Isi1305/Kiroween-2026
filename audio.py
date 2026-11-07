import asyncio
import edge_tts
from pydub import AudioSegment

# Voice settings for the TTS
async def make_speech(text, filename="warning.mp3"):
    communicate = edge_tts.Communicate(
        text,
        voice="en-US-ChristopherNeural",
        rate="-10%",
        pitch="-10Hz",
        volume="+0%"
    )
    await communicate.save(filename)

tone = AudioSegment.from_file("assets/alarm.wav")
voice = AudioSegment.from_file("warning.mp3")

final = tone + voice + tone
final.export("test_final.mp3", format="mp3")