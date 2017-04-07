__author__ = 'zhazhich'
# this script is used to delete line symbol to .* for automation excel data
import re
import linecache
import os
def get_content(path):
    if os.path.exists(path):
        content = linecache.getlines(path)
        return content
    else:
        print('the path [{}] is not exist!'.format(path))


data_path = 'C:\\Users\\zhazhich\\PycharmProjects\\subtoexcel\\data.txt'
content = get_content(data_path)
str=''
for i in range(0,len(content)):
    content[i]=content[i].lstrip()  #delete blank at front
    content[i]=re.sub(r'\n','',content[i])
    content[i]=re.sub(r'from',' from',content[i])
    content[i]=re.sub(r'where',' where',content[i])
    content[i]=re.sub(r'left','  left',content[i])
print (content, end="")
a=''
str=a.join(content)
print ()
print(str)