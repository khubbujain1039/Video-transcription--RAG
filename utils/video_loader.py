import os
import yt_dlp


def download_video(url):

    os.makedirs(
        "downloads",
        exist_ok=True
    )

    output_template = (
        "downloads/video.%(ext)s"
    )

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "quiet": True,
        "noplaylist": True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        ydl.download([url])

    for file in os.listdir(
        "downloads"
    ):

        if file.startswith(
            "video"
        ):

            return os.path.join(
                "downloads",
                file
            )

    raise Exception(
        "Downloaded file not found."
    )