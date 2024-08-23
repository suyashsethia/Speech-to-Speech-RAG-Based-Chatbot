import os
import io
import wave
import pyaudio
import keyboard
from google.cloud import speech
from google.cloud import texttospeech

# Set the environment variable to the path of your service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "animated-spirit-433009-p5-773b7d3034a1.json"

def text_to_speech(text, output_audio_file):
    """Convert text to speech using Google Text-to-Speech API and save to an audio file."""
    
    # Initialize the client with service account credentials
    client = texttospeech.TextToSpeechClient()

    # Define the request payload
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Journey-F"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        effects_profile_id=["small-bluetooth-speaker-class-device"],
        pitch=0,
        speaking_rate=0.6
    )

    # Send the request to the Google Text-to-Speech API
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Write audio content to file
    with open(output_audio_file, "wb") as out:
        out.write(response.audio_content)
    print(f"Audio content written to file: {output_audio_file}")

def live_speech_to_text():
    """Capture live audio from the microphone and transcribe it to text using Google Speech-to-Text API."""
    client = speech.SpeechClient()

    audio = pyaudio.PyAudio()
    print("Press SPACE to start recording. Press SPACE again to stop.")

    stream = audio.open(
        rate=16000,
        format=pyaudio.paInt16,
        channels=1,
        input=True,
        frames_per_buffer=1024
    )

    frames = []
    recording = False

    while True:
        if keyboard.is_pressed('space'):
            if not recording:
                print("Recording started.")
                recording = True
                frames = []
                while keyboard.is_pressed('space'):  # Wait until space is released
                    pass
            else:
                print("Recording stopped.")
                recording = False
                break

        if recording:
            data = stream.read(1024)
            frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open("live_audio.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(16000)
        wf.writeframes(b"".join(frames))

    with io.open("live_audio.wav", "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

def test_text_to_speech():
    """Test the text-to-speech function with sample text."""
    text = "Hello there, I would like to welcome you to the world of Flipkart. Umm, what would you like to know about us?"
    output_audio_file = "test_audio.wav"
    text_to_speech(text, output_audio_file)
    print(f"Testing complete. Check the file: {output_audio_file}")

def test_live_speech_to_text():
    """Test the live speech-to-text function."""
    print("Testing live speech-to-text. Press SPACE to start and stop recording...")
    live_speech_to_text()
    print("Testing complete.")

if __name__ == "__main__":
    # Run tests
    test_text_to_speech()
    test_live_speech_to_text()
  