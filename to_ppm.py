# -- IMPORTS --
from math import floor,sqrt
import sys

# -- GLOBAL VARIABLES
max_height = -1
input_path = ""
pixel_count = 0
pixels = []
pixel = ""

# -- FUNCTIONS --
def show_help():
  print("!!!  Define help !!!")

# -- MAIN --
print(len(sys.argv), sys.argv) #DEBUG

# Handling command line arguments
if (len(sys.argv) == 1):
  print("Please give a file to turn into an image")
  quit()

if "--help" in sys.argv:
  show_help()
  quit()

if (len(sys.argv) >= 2):
  input_path = sys.argv[1]

if (len(sys.argv) >= 3):
  max_height = int(sys.argv[2])

# Reading input file
with open(input_path, mode="rb") as fin:
  read_data = fin.read()
  fin.close()

byte_list = list(map(int.to_bytes, read_data))

# Computing original file bytes to PPM pixels
for i in range(len(byte_list)):
  if (i % 3 == 0):
    pixel = f"{int.from_bytes(byte_list[i])}"
  else:
    pixel = f"{pixel} {int.from_bytes(byte_list[i])}"
  if (i % 3 == 2):
    pixels.append(pixel)
    pixel = ""
    pixel_count += 1

# Computing output image height
if (max_height > 0):
  height = min(floor(sqrt(pixel_count)), max_height)
else:
  height = floor(sqrt(pixel_count))

# Generating output file
with open("output.ppm", mode="w") as fout:
  fout.write("P3\n")
  fout.write(f"{height} {height}\n")
  fout.write("255 \n\n")
  for i in range(height * height):
    fout.write(f"{pixels[i]}\n")

  fout.close()

print("output.ppm file generated")