input_data = input()

sdata = []
sum = 0
 # 65 ~ 90 'A' ~ 'Z'
for i in range(len(input_data)):
    if(ord(input_data[i])>= 65 and ord(input_data[i]) <= 90):
        sdata.append(input_data[i])
    else:
        sum += int(input_data[i])
sdata.sort() #정렬

if(sum != 0):
    sdata.append(str(sum))

for data in sdata:
    print(data,end="")











