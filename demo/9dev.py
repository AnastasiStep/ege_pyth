str = ""
i = 0
while i < 250:
    i+=1
    str += '3'
while ('3333' in str) or ('7777' in str):
    if ('3333' in str):
        str = str.replace('3333', '7')
    else:
        str = str.replace('777', '3')
print(str)