#coding:utf-8
import global_list
import os


def Change_fileType(Filename):
    destFileName=Filename[:-3]+'pcm'
    print destFileName 
    os.system('ffmpeg -y  -i '+Filename+'  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 '+destFileName)
    os.system('rm -rf '+Filename)
    return destFileName
    