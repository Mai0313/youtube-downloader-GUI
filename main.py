from pytube import YouTube
from ytmusicapi import YTMusic
import os
import json

class YouTubeDownloader:
    def __init__(self, output_path):
        os.makedirs(output_path, exist_ok=True)
        self.output_path = output_path

    def get_video(self, url: str, res: str):
        """Download a video from YouTube at a specified resolution.

        Args:
            url (str): The URL of the video to download.
            res (str): The resolution of the video to download. e.g. "720p", "480p", "360p", "240p", "144p"
            outpath (str): The path to save the video to.

        Returns:
            None
        """
        yt = YouTube(url)
        yt.streams.filter(file_extension="mp4").get_by_resolution(res).download(self.output_path, skip_existing = True)

    def get_highest_res_video(self, url: str):
        """Download the highest resolution video from YouTube.
        
        Args:
            url (str): The URL of the video to download.
        
        Returns:
            None
        """
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(self.output_path)

def get_vid_link(video_names: str, filter_type: str = "songs"):
    """Get the video link from YouTube

    Args:
        video_names (str): The name of the video to search for.
        filter_type (str): The type of search to perform. e.g. albums, artists, playlists, community_playlists, featured_playlists, songs, videos, profiles

    Returns:
        str: The link to the video.
    """
    ytmusic = YTMusic()
    result = ytmusic.search(query = video_names, filter = filter_type)
    result = result[0].get("videoId")
    result = f"https://www.youtube.com/watch?v={result}"
    return result

def main(target):
    yt = YouTubeDownloader("downloads")
    if "https:" in target and "youtu" in target:
        yt.get_highest_res_video(target)
    else:
        target = get_vid_link(target)
        print(f"Downloading from {target}...")
        yt.get_highest_res_video(target)

if __name__ == "__main__":
    YouTubeDownloader("downloads").get_video("https://www.youtube.com/watch?v=l4C4Ucwtqe0&ab_channel=%E5%9A%BC%E8%B1%86", "720p")
