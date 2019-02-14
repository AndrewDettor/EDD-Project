import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import re
import ssl


# Ignore SSL certificate errors

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


# Get all text from the Passmark GPU page, slim down to only GPUs

url = 'https://www.videocardbenchmark.net/common_gpus.html'

html = urllib.request.urlopen(url, context=context).read()
soup = BeautifulSoup(html, 'html.parser')

GPUlist = soup.get_text().split('\n')
GPUlist = GPUlist[182: 282]
# FORMAT: (, '  GeForce GTX 1080 Ti   14,205', '$779.89*',)


# Get all text from the Passmark CPU page, slim down to only CPUs

url = 'https://www.cpubenchmark.net/common_cpus.html'

html = urllib.request.urlopen(url, context=context).read()
soup = BeautifulSoup(html, 'html.parser')

CPUlist = soup.get_text().split('\n')
CPUlist = CPUlist[198: 298]
# FORMAT: (, '  Intel Core i5-3337U @ 1.80GHz    3,222       $225.00* ',)


# Get all text from the Passmark Hard Drive page, slim down to only Hard Drives

url = 'https://www.harddrivebenchmark.net/common_drives.html'

html = urllib.request.urlopen(url, context=context).read()
soup = BeautifulSoup(html, 'html.parser')

drivelist = soup.get_text().split('\n')
drivelist = drivelist[183:483]
# FORMAT: ('Samsung SSD 970 EVO 500GB', '21,736', '$147.55*')


# Get all the text from the PCPartPicker RAM section, slim down to only RAM

url = 'https://pcpartpicker.com/products/memory/#R=5,4,3&X=1466,281794&sort=-rating&page=1'

html = urllib.request.urlopen(url, context=context).read()
soup = BeautifulSoup(html, 'html.parser')

RAMlist = soup.get_text().split('\n')

RAMlist = RAMlist[:]

print(RAMlist)
