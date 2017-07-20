# Image Resizer

A script that allows you to easily resize your images.

You can set the new size for your images in pixels or specify a factor by which you want to multiply the length of each side of the image.

For example, an image 1200x900 after the command

```python image_resize.py  path/to/image.jpg --scale 2```

will save the bigger counterpart of the size 2400x1800 in `path/to/image__2400x1800.jpg` file.

You can specify only the width or only the height of the resulting image. Given one, the other will be computed based on the proportions of the source image.

Finally, you can set the output path with `--outfile` option. Don't forget to add the right extension of the image.

The script is tested on JPG and PNG formats.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
