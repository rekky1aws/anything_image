# Anything to ppm

I love data visualization so I made a small python script to encode any file's bytes to a Portable Pixmap (PPM) image. Why PPM ? It's very easy to make and I don't really have time to dig in the specifications of other image formats for now.

## Usage
Use from terminal
```bash
python to_ppm.py <input_file_path> [max_height]
```
This will generate a `output.ppm` image file containing the data from the inputed file as an image

## Issues
At the moment, even in full size (generating a file without specifying a max_height) it cannot be used to revert to the original as I truncate the original bytes to have a square image. The data loss chance grows with the size of the input file (but if the input file has a size of a perfect square in bytes, it might be possible in theory)

## Examples
This is the image generated using the script itself as input file :
![Image generated with the script](/assets/img/generation_examples/script.ppm)

This one was generated using this README file :
![Image generated with the README file](/assets/img/generation_examples/readme.ppm)