# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:12:13 2021

@author: enzoa
"""
import requests


URL = "http://127.0.0.1/predict" # local host
TEST_AUDIO_FILE_PATH = "speech_commands_v0.01/bed/0b56bcfe_nohash_0.wav"


if __name__ == "__main__":
    
    audio_file = open(TEST_AUDIO_FILE_PATH, "rb")
    values = {"file": (TEST_AUDIO_FILE_PATH, audio_file, "audio/wav")}
    response = requests.post(URL, files=values)
    data = response.json()
    
    print(f"Predicted keyword is: {data['keyword']}")