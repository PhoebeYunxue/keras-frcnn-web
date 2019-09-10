import os
import xml.etree.ElementTree as ET


xmlfilepath = 'Annotations'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)

for i in range(1,num):
    name = total_xml[i]
    print(name)
    path_root = '/Users/phoebechen/Desktop/keras-frcnn-web/VOC2007/Annotations/'+name
    tree = ET.parse(path_root)
    root = tree.getroot()
    path = root[2].text
    root[2].text = path_root
    print(root[2].text)
    tree.write(path_root)