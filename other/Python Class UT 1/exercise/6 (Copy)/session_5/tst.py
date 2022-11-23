import os
import re
import shutil


filenames= os.listdir('.')
specials= []



for filename in filenames:
 if re.search(r'__\w+__', filename):
     specials.append(filename)

print(specials)

specials_paths= [os.path.abspath(filename) for filename in specials]
print(specials_paths)



if not os.path.exists('.\\specials'):
    os.mkdir('.\\specials')

for path in specials_paths:
    shutil.copy(path, 'specials')
