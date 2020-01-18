from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
import xml.etree.ElementTree as ET
import sys

#command line ops https://www.tutorialspoint.com/python/python_command_line_arguments.htm
inputFile = sys.argv[1]
outputFile = sys.argv[2]

tree = ET.parse(inputFile)
root = tree.getroot()

root.findall('./rank') #None
root.findall('.//rank') #3 Elements with tag as 'rank'
root.findall('.//rank/') # None as rank is leaf
r = root.find('.//rank') #the first Elements with tag as 'rank'
t = r.text # it will be 1

## xml output
top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child',{"text":1, "name":2})
child.set("text", 1)
child.set("name", 2)
child.attrib["text"] = 1

child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'

ET.ElementTree(top).write("output.xml")

## json output
sample = {}
sample["key"] = 'value'

import json
with open('result.json', 'w') as fp:
    json.dump(sample, fp)



