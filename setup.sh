#!/bin/bash
# Program:
#       Install HLJH
# History:
# 2019/06/27	
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

echo "Start install \a \n"
sudo i2cdetect -y 1

cd ~
git clone https://github.com/Seeed-Studio/grove.py

cd grove.py/
sudo pip install .

sudo pip install hcsr04sensor

curl https://raw.githubusercontent.com/1one2two/hljh/master/hljh.py -o /grove.py/grove/

#Download node red

#Set hostname

exit 0
