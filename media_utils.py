# -*- coding:utf-8 -*-

"""
@version:
author:changshuai
@time: 2019/12/12
@file: media_utils.py
@function: media related tools
"""
import os
import subprocess


class Media:
    video_ext = ["mp4", "MP4", "webm", "WEBM"]

    @classmethod
    def get_video_files(cls, directory="."):
        videos = []
        pwd = os.path.join(os.getcwd(), directory)
        files = os.listdir(pwd)
        for f in files:
            if f.startswith("._"):  # 特殊情况
                continue
            if f.split(".")[-1] in Media.video_ext:
                videos.append(os.path.join(pwd, f))
        return videos

    @classmethod
    def extract_audio(cls, mp4_file):
        """
        extract audio from video file
        :param mp4_file: video file
        :return: audio file via mp3
        """
        mp3_file = ""
        # rename filename
        if mp4_file.split('.')[-1] in cls.video_ext:
            mp3_file = mp4_file.replace(mp4_file.split('.')[-1], "mp3")

            # command ffmpeg only show error msg
            cmd = "ffmpeg -v error -y -i '" + mp4_file + "' '" + mp3_file + "'"
            print(cmd)
            subprocess.check_call(cmd, shell=True)
        return mp3_file


if __name__ == '__main__':
    videos = Media.get_video_files("./test")
    print(videos)
    for video in videos:
        print(Media.extract_audio(video))
