#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import datetime
import sys
import os

root_path = sys.path[0]
# print(root_path)
types = ['.mp4', '.avi', '.wmv', '.mkv', '.flv', '.mov']


def is_video_file_extension(file_name):
    array = map(file_name.lower().endswith, types)
    if True in array:
        # print("True")
        return True
    else:
        # print("False")
        return False


def create_thumb(file_full_path, fail_thumb_dir):
    public = "ffmpeg -i '{}' -y -f mjpeg -ss 3 -t 0.001 -s ".format(file_full_path)
    thumb_video = public + '1280x720 {}/SYNOVIDEO_VIDEO_SCREENSHOT.jpg'.format(fail_thumb_dir)
    os.system(thumb_video)


def main():
    msg = "Sorry, the code was not executed due to unknown reasons."
    try:
        for file_path, dir_son_dirs_name, dir_son_files_name in os.walk(root_path):
            # print(file_path, dir_son_dirs_name, dir_son_files_name)
            for file_name in dir_son_files_name:
                if is_video_file_extension(file_name):
                    file_full_path = os.path.join(file_path, file_name)
                    fail_thumb_dir = file_path + "/@eaDir/" + file_name
                    # print(file_full_path, fail_thumb_dir)
                    thumb_video = fail_thumb_dir + '/SYNOVIDEO_VIDEO_SCREENSHOT.jpg'
                    if not os.path.exists(thumb_video):
                        create_thumb(file_full_path, fail_thumb_dir)
    except Exception as e:
        msg = "{} Failed! Error: {} \n".format(datetime.datetime.now(), e)
    else:
        msg = "{} Succeeded! \n".format(datetime.datetime.now())
    finally:
        with open("{}/Thumb_for_videostation_log.txt".format(root_path), mode='a', encoding='utf-8') as f:
            f.write(msg)
            f.close()


main()
