import urllib.request;
import re;
import sys;
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd);
url='https://movie.douban.com/subject/25812730/';
file=urllib.request.urlopen(url);
data=file.read().decode().translate(non_bmp_map);
pattern=re.compile('(?<=<span class="rating_per">)\d+\.\d+');
m=pattern.findall(data);
num=[float(i) for i in m];
sum=0;
x=5.0;
for i in num:
    sum=sum+0.010*i*x*2.0;
    x=x-1;
print (num);
print (sum);

