import sys
file = open(sys.argv[1] + "page_touches.txt" , "r")

total_lines = 0

percentil0 = 0.0
percentil1 = 0.0
percentil10 = 0.0
percentil25 = 0.0
percentil100 = 0.0
percentil1000 = 0.0
percentil2000 = 0.0
percentil5000 = 0.0

for line in file:
    total_lines= total_lines+1
    if int(line.split(",")[4].split(":")[1]) >= 5000:
        percentil5000+=1
    elif int(line.split(",")[4].split(":")[1]) >= 2000:
        percentil2000+=1
    elif int(line.split(",")[4].split(":")[1]) >= 1000:
        percentil1000+=1
    elif int(line.split(",")[4].split(":")[1]) >= 100:
        percentil100+=1
    elif int(line.split(",")[4].split(":")[1]) >= 25:
        percentil25+=1
    elif int(line.split(",")[4].split(":")[1]) >=10:
        percentil10+=1
    elif int(line.split(",")[4].split(":")[1]) >= 1:
        percentil1+=1
    elif int(line.split(",")[4].split(":")[1]) == 0:
        percentil0+=1

# print("Printing numbers")
# print("0: " + str(percentil0))
# print("1-9: " + str(percentil1))
# print("10-24: " + str(percentil10))
# print("25-99: " + str(percentil25))
# print("100-999: " + str(percentil100))
# print("1000-1999: " + str(percentil1000))
# print("2000-4999: " + str(percentil2000))
# print("+5000: " + str(percentil5000))

print("Printing percentajes")
print(str(percentil0/total_lines) ) # 0
print(str(percentil1/total_lines)) #1-9
print(str(percentil10/total_lines)) #10-24
print(str(percentil25/total_lines)) #25-99
print(str(percentil100/total_lines)) #100-999
print(str(percentil1000/total_lines)) #1000-1999
print(str(percentil2000/total_lines)) #2000-4999
print(str(percentil5000/total_lines)) #5000