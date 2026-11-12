 # def check(num1:int,num2:int):
#     if str(num1)[-1]==str(num2)[-1]:
#         return 'same'
#     else:
#         return 'different'
    


# s=''' hello this is hasan and tell me abiut your self 
# i hope u are good and most of time good'''
# v='AEIOUaeiou'
# lst=[]
# for i in s:
#     if i in v:
#         lst.append(i)
# print(lst[::-1])


# Problem Statement:
# Aapko ek integers ki list di gayi hai. Aapko list ko Rotate Right (Right Shift) karna hai by k steps.

# Yani list ke aakhri k elements aage aa jayenge aur baki elements piche chale jayenge.

# s=[1,2,3,4,3,4]
# k=2

# lst=s[-k:]+s[:-k]
# print(lst)

# s='hasan'
# m=s[1:-2].upper()+s[:3]+s[:]
# print(s)
# print(m)


# s='this is hasan from something'
# lst=s.split()
# print(lst)#['this', 'is', 'hasan', 'from', 'something']
# app=[]
# for i in lst:
#     i=i[0].upper()+i[1:-1]+i[-1].upper()
#     app.append(i)

# kl=" ".join(app)
# print(kl)


# Aapko ek string di gayi hai.
# Aapko usme se saare Duplicate characters ko remove karna hai aur original order maintain rakhna hai.
# text='programming'
# lst=[]
# for i in text:
#     lst.append(i)
# print(set(lst)) 


# Problem Statement:
# Aapko ek string di gayi hai. Aapko string ke sabse pehle NON-REPEATING (Unique)
# character ka index dhoondhna hai. Agar aisa koi character na ho, toh -1 return karna hai.

# Sample Input: "python 3.9 is fun"
# Expected Output: Vowels = 3, Consonants = 8

# txt='python 3.9 is fun'
# vowel='aeiouAEIOU'
# v=[]
# c=[]
# cons='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

# for i in txt:
#     if i in vowel:
#         v.append(i)
#     elif i in cons:
#         c.append(i)
# print(len(v))
# print(len(c))
        
# Question 2: Target Character Ki Index Position Nikalna
# Problem Statement:
# Ek string mein se kisi particular character (e.g., 'a') ki saari index positions ek list mein store karke print kijiye.

# Python
# Sample Input: text = "banana", target = "a"
# Expected Output: [1, 3, 5]

# Ek string me se saare Vowels (a, e, i, o, u) 
# ko remove karke baki string return kijiye. (Case-insensitive check karna hai).

# txt= "Python Programming"
# vow='aeiouAEIOU'
# v=[]
# for i in txt:
#     if i not in vow:
#         v.append(i)
# s=" ".join(v)
# print(s)

# Problem Statement:
# Ek numbers ki list mein Negative numbers ko left side aur Positive numbers ko right side shift kijiye, 
# par unka aapas ka order change nahi hona chahiye (Stable Sorting).
# hsn= [1, -2, 3, -4, -1, 6]

# conntnegative=[]
# countpositive=[]
# for i in hsn:
#     if i<0:
#         conntnegative.append(i)
#     elif i>0:
#         countpositive.append(i)
# # print(countpositive)
# # print(conntnegative)

# print(conntnegative+countpositive)

# Question 13: Loops & Index Tracking
# Problem Statement:
# Ek list mein wo saare elements dhundhiye jo apne Index Number ke barabar hain (i.e., nums[i] == i). 

# hsn= [10, 1, 5, 3, 8, 5]
# h=[]
# for idx,val in enumerate(hsn):
#     if idx==val:
#         h.append(val)
# print(h)
        
# Question 14: Frequency & Counting
# Problem Statement:
# String me kaun-kaun se characters sirf ek hi baar (Unique) aaye hain, unki ek list banayein.
# Sample="swiss"
# lst=list(Sample)
# v=[]
# for i in lst:
#     if i not in v:
#         v.append(i)
# print(v)

# Question 15: Search & Filter Logic
# Problem Statement:
# Ek string list me se unhi words ko filter karke nayi list banao
# jo Vowel se start hote hain AUR unka length even (2, 4, 6...) hai.

# Sample =["apple", "egg", "ice", "orange", "om"]
# vow='aeiouAEIOU'
# V=[]
# for i in Sample:
#     if i[0] in vow and len(i)%2==0:
#         V.append(i)
# print(V)      

# Problem Statement:
# Ek string di gayi hai. Continuous repeating characters ko unke count ke sath compress karke nayi string banayein.

 # Sample Input: s = "aabcccccaaa"
#s = "aabcccccaaa"
# v=[]
# s=[]
# nums = [0, 1, 0, 3, 12]
# for i in nums:
#     if i==0:
#         v.append(i)
#     elif i!=0:
#         s.append(i)
# print(s+v)

# Problem Statement:
# Ek sentence (words ki list ya string) di gayi hai. Unhi words ko filter karke nayi list mein daliye jo Palindrome hain (matlab aage aur piche se same read hote hain, e.g., "madam"), aur unka length 3 se bada hona chahiye.

# Sample Input: words = ["racecar", "noon", "cat", "madam", "kayak", "a"]
# words = ["racecar", "noon", "cat", "madam", "kayak", "a"]
# v=[]
# for i in words:
#     if i[:]==i[::-1] and len(i)>3:
#         v.append(i)
# print(v)         

# Problem Statement:
# Ek sentence (string) diya gaya hai. Un sabhi words ko count kijiye jo 
# Vowels (a, e, i, o, u) se start hote hain (Case-insensitive: uppercase aur lowercase dono count hone chahiye).

# sentence = "Apple is delicious and Elephant is huge"
# vow='aeiouAEIOU'
# v=[]
# lst=sentence.split()
# print(lst)
# for i in lst:
#     if i[0] in vow:
#         v.append(i)
# print(v)
# print(len(v))

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# lst=[]
# for i in list1:
#     if i in list2:
#         lst.append(i)
# print(lst)

# Level: Medium-Tricky | Topics: String Slicing + Loop / Join
# Problem Statement:
# Ek sentence diya gaya hai. Sentence ke words ka order same rakhna hai, 
# lekin har individual word ko reverse (ulta) kar dena hai.

# s = "python is fun"
# v=[]
# lst=s.split()
# for i in lst:
#     v.append(i[::-1])
# print(v)

# Write a Python function filter_words(words) that takes a list of strings and returns a new list containing only the words that meet both conditions:
# Starts with a vowel (a, e, i, o, u — case-insensitive)
# Has an even number of characters
     
# words = ["Apple", "orange", "elephant", "ice", "Umbrella", "ink", "Owl"]   

# def cal(words):
#     vow='aeiouAEIOU'
#     v=[]
#     for i in words:
#         if i[0] in vow and len(i)%2==0:
#             v.append(i)
#     return v

# s=cal(words)
# print(s)
    

# Write a Python function find_anagrams(words) that takes a list of strings
# and finds all pairs of words that are anagrams of each other (words made of the exact same letters in a different order).
# Return the pairs as a list of tuples.   
#words = ["cat", "dog", "tac", "god", "act", "python"]

# Problem 1: Multiplication Table Grid (2D Data / Combination)
# Write a Python program that prints a 5x5 multiplication table using nested loops.
# Goal:
# Outer loop holds the Row number (1 to 5).
# Inner loop holds the Column number (1 to 5) and multiplies it with the Row number.

# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j,end=' ') 
#     print()

# Problem 2: Find Common Characters Across Words (Comparing Strings)
# Write a Python function common_chars(word1, word2) that takes two words and
# returns a list of characters that appear in both words.
# Goal:
# Outer loop freezes each character of word1.
# Inner loop cycles through word2 to check if that frozen character exists there.

word1 = "apple"
word2 = "peach"

# def cal(word1:str,word2:str):
#     v=[]
#     for i in word1:
#         if i in word2:
#             if i not in v:
#                 v.append(i)
            
#     print(v)

# cal(word1,word2)      

# for i in range(1,5):
#     print("*"*i)
    
# for i in range(1,5):
#     for j in range(i):
#         print("*",end='')
#     print() 

# for i in range(5,0,-1):
#     print("*"*i)
    
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end='')
#     print()

# Problem 1: The Number Pyramid (Tracking Changing Values)
# Print a number triangle where the number printed matches the current row number.
# Goal: The outer loop controls the row (1 to 5), and the inner loop prints that row's number i times.
# Expected Output (n = 5):

'''
Problem 1: The Number Triangle (Printing Numbers Instead of Stars)
Goal: Build a growing number triangle where each row prints numbers starting from 1 up to the row number i.
💡 Hint: The inner loop needs to count from 1 up to i. What range() gives you numbers starting at 1 and ending at i?
Expected Output (n = 5):
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
    

'''Problem 2: Reverse Number Triangle
Numbers decrease as you go down, starting from 5 down to 1.

Expected Output:'''

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

'''Problem 3: Continuous Number Pyramid (Floyd's Triangle)
A single counter keeps increasing across all rows!

Expected Output:

Plaintext
1
2 3
4 5 6
7 8 9 10'''


# s='hasan'
# vow='aeiouAEIOU'
# even_ind=s[0::2]
# for i in even_ind:
#     if i not in vow:
#         return True
 
# def cal(s:str):
#     vow='aeiouAEIOU'
#     even_ind=s[0::2]
#     for i in even_ind:
#         if i not in vow:
#             return True

# import pyspark
 
# print(pyspark.__version__)
# from pyspark.sql import SparkSession

# spark = SparkSession.builder \
#     .appName("First Spark") \
#     .getOrCreate()

# print("Spark Started!")

# spark.stop()
    
# battery = 95
# while battery < 100:
#     print("Charging... Current:", battery)
#     battery = battery + 2
# print("Fully Charged!")

# def find_indices_of_element(l, elem):
#     """Find all indices of an element in a list.

#     Args:
#         l (list): The input list.
#         elem: The element to find.

#     Returns:
#         list: A list of indices where the element is found.

#     Examples:
#         >>> find_indices_of_element([1, 2, 3, 2, 4], 2)
#         [1, 3]
#         >>> find_indices_of_element(['a', 'b', 'a', 'c'], 'a')
#         [0, 2]
#     """


#l=[1,2,3,4,5,6,6,5,4,7,5,1,2,3,2,1,3,2,3]
# print(l.count(2))
# s=[]
# for e,i in enumerate(l):
#     if i==2:
#         s.append(e)
# print(s)



# l=[1,2,3,4,5,6,6,5,4,7,5,1,2,3,2,1,3,2,9,72] 
# print(len(l)) 
# h=[]
# if len(l)%2==0:
#     for i in range(0,len(l),2):
#         h.extend([l[i+1],l[i]])
#     print(h)

'''h='hasan'
m='ali'

h=[1,2,3,4,5]

for i in range(len(h)-1,len(h)-1-3,-1):
    h[i]=h[i]**2
print(h)'''
        




# h=check(41,30)
# print(h)

# def cal(n:int,f:int):
#     prts=[]
#     quotent=n//f
#     remender=n%f
#     for i in range(f):
#         if i<remender:
#             prts.append(quotent+1)
#         else:
#             prts.append(quotent)
#     return prts      
                
# h=cal(10,3)  
# print(h)


   
        
    
   



    







        


    
    
    
  
