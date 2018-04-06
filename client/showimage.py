#!/usr/local/bin/python3
# refarence from Masato Fujitake 

from PIL import Image
import sys
import os
import math
import argparse

def get_terminal_size():
    terminal_size = os.popen('stty size').read().split()
    return terminal_size

def set_parameter_string(default, lsTrueValue):
    return lsTrueValue if lsTrueValue else default

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ./showimage.py <Image Path>...")
        sys.exit(0) 

    parser = argparse.ArgumentParser(description='Show some image files')
    parser.add_argument(dest='filenames', metavar='filenames', nargs='*')
    parser.add_argument('-s', '--split', dest='splits', action='store', help='Value of display splitting by input images. Type an integer number.')
    parser.add_argument('-p', '--pat', dest='pattern', action='store', help='A displayed mark. The default parameter is a white space.')

    args = parser.parse_args()
    print(args)

try:
    print(args.filenames)
    while 1: 
        for files in args.filenames:
            img = Image.open(files)
            imgW = img.size[0]
            imgH = img.size[1]
            imgh = img.size[1]

            TerminalSize = get_terminal_size()
            terminaly = int(TerminalSize[0])
            terminalx = int(TerminalSize[1])

            img = img.resize((imgW, round(imgH*2/3)))
            splitNum = set_parameter_string('1', args.splits)
            terminalY = round((terminaly - 1)/int(splitNum))
            img.thumbnail((terminalx, terminalY), Image.ANTIALIAS)
            convertedImgW = img.size[0]
            convertedImgH = img.size[1]

            ascii_markNum = '38' if  args.pattern else'48'
            ascii_markString = 'm'+args.pattern[0] if args.pattern else 'm '

            if(img.mode == "RGB" or img.mode == "RGBA"):
                    for y in range(0, convertedImgH):
                        for x in range(0, convertedImgW):
                            offset = y * convertedImgW + x
                            xy = (x, y)
                            rgb = img.getpixel(xy)
                            rgbR = rgb[0]
                            rgbG = rgb[1]
                            rgbB = rgb[2]
                            outline = "\033["+ascii_markNum + ";2;"  + str(rgbR)+";"+str(rgbG) + ";"+str(rgbB) + ascii_markString

                            sys.stdout.write(outline)
                        sys.stdout.write("\033[0m\n")



except:
    print("FINISHED")
