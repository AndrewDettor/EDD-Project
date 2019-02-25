import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


# LIST FORMAT: ('name', 'score', 'price')
# 'price' could equal 'NA'


def getGPUlist():
    # Get all text from the Passmark GPU page, slim down to only GPUs

    url = 'https://www.videocardbenchmark.net/common_gpus.html'

    html = urllib.request.urlopen(url, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    GPUlist = soup.get_text().split('\n')
    GPUlist = GPUlist[182: 282]

    newGPUlist = []

    for index, value in enumerate(GPUlist):
        if index % 2 is 0 or index is 0:

            # Name and Score are on every even index. Split by space, and remove empty elements.
            templist = value.strip().split(" ")
            templist = list(filter(None, templist))

            # Score is the last element.
            tempscore = templist[-1]

            # Shorten templist down to just the name of the part.
            templist = templist[:-1]

            #  Name was split by each space, so put it back together
            tempname = ''
            for value in templist:
                tempname = tempname + value + ' '

            # Remove the extra space
            tempname = tempname[:-1]

            # Price is on the next index after the Name/Score index. Get price, then remove the *.
            tempprice = GPUlist[index + 1]
            if '*' in tempprice:
                tempprice = tempprice[:-1]

            # Put tuple of info in new GPUlist bc the indexes are fucked on the original list
            newGPUlist.append((tempname, tempscore, tempprice))

    return newGPUlist


def getCPUlist():
    # Get all text from the Passmark CPU page, slim down to only CPUs

    url = 'https://www.cpubenchmark.net/common_cpus.html'

    html = urllib.request.urlopen(url, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    CPUlist = soup.get_text().split('\n')
    CPUlist = CPUlist[198: 298]

    for index, value in enumerate(CPUlist):

        # Each value has all the info in one index. Split each index by space, and remove empty space.
        templist = value.strip().split(" ")
        templist = list(filter(None, templist))

        # Price is the last element. Get price, then remove the * if there is one
        tempprice = templist[-1]
        if '*' in tempprice:
            tempprice = tempprice[:-1]

        # Score is the second to last element
        tempscore = templist[-2]

        # Shorten templist down to just the name of the part.
        templist = templist[:-2]

        #  Name was split by each space, so put it back together
        tempname = ''
        for value in templist:
            tempname = tempname + value + ' '

        # Remove the extra space
        tempname = tempname[:-1]

        # Replace the original spot in CPUlist with the tuple of info
        CPUlist[index] = (tempname, tempscore, tempprice)

    return CPUlist


def getDrivelist():
    # Get all text from the Passmark Hard Drive page, slim down to only Hard Drives

    url = 'https://www.harddrivebenchmark.net/common_drives.html'

    html = urllib.request.urlopen(url, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    drivelist = soup.get_text().split('\n')
    drivelist = drivelist[183:483]

    newdrivelist = []
    count = 3

    for index, value in enumerate(drivelist):
        # Each 3 elements in drivelist need to be combined into one tuple
        if count % 3 is 0:
            tempname = drivelist[index]
            tempscore = drivelist[index + 1]
            tempprice = drivelist[index + 2]

            if '*' in tempprice:
                tempprice = tempprice[:-1]

            newdrivelist.append((tempname, tempscore, tempprice))

        count += 1

    return newdrivelist


def getRAMlist():
    # FORMAT [('name', 'type', 'speed', 'size', 'price/GB', 'price')]
    return [('G.Skill NT Series', 'DDR4', '2133 Mhz', '8 GB', '$5.50', '$43.98'),
            ('Team Vulcan', 'DDR4', '2400 Mhz', '8 GB', '$5.62', '$44.99'),
            ('Crucial Ballistix Sport LT', 'DDR4', '2666 Mhz', '8 GB', '$5.74', '$45.89')]


print(getGPUlist())
print('\n\n')
print(getCPUlist())
print('\n\n')
print(getDrivelist())
print('\n\n')
print(getRAMlist())
