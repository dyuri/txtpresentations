# Portable Network Graphics

One of the most widely used raster image formats, that supports lossless compression, alpha transparency and is supported by all the webbrowsers. It was developed as an improved, non-patented replacement for GIF (*"PNG's not GIF"*).

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

[13 bytes total]

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




