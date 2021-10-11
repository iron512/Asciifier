#!/usr/bin/python
import sys
import os
import argparse

from PIL import Image

def main():
    parser = argparse.ArgumentParser(description = "A simple image parser, producing the ASCII grayscaled counterpart",formatter_class=argparse.RawTextHelpFormatter, add_help=True)
    parser.add_argument("img", type=str, help="The image to parse")
    parser.add_argument("-c","--columns", type=int, help="The max number of columns to use", default=240)
    parser.add_argument("-f","--format", help="The format to use", default='none', choices=['std', 'reverse_std', 'short', 'reverse_short'])
    parser.add_argument("-v", "--verbose", help="modify output verbosity", action = "store_true")

    #parse the user's input
    args = parser.parse_args()

    verbosity = args.verbose
    columns = args.columns
    rows = -1

    img = Image.open(args.img)
    c, r = img.size

    stdformat = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    if (args.format == "reverse_std"):
        stdformat = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    elif (args.format == "short"):
        stdformat = " .:-=+*#%@"
    elif (args.format == "reverse_short"):
        stdformat = "@%#*+=-:. "

    #reset column and row values
    ratio = int(c/columns+0.99)
    columns = int(c/ratio)
    rows = int(r/ratio/2)

    grayscaled = Image.new(mode="RGB", size=(columns, rows))

    for x in range(columns):
        for y in range(rows):
            tot = 0
            for a in range(ratio):
                for b in range(ratio):
                    r, g, b =  img.getpixel((x*ratio+a,y*2*ratio+b))
                    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
                    tot += gray
            tot = int(tot/(ratio*ratio))
            grayscaled.putpixel((x,y),(tot,tot,tot))
    if verbosity:
    	img.show()
    	grayscaled.show()

    step = 255/len(stdformat)
    for y in range(rows):
        for x in range(columns):
            r, g, b = grayscaled.getpixel((x,y))
            print(stdformat[int(r/step)],end="")
        print()


if __name__ == "__main__":
    main()
