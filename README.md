# Automated Video Generation Tool

This project is an automation tool that generates video content from a text prompt.

The workflow demonstrates a repeatable, programmatic pipeline where:
- A text prompt is converted into a voice narration
- A stock video is automatically fetched
- Outputs are generated without any manual editing

This approach aligns with an MVP-style implementation and can be extended to use AI video generation APIs or other video backends.

## Features
- Accepts a text prompt as input
- Fully automated and repeatable workflow
- Runnable script (no manual steps)
- Generates example video output

## Requirements
- Python 3
- Internet connection

## Setup
Install required dependencies:

```
python -m pip install gtts requests
```


## Usage
Run the script:

```
python generate_video.py
```

## Output
The script generates the following files in the `output/` directory:
- `sample_video.mp4` – example video generated automatically
- `voice.mp3` – narration generated from the text prompt

## Example Prompt
"A calm explanation about the importance of clean energy"

## Notes
The implementation is modular and can be extended to:
- Combine audio and video in a single pipeline
- Swap in AI video generation APIs
- Support different prompt formats
