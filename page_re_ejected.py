import sys
from dataclasses import dataclass

file = open(sys.argv[1] + "page_touches.txt" , "r")

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
percentil25 = 0.0
percentil50 = 0.0
percentil100 = 0.0
percentil500 = 0.0
percentil1000 = 0.0

for entry in pages_25:
    if entry.re_ejected >= 1000:
        percentil1000+=1
    elif entry.re_ejected >= 500:
        percentil500+=1
    elif entry.re_ejected >= 100:
        percentil100+=1
    elif entry.re_entry >= 50:
        percentil50+=1
    elif entry.re_entry >=25:
        percentil25+=1
    elif entry.re_entry >=0:
        percentil0+=1


print("Numeros")
print("0-24: " + str(percentil0))
print("25-49: " + str(percentil25))
print("50-99: " + str(percentil50))
print("100-499: " + str(percentil100))
print("500-999: " + str(percentil500))
print("+1000: " + str(percentil1000))

print("Percentaje")
print("0-24: " + str(percentil0/len(pages_25)))
print("25-49: " + str(percentil25/len(pages_25)))
print("50-99: " + str(percentil50/len(pages_25)))
print("100-499: " + str(percentil100/len(pages_25)))
print("500-999: " + str(percentil500/len(pages_25)))
print("+1000: " + str(percentil1000/len(pages_25)))
