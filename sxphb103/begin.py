from scrapy import cmdline
import sys
print('请选择要输出的格式')
print('1.json')
print('2.csv')
a = int(input('请输入:\n'))
if a == 1:
    #输出json
    # cmdline.execute('scrapy crawl sxphb -o Sxphb.json'.split())
    cmdline.execute('scrapy crawl sxphb -o test.json'.split())
elif a == 2:
    #输出csv,需要在setting中更改编码为gbk
    cmdline.execute('scrapy crawl sxphb -o Sxphb.csv'.split())
else:
    sys.exit('输入有误，程序退出')