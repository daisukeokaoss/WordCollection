# -*- coding: utf-8 -*-
#医療単語を追加する


import urllib2

#import HTMLParser
from TextHTMLParser import TestHTMLParser


from MedicalWordURLCollection import MedicalWordURLStore

from StoreToText import StoreToFile_class

from constructSourceCode_Obejective_c import constructSourceCode_Obejective_c




#URLCollection = MedicalWordURLStore().ReturnURLArray()
URLCollection = ['http://ejje.weblio.jp/category/computer/cmpyg/aa/10']

construct = constructSourceCode_Obejective_c()

construct.SetDataToConstructSource(URLCollection)
construct.ConstructAndOutputArray("/Users/okadaisuke/Desktop/WordStore.txt")





