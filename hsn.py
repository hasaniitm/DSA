'''numbers = [10,21, 20,100, 30, 40, 50]
even=0
odd=0

for i in numbers:
    if i%2==0:
        even+=1
    
    else:
        odd+=1
print(f"Even : {even}\nOdd : {odd}")'''


'''numbers = [1, 2, 3, 2, 4, 1, 5, 3]
n=[]
for i in numbers:
    if i not in n:
        n.append(i)
print(n)'''

# numbers = [1, 2, 3, 2, 4, 1, 5, 3]
# numbers.reverse()
# print(numbers)


'''
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
print(numbers[::-1])


numbers = [1, 2, 3, 2, 4, 1, 5, 3]
s=list(set(numbers))
print(s[-2])
'''

'''
numbers = [0, 1, 0, 3, 12, 0, 5]
l=[]
m=[]
for i in numbers:
    if i==0:
        l.append(i)
    else:
        m.append(i)


m.extend(l)
print(m)
'''


'''a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]


s=[]
for i in a:
    if i in b:
        s.append(i)
print(s)'''


'''
numbers = [1, 2, 2, 3, 3, 3, 4, 4]

n={}
for i in numbers:
    if i in n:
        n[i]+=1
    else:
        n[i]=1
print(n)
'''

'''
s = "programming"
vow='aeiouAEIOU'
vow_count=0
cons=0

for i in s:
    if i in vow:
        vow_count+=1
    else:
        cons+=1
print(f"Vowel:{vow_count}\nCons:{cons}")
'''


'''s = "madam"
if s[::]==s[::-1]:
    print(True)
else:
    print(False)'''
    
'''s = "banana"
n={}

for i in s:
    if i in n:
        n[i]+=1
    else:
        n[i]=1
print(n)'''

'''s = "programming"
g=[]
for i in s:
    if i not in g:
        g.append(i)
print(''.join(g))'''

# s = "aabbcde"
# n={}
# for i in s:
#     if i in n:
#         n[i]+=1
#     else:
#         n[i]=1


# l=[]
# for i in n:
#     if n.get(i)==1:
#         l.append(i)
# print(l[0])


'''
s = "Python is very powerful language"
m=s.split(' ')
k=[]
for i in m:
    k.append(i)

print(m[i],max(k))
'''




'''
s = "hello python world"
h=s.split(' ')
m=[]
for i in h:
    m.append(i[::-1])
print(' '.join(m))
'''

s = "Python is very powerful languages"
# m=s.split(' ')
# h={}

# for i in m:
#     h[i]=len(i)
# print(h)

# s = "A8B3C2"
# for i in range(0,len(s),2):
#     print(f"{s[i]*int(s[i+1])}",end='')

'''numbers = [1, 2, 3, 2, 4, 5, 1, 3]
n={}
for i in numbers:
    if i in n:
        n[i]+=1
    else:
        n[i]=1
        
print(n)
        
s=max(n,key=n.get)
print(s)'''

# s = "mississippi"
# n={}
# for i in s:
#     if i in n:
#         n[i]+=1
#     else:
#         n[i]=1
# f=max(n,key=n.get)     
# print(f)
    
        
# numbers = [10, 50, 30, 80, 60, 80]
# numbers=set(numbers)
# numbers=list(numbers)
# print(numbers[-2])

# numbers = [10, 15, 20, 25, 30, 35, 40]
# count=0
# for i in numbers:
#     if i%2==1:
#         count+=i
#     else:
#         pass
# print(count)
# s = "programming"
# v='aeiouAEIOU'

# count=0

# for i in s:
#     if i in v:
#         count+=1
# print(count)
        
# numbers = [10, 45, 20, 80, 60, 80]   
# print(numbers)
# numbers=set(numbers)  
# numbers=list(numbers)
# numbers.sort()
# print(numbers[-2])

    
# numbers = [1, 2, 2, 3, 4, 4, 5]
# lst=[]
# for i in numbers:
#     if i not in lst:
#         lst.append(i)
# print(lst)

# n={}
# for i in numbers:
#     if i in n:
#         n[i]+=1
#     else:
#         n[i]=1
# print(n)
        
# d=[]
# for k,v in n.items():
#     if v>1:
#         d.append(k)
# print(d)


# for k,v in n.items():
#     if v>1:
#         print(f"{k}:{v}")

    
# s = "banana"
# n={}
# for i in s:
#     if i in n:
#         n[i]+=1
#     else:
#         n[i]=1
# print(n)


# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]

# c=set(a)
# d=set(b)

# h=c.intersection(d)
# print(list(h))

    
   
# num=153
# n=str(num)
# t=len(n)
# lst=[]
# for i in n:
#     lst.append(int(i)**t)
# print(lst)

# if sum(lst)==num:
#     print('arm num')
# else:
#     print('not a arm number')

# def arm():
#     num_str = input('enter no here: ')
#     num = int(num_str)
#     leng = len(num_str)
    
#     lst = []
#     for i in num_str:
#         lst.append(int(i) ** leng)
        
#     if sum(lst) == num:
#         print('Hasan')
#     else:
#         print('ali')

# arm()
 

# num = int(input('Enter number: '))

# def arm(n):
#     num_str = str(n)
#     leng = len(num_str)
#     lst = []
#     for i in num_str:
#         lst.append(int(i) ** leng)
        
#     if sum(lst) == n:
#         print('Hasan')
#     else:
#         print('ali')

# arm(num)



# def armstrong_check(num):
#     number = str(num)
#     len_num = len(number)

#     lst = []
#     for i in number:
#         lst.append(int(i) ** len_num)

#     if sum(lst) == num:
#         return 'yes'
#     else:
#         return 'no'
    
    
# "abcdef" -> "acebdf"
# "12345" -> "13524"

# s='12345' 
# even_lst=[]
# odd_lst=[]
# for i in range(0,len(s)):
#     if i%2==0:
#         even_lst.append(s[i])
#     elif i%2 !=0:
#         odd_lst.append(s[i])
# even_lst.extend(odd_lst)
# final=''.join(even_lst)
# print(final)


'''>>> keys = ['apple', 'banana', 'cherry']
>>> values = [10, 20, 30, 40]
>>> make_dict_from_elems_in_index(keys, values, 1) 
{'banana': 20}
>>> make_dict_from_elems_in_index(keys, values, -1) 
{'cherry': 40}'''

# def dat(data):
#     date=[]
#     suit_value={'S':1,'H':2,'D':3,'C':4}
#     rank_value={'A':1,'J':11,'Q':12,'K':13}
#     suit=data[-1]
#     rank=data[:-1]
#     if suit in suit_value:
#         date.append(int(suit_value[suit]))
#     if rank in rank_value:
#         date.append(int(rank_value[rank]))
#     else:
#         date.append(int(rank))
#     print(tuple((date)))

# dat('7H')
    
'''
>>> rotate_even([1,2,3,4,5,6],1)
[5,2,1,4,3,6]
>>> rotate_even([1,2,3,4,5,6,7,8],3)
[3,2,5,4,7,6,1,8]
'''

# def rotate_even(lst, k):
#   evens = lst[0::2]
#   if evens:
#     k = k % len(evens)
#     # Rotate right by slicing
#     rotated_evens = evens[-k:] + evens[:-k]

#     result = list(lst)
#     result[0::2] = rotated_evens
#     return result
#   return list(lst)


# s=rotate_even([1,2,3,4,5,6],1)
# print(s)

# s=[1,2,3,4,5,6]
# even=s[0::2]
# print(even)

# lst=[1,2,3,4,5,6,7]  
# even=[]
# for i in lst:
#     even.append(str(i))
#     print(type(i))
# print(even)   
    
# st=''.join(even)
# print(st)
    



# s='''
# 2
# Hello World
# Good Night'''
# vow='aeiouAEIOU'
# f=s.strip()
# for i in f:
#     if i not in vow:
#         z=f.replace(i,'#')
# print(z)
    

# s='hasan'
# for i in s:
#     if i=='a':
#         k=s.replace(i,'M')
# print(k)
       



# import random

# def guess_number():
#     num=int(input('enter Your number: '))
#     no=random.randint(1,5)
    
#     if num==no:
#         print('Congratulations You Guess Number')
#     else:
#         print('Retry')
#         print(f"Number was {no}")


# guess_number()




'''
>>> rotate_even([1,2,3,4,5,6],1)
[5,2,1,4,3,6]
>>> rotate_even([1,2,3,4,5,6,7,8],3)
[3,2,5,4,7,6,1,8]
'''


# def rotate_odd(lst:list,k:int):
#     odd_list=lst[1::2]
#     if lst:
#         k=k%len(odd_list)
#         rotate_list=odd_list[-k:]+odd_list[:-k]
#         lst[1::2]=rotate_list
#         return lst
#     else:
#         return 'Empty list'


# l=[1,2,3,4,5,6,7]
# s=rotate_odd(l,5)
# print(s)


# k=4
# s=[1,2,3,4,5,6,7]
# sum=[]

# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if not i==j:
#             if s[i]+s[j]==8:
#                 sum.append((i,j))
# print(tuple(sum))


# s=input('''
#     1
#     hello from me
#     welcome
     
#     ''')
# vw='aeiouAEIOU'
# l=s.strip()
# for i in s:
#     if i not in vw:
#         s=s.replace(i,'#')
# print(s)




        









 


        










# def rotate_even(lst,k):
#     even=lst[0::2]
#     if even:
#         k=k%len(even)
#         rotate_even=even[-k:]+even[:-k]
#         result=list(lst)
#         result[0::2]=rotate_even
#         return result
#     else:
#         return list(lst)
        
# l=[1,2,3,4,5,6]       

# s=rotate_even(l,2)
# print(s)

 
# def rotate_even(lst, k):
#   evens = lst[0::2]
#   if evens:
#     k = k % len(evens)
#     # Rotate right by slicing
#     rotated_evens = evens[-k:] + evens[:-k]

#     result = list(lst)
#     result[0::2] = rotated_evens
#     return result
#   return list(lst)


 

