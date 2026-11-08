import asyncio
import edge_tts
from pydub import AudioSegment
from pydub.effects import high_pass_filter, low_pass_filter

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

def radio_filter(voice):
    """Make the voice sound like an old loudspeaker."""
    try:
        voice = high_pass_filter(voice, 300) # everything under 300 Hz gone
        voice = low_pass_filter(voice, 3000) # everything above 3000 Hz gone
        return voice
    except Exception:
        return voice # Fallback: unfiltered voice

def build_broadcast(voice_path="warning.mp3", output_path="broadcast.mp3"):
    """Put the alarm tone before and after the voice."""
    tone = AudioSegment.from_file("assets/alarm.wav")
    voice = AudioSegment.from_file(voice_path)

    final = tone + radio_filter(voice) + tone
    final.export(output_path, format="mp3")

    return output_path