#!/usr/bin/env python

import struct
import zlib

from typing import List, Tuple

DEBUG = True

f = open('example_rgb.png', 'rb')

# check the header
png_signature = b'\x89PNG\r\n\x1a\n'

if f.read(8) != png_signature:
    print('Not a valid PNG file')
    exit()


def log(msg):
    if DEBUG:
        print(msg)


def read_chunk(f):
    # read the length of the chunk
    length = struct.unpack('>I', f.read(4))[0]
    # read the chunk type
    chunk_type = f.read(4)
    # read the chunk data
    chunk_data = f.read(length)
    # read the chunk CRC
    chunk_crc = struct.unpack('>I', f.read(4))[0]

    # check the CRC
    if chunk_crc != zlib.crc32(chunk_type + chunk_data):
        print('CRC error')
        exit()

    return chunk_type, chunk_data


def rgbcolor(r, g, b):
    return f'\x1b[38;2;{r};{g};{b}m█\x1b[0m'


def display_image(img):
    for y in range(len(img)):
        for x in range(len(img[y])):
            print(rgbcolor(*img[y][x]), end='')
        print()


chunks: List[Tuple] = []
image: List[List[Tuple]] = []

width = 0
height = 0

while True:
    chunk_type, chunk_data = read_chunk(f)
    chunks.append((chunk_type, chunk_data))

    if chunk_type == b'IHDR':
        width = struct.unpack('>I', chunk_data[0:4])[0]
        height = struct.unpack('>I', chunk_data[4:8])[0]
        width, height, bitd, colort, compm, filterm, interlacem = struct.unpack('>IIBBBBB', chunk_data)
        log(f'width = {width}, height = {height}, bitd = {bitd}, colort = {colort}, compm = {compm}, filterm = {filterm}, interlacem = {interlacem}')

        if compm != 0 or filterm != 0 or interlacem != 0 or colort != 2 or bitd != 8:
            print('We only support 8-bit rgb non-interlaced images')
            exit()

        for i in range(height):
            image.append([])
            for j in range(width):
                image[i].append((0, 0, 0))

    if chunk_type == b'IDAT':
        # decompress the data
        data = zlib.decompress(chunk_data)
        log(f'data length = {len(data)}')

        # split the data into rows, row: [filter_type, [r, g, b]*width]
        rows = [data[i:i+1+width*3] for i in range(0, len(data), 1+width*3)]
        log(f'rows length = {len(rows)}')

        for y, r in enumerate(rows):
            filter_type = r[0]
            # TODO filter restoration
            pixels = [r[i:i+3] for i in range(1, len(r), 3)]
            for x, pixel in enumerate(pixels):
                image[y][x] = (int(pixel[0]), int(pixel[1]), int(pixel[2]))

    if chunk_type == b'IEND':
        break

for chunk in chunks:
    log(chunk[0])

display_image(image)
