import os
import errno
import argparse
from multiprocessing import Process
from code_gen_detect_image2 import FakeTextDataGenerator


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate synthetic text data for text recognition.')
    parser.add_argument(
        "--output_dir",
        type=str,
        nargs="?",
        help="The output directory",
        default="output/detect/",
    )
    parser.add_argument(
        "-s",
        "--start_index",
        type=int,
        nargs="?",
        help="The start index of images to be created.",
        default=1
    )
    parser.add_argument(
        "-end",
        "--end_index",
        type=int,
        nargs="?",
        help="The end index of images to be created.",
        default=5
    )
    parser.add_argument(
        "-e",
        "--extension",
        type=str,
        nargs="?",
        help="Define the extension to save the image with",
        default="jpg",  # 图片格式
    )
    return parser.parse_args()


def run(start_index, end_index, output_dir, extension):
    f = FakeTextDataGenerator()
    for i in range(start_index, end_index + 1):
        f.generate(i, output_dir, extension)


def main():
    constant = parse_arguments()
    # create the directory if it does not exist.
    try:
        os.makedirs(constant.output_dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.makedirs(os.path.join(constant.output_dir, 'Images'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.makedirs(os.path.join(constant.output_dir, 'Labels'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    image_num = constant.end_index + 1 - constant.start_index
    process_num = 5
    image_per_process = image_num // process_num
    for i in range(process_num):
        start_index = i * image_per_process + 1
        end_index = (i + 1) * image_per_process
        p = Process(target=run, args=(start_index, end_index, constant.output_dir, constant.extension))
        p.start()
    # run(constant.start_index, constant.end_index, constant.output_dir, constant.extension)


if __name__ == '__main__':
    main()
