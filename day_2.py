name = "yuvraj"
num = 20
print(type(name))
#print(len(num))# it's show error because integer dont show len]
print(type(num))



#numeric datatype

x= 2;y=3.13;z=4+1j
print(type(x))
print(type(y))
print(type(z))



a=10
b=4

print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a%b)
print(a*b)
#logical and boolean
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)
print(x>5 and y<4)
print(x>6 or y<4)
print(not(x==y))


import math
print(math.ceil(2.43))
print(math.floor(3.43))
print(round(3.43))


number =[10,20,30]
name =["yuvraj","rishi","mihir"]
status =[ True,False,True]

data =["manish",278,True]
print(data)
print( name.append ("yuko")or name)
print(name.pop(1))


name =["yuvraj","rishi","mihir"]
asd =(" there are three people")
print(len(name))
print(len(asd))

#using in operator
asd =(" there are three people")
if "are" in asd:
    print("are is there")
else :
    print("are is not there")

lst =["hii everyone","good morning","what are you doing"]
result ="hii" in lst[1] or "hii" in lst[0]
print(result)
