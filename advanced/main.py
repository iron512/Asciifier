#!/usr/bin/python
import sys
import argparse
import os

import cv2
import numpy as np

def asciifize(img, columns, rows, stdformat):

    step = 255/len(stdformat)

    os.system("clear")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, [columns, rows])

    #cv2.imshow("frame",resized)

    toPrint = ""
    for i in range(rows):
        for j in range(columns):
            toPrint += stdformat[int((resized[i,j]-1)/step)]
        toPrint += "\n"

    print(toPrint)

def main():
    parser = argparse.ArgumentParser(description = "A simple video parser, producing the ASCII grayscaled counterpart",formatter_class=argparse.RawTextHelpFormatter, add_help=True)
    parser.add_argument("-i","--input_video", type=str, help="The video to parse", default='none')
    parser.add_argument("-c","--columns", type=int, help="The max number of columns to use", default=240)
    parser.add_argument("-f","--format", help="The format to use", default='std', choices=['std', 'reverse_std', 'short', 'reverse_short'])

    #parse the user's input
    args = parser.parse_args()

    columns = args.columns
    rows = -1

    cap = cv2.VideoCapture(0)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    if args.input_video != "none":
        cap = cv2.VideoCapture(args.input_video)
        fps = int(cap.get(cv2.CAP_PROP_FPS))


    if (cap.isOpened()== False):
        print("Error opening video stream or file")
        sys.exit(1)

    stdformat = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    if (args.format == "reverse_std"):
        stdformat = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    elif (args.format == "short"):
        stdformat = " .:-=+*#%@"
    elif (args.format == "reverse_short"):
        stdformat = "@%#*+=-:. "

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    ratio = int(width/columns+0.99)
    columns = int(width/ratio)
    rows = int(height/ratio/2)

    while True:
        ret, img = cap.read()
        if ret:
            img = cv2.flip(img,1)

            cv2.imshow("Video", img)

            asciifize(img, columns, rows, stdformat)
            print(fps)

            if cv2.waitKey(int((1/int(fps))*1000)) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
if __name__ == "__main__":
    main()
