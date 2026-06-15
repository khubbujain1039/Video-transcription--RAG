import os

os.environ["PATH"] += (
    os.pathsep
    + r"C:\Users\Khushboo Jain\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin"
)

import whisper


def transcribe_video(
    video_path
):

    model = whisper.load_model(
        "base"
    )

    result = model.transcribe(
        video_path
    )

    return result