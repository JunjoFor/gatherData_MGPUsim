import sys
from dataclasses import dataclass

file = open(sys.argv[1], "r")

@dataclass
class PageEntry:
    where: str
    page: int
    re_ejected: int

pages_25 = []

for line in file:
    if int(line.split(",")[4].split(":")[1]) >= 25:
        if (len(pages_25)) == 0:
            pages_25.append(PageEntry(line.split(",")[2].split("@")[1], int(line.split(",")[3].split(":")[1]), 0))
        else:
            for entry in pages_25:
                if entry.where == line.split(",")[2].split("@")[1] and entry.page == int(line.split(",")[3].split(":")[1]):
                    entry.re_ejected +=1
                else:
                    if len(pages_25) < 5000:
                        pages_25.append(PageEntry(line.split(",")[2].split("@")[1], int(line.split(",")[3].split(":")[1]), 0))
        
percentil0 = 0.0
percentil1000 = 0.0
percentil2000 = 0.0
percentil3000 = 0.0
percentil5000 = 0.0
percentil10000 = 0.0

for entry in pages_25:
    if entry.re_ejected >= 10000:
        percentil10000+=1
    elif entry.re_ejected >= 5000:
        percentil5000+=1
    elif entry.re_ejected >= 3000:
        percentil3000+=1
    elif entry.re_ejected >= 2000:
        percentil2000+=1
    elif entry.re_ejected >1000:
        percentil1000+=1
    elif entry.re_ejected >=0:
        percentil0+=1


print("Numeros")
print("0-999: " + str(percentil0))
print("1000-1999: " + str(percentil1000))
print("2000-2999: " + str(percentil2000))
print("3000-4999: " + str(percentil3000))
print("5000-9999: " + str(percentil5000))
print("+10000: " + str(percentil10000))

print("Percentaje")
print("0-999: " + str(percentil0/len(pages_25)))
print("1000-1999: " + str(percentil1000/len(pages_25)))
print("2000-2999: " + str(percentil2000/len(pages_25)))
print("3000-4999: " + str(percentil3000/len(pages_25)))
print("5000-9999: " + str(percentil5000/len(pages_25)))
print("+10000: " + str(percentil10000/len(pages_25)))