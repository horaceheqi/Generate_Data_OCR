import random
from PIL import Image, ImageColor, ImageFont, ImageDraw, ImageFilter


# 判断一个unicode是否是汉字
def is_chinese(uchar):
    if '\u4e00' <= uchar <= '\u9fff':
        return True
    else:
        return False


# 判断一个unicode是否是数字
def is_number(uchar):
    if '\u0030' <= uchar <= '\u0039':
        return True
    else:
        return False


# 判断一个unicode是否是英文字母
def is_alphabet(uchar):
    if ('\u0041' <= uchar <= '\u005a') or ('\u0061' <= uchar <= '\u007a'):
        return True
    else:
        return False


def judge_word_type(word, _type, _color, _size, _key):
    #  isdigit()方法检测字符串是否只由数字组成,isalpha()方法检测字符串是否只由字母和汉子组成.
    # random.sample(_type[0], 1)[0], int(random.sample(_size[0], 1)[0]), ImageColor.getrgb(random.sample(_color[0], 1)[0])
    if word in ['￥', '¥']:
        return './fonts/SimSun.ttf', int(_size[0]), _color[0]
    elif word in ['ⓧ']:
        return './fonts/SourceHanSans-Normal.ttf', int(_size[0]), _color[0]
    elif word in ['%', '.', '+', '-', '*', '/', '<', '>']:
        return _type[0], int(_size[0]), _color[0]
    elif _key in ['train'] and word == '站':
        return _type[3], int(_size[3]), _color[3]
    elif is_chinese(word):
        return _type[0], int(_size[0]), _color[0]
    elif is_number(word):
        return _type[1], int(_size[1]), _color[1]
    elif is_alphabet(word):
        return _type[2], int(_size[2]), _color[2]
    else:  # 其他
        return _type[1], int(_size[1]), _color[1]


def generate(key, text_content, text_type, text_color, font_size, space_width, text_fluctuate, fit):
    _key = key.split('_')[0]
    if _key not in ['mixed', 'train']:
        return _generate_text(text_content, text_type, text_color, font_size, space_width, fit)
    else:
        return _generate_mixed_text(_key, text_content, text_type, text_color, font_size, space_width, text_fluctuate,
                                    fit)


def _generate_text(words, font_type, font_color, font_size, space_width, fit):
    # print(words)
    # print(words)
    bbox_x_min, bbox_x_max = [], []
    txt_img = None
    image_font = ImageFont.truetype(font=font_type, size=int(font_size))
    space_width = image_font.getsize(' ')[0] * space_width
    words_width = [image_font.getsize(w)[0] for w in words]
    text_width = sum(words_width) + int(space_width) * (len(words) - 1)
    text_height = max([image_font.getsize(w)[1] for w in words])
    txt_img = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
    txt_draw = ImageDraw.Draw(txt_img)
    color = ImageColor.getrgb(font_color)
    for i, w in enumerate(words):
        bbox_x_min.append(sum(words_width[0:i]) + i * int(space_width))
        image_font = ImageFont.truetype(font=font_type, size=int(font_size))
        txt_draw.text((sum(words_width[0:i]) + i * int(space_width), 0), w, fill=color, font=image_font)
        bbox_x_max.append(sum(words_width[0:i + 1]) + i * int(space_width))
    if fit:
        return txt_img.crop(txt_img.getbbox()), bbox_x_min, bbox_x_max
    else:
        return txt_img, bbox_x_min, bbox_x_max


def _generate_mixed_text(_key, words, font_type, font_color, font_size, space_width, text_fluctuate, fit):
    res_font, res_color, res_size = dict(), dict(), dict()
    _fluctuate = random.randint(0, 2) if text_fluctuate else 0
    bbox_x_min, bbox_x_max, text_width, text_height = [], [], [], []
    txt_img, words_width, spaces_width, image_height = None, [], [], []
    for k, v in font_type.items():
        temp_font = random.sample(v, 1)[0]
        temp_size = int(random.sample(font_size[k], 1)[0])
        temp_color = ImageColor.getrgb(random.sample(font_color[k], 1)[0])
        res_font[k], res_size[k], res_color[k] = temp_font, temp_size, temp_color
    for w in words:
        temp_font, temp_size, _ = judge_word_type(w, res_font, res_color, res_size, _key)
        image_font = ImageFont.truetype(font=temp_font, size=temp_size)
        spaces_width.append(image_font.getsize(' ')[0] * space_width)
        words_width.append(image_font.getsize(w)[0])
        image_height.append(image_font.getsize(w)[1])
    text_width = sum(words_width) + sum(spaces_width)
    text_height = max(image_height) + _fluctuate
    # text_width.append(_width)
    # text_height.append(_height)
    txt_img = Image.new('RGBA', (int(text_width), int(text_height)), (0, 0, 0, 0))
    txt_draw = ImageDraw.Draw(txt_img)
    # print(words)
    for i, w in enumerate(words):
        bbox_x_min.append(sum(words_width[0:i]) + i * int(space_width))
        _font, _size, _color = judge_word_type(w, res_font, res_color, res_size, _key)
        image_font = ImageFont.truetype(font=_font, size=_size)
        txt_draw.text((sum(words_width[0:i]) + sum(spaces_width[0:i]), _fluctuate), w, fill=_color, font=image_font)
        bbox_x_max.append(sum(words_width[0:i + 1]) + sum(spaces_width[0:i]))
    if fit:
        return txt_img.crop(txt_img.getbbox()), bbox_x_min, bbox_x_max
    else:
        return txt_img, bbox_x_min, bbox_x_max
