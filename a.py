#-------------------------------------------------------------------------------
#-*- coding:utf-8 -*-
# Name:        module1
# Purpose:
#
# Author:      ghkdq
#
# Created:     16-05-2019
# Copyright:   (c) ghkdq 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
import csv
import sys
import chardet
import codecs

line_counter = 0

df = pd.read_csv('2.csv')


print(df)


##infile = codecs.open('final2.csv','r',encoding='utf-8')

##for line in infile:
##    line = line.replace(u'\xa0', ' ')
##    print(line)


##infile.close()




print(u'우아아아')