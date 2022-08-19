# Portable Network Graphics

One of the most widely used raster image formats, that supports lossless compression, alpha transparency and is supported by all the webbrowsers. It was developed in 1996 as an improved, non-patented replacement for GIF (*"PNG's not GIF"*). ISO and IETF standard.

Features:

- wide range of pixel format (indexed/palette, grayscale, rgb, gs+alpha, rgb+alpha)

- full scale of alpha transparency (from single pixel to full 16-bit alpha channel)

- 2 stage compression: filtering + DEFLATE
  
  - Filtering: prediction based on previous pixel colors, to improve compression
  
  - DEFLATE: LZ77 + Huffman coding, implementations widely available (*zlib* for example)

- 2 dimensional, 7-pass interlacing (allows to render the image with a lower resolution much earlier during the transfer, but usually reduces the compressibility)

- extendibility - "forward compatibility", custom chunks can be implemented and used
  
  - for example APNG (animated PNG) - which is also supported by all major browser - is an unofficial extension of PNG, even PNG decoders that does not know anything about APNG will display the first frame without any error

## File structure

Header + chunks

### Header

8 byte signature:

`89 50 4E 47 0D 0A 1A 0A`

- `89`- something above 128 for easy binary content detection

- `50 4E 47`- `PNG`

- `0D 0A`- DOS line ending (CRLF, `\r\n`)

- `1A`- DOS EOF (Ctrl+Z)

- `0A`- UNIX line ending (LF, `\n`)

### Chunks

After the header comes a series af chunks:

`[length 4bytes][type 4bytes][data <length>bytes][crc 4bytes]`

#### Chunk type

4 bytes (characters in this case), case sensitive, character cases has special meaning:

1. critical (upper) or not (lower) - ancillary chunks can be ignored during decoding

2. public (upper) or private (lower) - ensures that public (standardized) and private (custom) chunks never conflict (two private might)

3. should be uppercase (reserved for future expansion)

4. safe to copy - not safe (upper) / safe (lower) - whether is it safe to copy this chunk if the image is heavily modified

**Some critical chunks**

`IHDR`

- "image header"

- 4 byte width

- 4 byte height

- bit depth (1 byte, 1/2/4/8/16) - number of bits per sample or per palette index (not per pixel)

- color type (1 byte - bitmask, 0, 2, 3, 4, 6)

- compression method (1 byte, always 0)

- filter method (1 byte, always 0)

- interlace method (1 byte, 0 - no interlace, 1 - Adam7 interlace)

- 13 bytes total

`IEND`

- end of image, last chunk

- empty, 0 byte length

`PLTE`

- palette, required for indexed images

`IDAT`

- the actual image data

- might be split into multiple `IDAT` chunks (for streaming i.e.)

**Some ancillary chunks**

`bKGD` - default background color (for transparent images)

`cHRM` - chromaticity (color primaries and white point) ~ _white balance_

`dSIG` - digital signature

`eXIf` - exif metadata

`gAMA` - gamma (multiplied by 100000, integer)

`iCCP` - ICC profile

`tEXt` - key / text (basically anything)

`pHYs` - physical pixel size

`tIME` - last time the image was changed

...

### Pixel format

`IHDR` bit depth + color type

**Bit depth**

- Indexed: 1, 2, 4, 8 bit per pixel (2, 4, 16, 256 colors)

- Grayscale: 1, 2, 4, 8, 16 bpp

- Gs+alpha: 16 or 32 bpp

- Truecolor: 24 or 48 bpp

- Truecolor+alpha: 32 or 64 bpp

**Color type**

Bitmask:

- bit value 1: indexed (palette)

- bit value 2: rgb (or trichromatic), grayscale (relative luminance) otherwise

- bit value 4: alpha channel (per pixel)

Possible values:

- 0: grayscale

- 2: rgb/truecolor

- 3: indexed (colors in palette can have alpha transparency, individual pixels don't)

- 4: grayscale + alpha

- 6: rgb+alpha

### Compression

lossless, 2 stage:

- filtering (~prediction)

- DEFLATE - LZ77 + Huffman coding

#### Filtering

One filter *method* for the entire image (well, currently there's only one in the standard, '0'), and one filter *type* per line.

The filter *predicts* the value of each pixel based on previous pixels, and substracts the predicted color from the actual value. In many cases this results in a more compressible line.

**Filter types**

(type - name - predicted value)

- 0 - *None* - zero (no prediction)

- 1 - *Sub* - pixel to the left

- 2 - *Up* - pixel above

- 3 - *Average* - mean of left + above pixel (rounded down)

- 4 - *Paeth* - (left), (above), or (left-above), whichever is closest to *p = (left) + (above) - (left-above)*

### Interlacing

Optional, 2 dimensional, 7 pass scheme (Adam7).

8x8 blocks:

```
1 6 4 6 2 6 4 6
7 7 7 7 7 7 7 7
5 6 5 6 5 6 5 6
7 7 7 7 7 7 7 7
3 6 4 6 3 6 4 6
7 7 7 7 7 7 7 7
5 6 5 6 5 6 5 6
7 7 7 7 7 7 7 7
```

![](https://upload.wikimedia.org/wikipedia/commons/2/27/Adam7_passes.gif)

Reduces data compressibility - filtering uses neighbour pixels for prediction, with interlacing this isn't that much effective.

### Animation

Many "extension" that adds animation to PNG, the most widely supported one is **APNG** (which is not "standardised" by the PNG Group, but still), all major browsers and operating systems support it.

Backward compatible:

- `acTL` chunk for generic animation data (frame number, loop count)

- one `IDAT` chunk - "normal" PNG decoders will display a still image

- multiple `fcTL` and `fdAT` chunks for further frames (metadata + data)


