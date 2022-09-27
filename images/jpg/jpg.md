# JPEG

The most widely used digital image format, developed by Joint Photographic Experts Group. Several attempts has been made to replace it with something "better" (JPEG 2000 included), but it helds it's position. ISO/IEC and ITU-T standard, which only specifies the codec, but not the file format - the Exif and JFIF standards define the commonly used ones.

# File format

A sequence of segments, each beginning with a marker. A marker is 2 bytes long, the first byte is 0xFF, the other byte indicates the type of the marker.

Examples:
- `FF D8` - SOI: start of image
- `FF D9` - EOI: end of image
- `FF C0` - SOF: start of frame (baseline DCT)
- `FF C2` - SOF (progressive DCT)
- `FF C4` - DHT: define Huffman tables
- `FF DB` - DQT: define quantization tables
- `FF DA` - SOS: start of scan (generally 1 for baseline, and multiple for progressive images)
- `FF E?` - APP? specific data (APP0 is JFIF and APP1 is Exif for example)
- `FF FE` - COMment

APP markers often begin with a standard or vendor name, like `JFIF\0` for JFIF. (Several vendors might use the same APPn marker type, they are not standardised.)
ICC profiles and such can be attached too.

## JPEG encoding

A JPEG file can be encoded in various ways, most commonly it is done with JFIF encoding:

1. Image colors are converted from RGB to YCbCr.
2. The resolution of chroma data is reduced - the human eye is less sensitive to color than brightness.
3. The image is split into 8x8 pixel blocks, each channel undergoes DCT.
4. The amplitudes of the frequency components are *quantized*. Human vision is more sensitive to small variations in color/brightness over large areas - the magnitude of the high-frequency components is reduced. (This is the quality setting of the JPEG, at very low quality high frequencies are discarded completely.)
5. The result is compressed with a variant of Huffman encoding (lossless).

## YCbCr

RGB: red, green, blue
YCbCr:
- Y: luma/luminescense - brightness (Y' is used for JPEG, which is gamma corrected Y)
- Cb: blue chroma - yellow-blue axis
- Cr: red chroma - green-red axis

## Downsampling

...

## Block splitting

...

## DCT

Discrete Cosine Transform (~DFT, but only using **real** numbers)

## Quantization

...

## Entropy coding

...


### Links

- [JPEG Sandbox](https://jpeg-sandbox.glitch.me/)
- [JPEG Sandbox on github](https://github.com/OmarShehata/jpeg-sandbox)
- [Interactive Fourier](https://www.jezzamon.com/fourier/)
- [Unraveling the JPEG](https://parametric.press/issue-01/unraveling-the-jpeg/)
