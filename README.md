# QR Generator

A simple Python project that generates QR code images from a URL or text.

## Features

- Generates QR codes using the `qrcode` library
- Saves QR code output as a PNG image
- Easy to customize the text or URL

## Requirements

- Python 3.8+
- `qrcode` package
- `Pillow` image library

## Install

```bash
pip install qrcode[pil]
```

If needed, install Pillow separately:

```bash
pip install pillow
```

## Usage

Edit `main.py` to set the URL or text you want to encode, then run:

```bash
python main.py
```

The QR code image will be saved as `Github_profile.png` by default.

## Example

```python
import qrcode

img = qrcode.make("https://github.com/Shreyaaaaaak")
img.save("Github_profile.png")
```

## Notes

- If you use `qrcode.QRCode(...)`, call `add_data(...)` and `make_image(...)` correctly.
- Make sure the package is installed in the same Python environment used to run the script.
