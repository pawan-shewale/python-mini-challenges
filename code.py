# --------------
#Code starts here

#print("enter a number:")
#input_string="NAYAN"



#new_string=input_string()

def palindrome(num):
    num=str(num)
    while ((num[::-1]==num)==False):
        num=int(num)
        num=num+1
        num=str(num)
    else:
        if(len(num)==1):
            num = int(num)
            num = num+1
        return int(num)
    #break
print(palindrome(10201))
print(palindrome(123))
print(palindrome(8))
print(palindrome(12))
print(palindrome(13456))


     



# --------------
#Code starts here

def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)

#print(a_scramble("Tom Marvolo Riddle","Voldemort"))
#print("--------")
#print(a_scramble("ticket","chat"))
#print("--------")
print(a_scramble("labratory","Bat"))
print("--------")
print(a_scramble("baby shower","shows"))
print("--------")
print(a_scramble("eatcher","teacher"))


# --------------
#Code starts here

import math 
  
# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def check_fib(num): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4) 
     
print(check_fib(145))
print(check_fib(377))
        



# --------------
#Code starts here
def compress(word):
    count=1
    length=""
    word = word.lower()
    if len(word)>1:
        word=word+"$"
        for i in range(1,len(word)):
            if word[i-1]==word[i]:
                count+=1
                #print("1st Output",word[i-1],count)
                #print("---")
                continue
            else :
                #if(word[i-1] not in length):
                length += (word[i-1]+str(count))
                count=1
                #print("Length",word[i-1],length)
            if(word[i-1] not in length):
                length += (word[i-1]+str(count))
        
            
    else:
        i=0
        length += (word[i]+str(count))

    return(length)

print(compress("xxcccdex"))
print("---------")
print(compress('Ss'))
print("---------")
print(compress('ssggtts'))
print("---------")
print(compress('banana'))


# --------------
#Code starts here

def k_distinct(string,k):
    string = str(string).lower()
    alist = []
    for x in string:
        
        if x not in alist:
            alist.append(x)
    if(len(alist)==k):
        return True
    else:
        return False

k_distinct('Messoptamia',8)
k_distinct('SUBBOOKKEEPER',8)



