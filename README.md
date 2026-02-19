# Anything to ppm

I love data visualization so I made a small python script to encode any file's bytes to a Portable Pixmap (PPM) image. Why PPM ? It's very easy to make and I don't really have time to dig in the specifications of other image formats for now.

## Usage
Use from terminal
```bash
python to_ppm.py <input_file_path> [max_height]
```
This will generate a `output.ppm` image file containing the data from the inputed file as an image