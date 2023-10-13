import os
import cairosvg

directory = 'resources/'

for input_name in os.listdir (directory):
    if input_name[-3:] == 'svg':
        output_name = input_name[:-3] + 'png'
        cairosvg.svg2png (url=os.path.join (directory, input_name), write_to=os.path.join (directory, output_name))

for file_name in os.listdir (directory):
    if file_name[-3:] == 'svg':
        os.remove (os.path.join (directory, file_name))