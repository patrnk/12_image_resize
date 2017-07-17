from argparse import ArgumentParser
import sys

from PIL import Image


def resize_image(image):
    raise NotImplemented


def have_different_proportions(image, size):
    return image.size[0] / image.size[1] != size[0] / size[1]


def no_size_specified(args):
    return not args.width and not args.height and not args.scale


def resolution_and_scale_specified(args):
    return (args.width or args.height) and args.scale


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('--width', type=int)
    parser.add_argument('--height', type=int)
    parser.add_argument('--scale', type=int)
    parser.add_argument('--outfile', '-o')
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    if no_size_specified:
        print('Specify the size of the output image')
        sys.exit(1)
    if resolution_and_scale_specified:
        print('Specify either the resolution or the scale, not both')
        sys.exit(1)
    source_image = Image.open(args.infile)
    if have_different_proportions(source_image, args.width, args.height):
        print('The new size has propotions different from the initial one.')
