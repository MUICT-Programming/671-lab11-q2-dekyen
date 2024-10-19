# YOUR CODE HERE
n=int(input())
lst1=[]
lst2=[]

for i in range(n):
    a=int(input())
    lst1.append(a)

for i in range(n):
    a=int(input())
    lst2.append(a)

def sumation(a,b):
    lst_sum=[]
    global n
    for i in range(n):
        sum=a[i]+b[i]
        lst_sum.append(sum)
    return lst_sum

lst_sum=sumation(lst1,lst2)

def find_min_max(lst1_sum):
    max=lst_sum[0]
    min=lst_sum[0]
    for i in lst1_sum:
        if i > max :
            max=i
        else:
            continue
    
    for i in lst_sum:
        if i < min:
            min=i
        else:
            continue

    min_max=(min,max)
    return min_max

print(sumation(lst1,lst2))
print(find_min_max(lst_sum))
