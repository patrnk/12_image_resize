from argparse import ArgumentParser
from math import isclose
import sys
import os.path

from PIL import Image


def have_different_proportions(image, size):
    return not isclose(image.size[0] / image.size[1], size[0] / size[1], abs_tol=0.01)


def no_size_specified(args):
    return not args.width and not args.height and not args.scale


def resolution_and_scale_specified(args):
    return (args.width or args.height) and args.scale


def retrieve_output_size_from_args(args, input_size):
    if args.width and args.height:
        return (args.width, args.height)
    if args.scale:
        return (round(input_size[0] * args.scale), round(input_size[1] * args.scale))
    scale = input_size[0] / input_size[1]
    if args.width and not args.height:
        output_height = round(args.width / scale)
        return (args.width, output_height)
    if not args.width and args.height:
        output_width = round(args.height * scale)
        return (output_width, args.height)


def get_resized_image_name(source_image_name, resulting_size):
    name, extension = os.path.splitext(source_image_name)
    width, height = resulting_size
    size_suffix = '__{0}x{1}'.format(width, height)
    return '{0}{1}.{2}'.format(name, size_suffix, extension)


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('--width', type=int)
    parser.add_argument('--height', type=int)
    parser.add_argument('--scale', type=float)
    parser.add_argument('--outfile', '-o')
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    if no_size_specified(args):
        print('Specify the size of the output image.')
        sys.exit(1)
    if resolution_and_scale_specified(args):
        print('Specify either the resolution or the scale, not both.')
        sys.exit(1)
    source_image = Image.open(args.infile)
    output_size = retrieve_output_size_from_args(args, source_image.size)
    if have_different_proportions(source_image, output_size):
        print('The output image size has propotions different from the initial one.')
    output_image = source_image.resize(output_size)
    output_image_path = args.outfile or get_resized_image_name(args.infile, output_size)
    output_image.save(output_image_path)
