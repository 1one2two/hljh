#!/bin/bash
# Program:
#       This program shows "Hello World!" in your screen.
# History:
# 2015/07/16	VBird	First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

echo "Start install \a \n"
sudo i2cdetect -y 1

cd ~
git clone https://github.com/Seeed-Studio/grove.py

cd grove.py/
sudo pip install .

sudo pip install hcsr04sensor

#Download hljh.py

#Download node red

#Set hostname

exit 0
