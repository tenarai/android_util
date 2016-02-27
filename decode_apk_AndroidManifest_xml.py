# This script can be decode apk encoded AndroidManifest.xml.
# pip install androguard
# python decode_apk_AndroidManifest_xml.py AndroidManifest.xml
# 
import sys
from androguard.core.bytecodes import apk

file_name = sys.argv[1]
filep = open(file_name)
axml_printer = apk.AXMLPrinter(filep.read())
android_xml = axml_printer.get_xml()
print(android_xml)
