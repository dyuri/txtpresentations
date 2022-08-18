#!/usr/bin/env python

import struct
import zlib
import os
import sys

from typing import List, Tuple

DEBUG = os.environ.get('PNGDEBUG', False)


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


def rgbcolor(r, g, b, r2, g2, b2):
    return f'\x1b[38;2;{r};{g};{b}m\x1b[48;2;{r2};{g2};{b2}m▀\x1b[0m'


def display_image(img):
    for y in range(0, len(img), 2):
        for x in range(len(img[y])):
            c1 = img[y][x]
            if len(img) > y:
                c2 = img[y+1][x]
            else:
                c2 = (0, 0, 0)
            print(rgbcolor(*c1, *c2), end='')
        print()


def paeth(x, fa, fb, fc):
    a = (x + fa) % 256
    b = (x + fb) % 256
    c = (x + fc) % 256
    p = (a + b - c) % 256
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    elif pb <= pc:
        return b
    else:
        return c


FILTERS = {
    0: lambda x, a, b, c: x,
    1: lambda x, a, b, c: (x + a) % 256,
    2: lambda x, a, b, c: (x + b) % 256,
    3: lambda x, a, b, c: ((x + a) % 256 + (x + b) % 256) // 2,
    4: lambda x, a, b, c: paeth(x, a, b, c),
}


def restore_filters(ft, bpp, r, lr):
    # TODO bpp
    lrs = [0 for _ in range(bpp)] + lr[:-bpp]
    row = []

    rpx = zip(*(r[i::bpp] for i in range(bpp)))
    lrpx = zip(*(lr[i::bpp] for i in range(bpp)))
    lrspx = zip(*(lrs[i::bpp] for i in range(bpp)))

    for x, b, c in zip(rpx, lrpx, lrspx):
        a = [0 for _ in range(bpp)]
        if len(row) > 0:
            a = row[-bpp:]

        # log(f'{x} {a} {b} {c}')
        for pxc in range(bpp):
            row.append(FILTERS[ft](x[pxc], a[pxc], b[pxc], c[pxc]))

    return row


filename = 'example_rgb.png'

if sys.argv[1:]:
    filename = sys.argv[1]

# read the file
f = open(filename, 'rb')

# check the header
png_signature = b'\x89PNG\r\n\x1a\n'

if f.read(8) != png_signature:
    print('Not a valid PNG file')
    exit()

chunks: List[Tuple] = []
image: List[List[Tuple]] = []

width = 0
height = 0
bpp = 0  # bytes per pixel

while True:
    chunk_type, chunk_data = read_chunk(f)
    chunks.append((chunk_type, chunk_data))

    if chunk_type == b'IHDR':
        width = struct.unpack('>I', chunk_data[0:4])[0]
        height = struct.unpack('>I', chunk_data[4:8])[0]
        width, height, bitd, colort, compm, filterm, interlacem = struct.unpack('>IIBBBBB', chunk_data)
        if colort == 2:
            bpp = 3  # RGB
        elif colort == 6:
            bpp = 4

        log(f'width = {width}, height = {height}, bitd = {bitd}, colort = {colort}, compm = {compm}, filterm = {filterm}, interlacem = {interlacem}')

        if compm != 0 or filterm != 0 or interlacem != 0 or bpp == 0 or bitd != 8:
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
        rows = [data[i:i+1+width*bpp] for i in range(0, len(data), 1+width*bpp)]
        log(f'rows length = {len(rows)}')

        last_row = [0 for _ in range(width*bpp)]
        for y, r in enumerate(rows):
            filter_type = r[0]

            row = restore_filters(filter_type, bpp, r[1:], last_row)
            last_row = row

            pixels = [row[i:i+bpp] for i in range(0, len(row), bpp)]
            for x, pixel in enumerate(pixels):
                image[y][x] = (int(pixel[0]), int(pixel[1]), int(pixel[2]))  # alpha ignored

    if chunk_type == b'IEND':
        break

for chunk in chunks:
    log(chunk[0])

display_image(image)
