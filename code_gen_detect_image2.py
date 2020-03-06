import os
import sys
dir_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dir_)
import random
from PIL import Image
import template2 as template
from code_process.XML import xml_operate
import code_process.background_generator as background_generator
from code_process.string_generator import select_string_from_file
import code_process.computer_text_generator as computer_text_generator


class FakeTextDataGenerator(object):
    @staticmethod
    def fine_tuning(key, _font, _color, _size):
        if key.split('_')[0] in ['mixed', 'train']:
            res_font = _font
            res_color = _color
            res_size = _size.copy()
            for k, v in _size.items():
                res_size[k] = [i + random.randint(-5, 5) for i in v]
            return res_font, res_color, res_size
        else:
            res_font = _font[0] if len(_font) == 1 else random.sample(_font, 1)[0]
            res_color = _color[0] if len(_color) == 1 else random.sample(_color, 1)[0]
            res_size = [i + random.randint(-5, 5) for i in _size][0]
            return res_font, res_color, res_size

    @classmethod
    def generate_from_tuple(self, t):
        self.generate(*t)

    @classmethod
    def generate(self, index, out_dir, extension):
        # random.seed(1)
        # 这里需要设置针对的加载模板(例如id_card)
        template_content = template.invoice_electronic
        # create background
        background = background_generator.picture_full(template_content.get('bank_ground'))
        background = background.resize([736, 736], Image.ANTIALIAS)
        background_width = background.size[0]
        background_height = background.size[1]


        self.xml = xml_operate()
        self.xml.add_size(width=str(background_width), height=str(background_height))

        image_heights, all_lists, gap_row, text_fluctuate = [], [], [], ''
        gap_row.append(12)
        temp_width, temp_height = random.randint(5, 10), 0
        for key in template_content.keys():
            if key == 'bank_ground':
                continue
            style = template_content.get(key)
            temp_list = [key for _ in range(style.get("count"))]
            all_lists += temp_list
        while all_lists:
            random_key = random.sample(all_lists, 1)[0]
            style = template_content.get(random_key)
            text_content = select_string_from_file(style.get("text"))
            # print(style.get("text"))
            text_font, text_color, text_size = FakeTextDataGenerator.fine_tuning(
                random_key, style.get("font_type"), style.get("font_color"), style.get("font_size"))
            text_space = random.randint(0, 5) / 10
            if random_key.split('_')[0] == 'mixed':
                text_fluctuate = style.get("fluctuate")
            text_line_image, start_tags, end_tags = computer_text_generator.generate(
                random_key, text_content, text_font, text_color, text_size, text_space, text_fluctuate, fit=True)
            if text_line_image.size[0] > background_width or text_line_image.size[1] > background_height:
                continue
            else:
                # 2，粘贴
                row = random.randint(10, 15)
                col = random.randint(10, 15)
                remain_width = background.size[0] - temp_width
                # 单行能放下
                if remain_width > text_line_image.size[0]:
                    text_x_min = temp_width + random.randint(10, 15)
                    text_y_min = sum(image_heights) + sum(gap_row)
                    text_x_max = text_x_min + text_line_image.size[0]
                    text_y_max = text_y_min + text_line_image.size[1]
                    if text_y_max < background.size[1] and text_x_max < background.size[0]:
                        all_lists.remove(random_key)
                        temp_width = text_x_max + col
                        temp_height = text_line_image.size[1] if text_line_image.size[1] > temp_height else temp_height
                        background.paste(text_line_image, (text_x_min, text_y_min), text_line_image)
                        self.xml.add_object(text_content, str(text_x_min), str(text_y_min), str(text_x_max),
                                            str(text_y_max))
                    else:
                        continue
                # 单行放不下 换下一行
                elif remain_width < text_line_image.size[0] and background_height > text_line_image.size[1]:
                    temp_width = random.randint(10, 15)
                    gap_row.append(row)
                    image_heights.append(temp_height)
                    text_x_min = temp_width + random.randint(10, 15)
                    text_y_min = sum(image_heights) + sum(gap_row)
                    text_x_max = text_x_min + text_line_image.size[0]
                    text_y_max = text_y_min + text_line_image.size[1]
                    if text_y_max < background.size[1] and text_x_max < background.size[0]:
                        all_lists.remove(random_key)
                        temp_width = text_x_max + col
                        temp_height = text_line_image.size[1]
                        background.paste(text_line_image, (text_x_min, text_y_min), text_line_image)
                        self.xml.add_object(text_content, str(text_x_min), str(text_y_min), str(text_x_max),
                                            str(text_y_max))
                    else:
                        continue
                # 单行放不下，并且到图片最后一行
                else:
                    break
        # Generate name for resulting image
        image_name = 'invoice_electronic_{}.{}'.format(str(index), extension)
        self.xml.add_file_name(image_name)
        # Save the image
        background.convert('RGB').save(os.path.join(out_dir, 'Images', image_name), 'JPEG', quality=100)
        print(os.path.join(out_dir, 'Images', image_name))
        self.xml.generate_xml(os.path.join(out_dir, 'Labels', 'invoice_electronic_{}.{}'.format(str(index), "xml")))
