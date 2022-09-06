
'''python 冒泡排序'''

list = [23,4,12,45,76,34]

def Bullet_sort():
    for i in range(len(list)):
        for j in range(len(list)-1 -i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

Bullet_sort()

for i in list:
    print(i,end="   ")
    
    
    
   ''''''
