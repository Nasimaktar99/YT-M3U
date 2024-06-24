#!/usr/bin/python3

import requests
import os
import sys
import time

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url, ch_name, grp_title, tvg_logo, tvg_id, output_file, session):
    response = session.get(url, timeout=15).text
    if '.m3u8' not in response:
        response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/Nasimaktar99/YT-M3U/main/assets/info.m3u8')
                return
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/Nasimaktar99/YT-M3U/main/assets/info.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    streams = session.get(link[start:end]).text.split('#EXT')
    hd = streams[-1].strip()
    st = hd.find('http')
    m3u8_url = hd[st:].strip()
    
    with open(output_file, 'a') as file:
        file.write(f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{ch_name}" group-title="{grp_title}" tvg-logo="{tvg_logo}",{ch_name}\n')
        file.write(f'{m3u8_url}\n')

def main():
    output_file = "../YouTube_Live.m3u"
    with open(output_file, 'w') as file:
        file.write("#EXTM3U\n\n")
    
    session = requests.Session()
    with open('../YouTube_Live.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Skip the first two lines
    channels = lines[2:]
    
    for i in range(0, len(channels), 2):
        channel_info = channels[i].strip().split('|')
        youtube_url = channels[i + 1].strip()
        
        if len(channel_info) == 4:
            ch_name, grp_title, tvg_logo, tvg_id = channel_info
            grab(youtube_url, ch_name, grp_title, tvg_logo, tvg_id, output_file, session)
    
    if 'temp.txt' in os.listdir():
        os.system('rm temp.txt')
        os.system('rm watch*')

if __name__ == "__main__":
    while True:
        main()
        time.sleep(3 * 3600)  # Sleep for 3 hours before updating again
