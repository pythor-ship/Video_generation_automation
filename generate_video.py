from gtts import gTTS
import requests
import os

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Text prompt input
prompt = "A calm explanation about the importance of clean energy"

# Convert text to voice
tts = gTTS(text=prompt, lang="en")
tts.save("output/voice.mp3")

# Download stock video
video_url = "https://filesamples.com/samples/video/mp4/sample_640x360.mp4"
video_data = requests.get(video_url).content

with open("output/sample_video.mp4", "wb") as f:
    f.write(video_data)

print("Automation complete. Video and voice generated.")
