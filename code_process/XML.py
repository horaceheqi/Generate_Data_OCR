import os
import xml.etree.cElementTree as ET


class xml_operate(object):
    def __init__(self):
        self.root = ET.Element('annotation')

    def __add_node__(self, parent_node_name, sub_node_name, sub_node_content):
        if parent_node_name == 'annotation':
            # tree = ET.ElementTree(self.root)
            # self.root = tree.getroot()
            sub_node = ET.Element(sub_node_name)
            sub_node.text = sub_node_content
            self.root.append(sub_node)
        else:
            tree = ET.ElementTree(self.root)
            self.root = tree.getroot()
            parent_node = tree.find(parent_node_name)
            if parent_node is None:
                parent_node = ET.Element(parent_node_name)
                self.root.append(parent_node)
            node = ET.Element(sub_node_name)
            if sub_node_content != "":
                node.text = sub_node_content
            parent_node.append(node)

    def add_file_name(self, filename):
        self.__add_node__("annotation", "filename", filename)

    def add_template(self, template_name):
        self.__add_node__("annotation", "template", template_name)

    def add_size(self, width, height):
        self.__add_node__("annotation", "size", "")
        self.__add_node__("size", "width", width)
        self.__add_node__("size", "height", height)

    def add_object(self, name, xmin, ymin, xmax, ymax):
        object_node = ET.Element('object')
        object_name_node = ET.SubElement(object_node, "name")
        object_name_node.text = name

        bndbox_node = ET.SubElement(object_node, "bndbox")
        xmin_node = ET.SubElement(bndbox_node, "xmin")
        xmin_node.text = xmin
        ymin_node = ET.SubElement(bndbox_node, "ymin")
        ymin_node.text = ymin
        xmax_node = ET.SubElement(bndbox_node, "xmax")
        xmax_node.text = xmax
        ymax_node = ET.SubElement(bndbox_node, "ymax")
        ymax_node.text = ymax
        tree = ET.ElementTree(self.root)
        self.root = tree.getroot()
        self.root.append(object_node)

    def generate_xml(self, path):
        if os.path.exists(path):
            os.remove(path)
        tree = ET.ElementTree(self.root)
        tree.write(path, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    xml = xml_operate()
    xml.add_file_name("00.png")
    xml.add_template("faf")
    xml.add_size("512", "320")
    xml.add_object("tittle:北京增值税发票", "112", "36", "182", "58")
    xml.add_object("key1", "112", "36", "182", "58")
    xml.generate_xml("./out/test.xml")
