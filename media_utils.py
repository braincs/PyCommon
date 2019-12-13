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

    @classmethod
    def down_sample_video(cls, video_file, factor):
        """
        video down sampling via CRT
        :param video_file: input video
        :param factor: Constant Rate Factor (CRT) between around 18 and 24
        :return: output video path
        """
        res_video = ""
        if video_file.split('.')[-1] in cls.video_ext:
            segments = video_file.split(".")
            segments.insert(-1, "ds")
            res_video = ".".join(segments)
            # ffmpeg -i input.mp4 -vcodec libx264 -crf 20 output.mp4
            cmd = "ffmpeg -v error -y -i '" + video_file + "' -vcodec libx264 -crf " + str(
                factor) + " '" + res_video + "'"
            print(cmd)
            subprocess.check_call(cmd, shell=True)

        return res_video


if __name__ == '__main__':
    videos = Media.get_video_files("./test")
    print(videos)
    for video in videos:
        print(Media.extract_audio(video))
        Media.down_sample_video(video, 18)
