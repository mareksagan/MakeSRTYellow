#! /usr/bin/python3

import datetime as dt
import glob
import codecs

def get_subtitles_from_file(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8-sig') as srt_file:
        subtitles = list(srt_file.read().split('\n\n'))
    return subtitles

start_time = dt.datetime.now()
file_list = glob.glob('./*.srt')
print(f'There are {len(file_list)} file(s) to process...')
print()
processed_file_count = 1
for file_name in file_list:
    print(f'Processing file {processed_file_count} from {len(file_list)}. File name: {file_name}')
    
    subtitle = get_subtitles_from_file(file_name)

    with codecs.open(file_name, 'w+', 'utf-8-sig') as new_srt_file:
        for subtitle_line in subtitle:
            line = list(subtitle_line.splitlines())
            for i in range(0, len(line)):
                if i < 2:
                    new_srt_file.write(line[i])
                else:
                    new_srt_file.write("<b><font color=#ffff00>")
                    new_srt_file.write(line[i])
                    new_srt_file.write("</font></b>")
                new_srt_file.write('\n')
            new_srt_file.write('\n')
    processed_file_count += 1

end_time = dt.datetime.now()
print()
print(f'Processed in: {(end_time - start_time)}')
