#Q1
#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")
#full_name = last_name + " " + first_name
#print(full_name[::-1])

#Q2
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

#Q3
# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)

#Q4
# pi = 3.1415926535897931
# radius= 6.0
# volume= 4.0/3.0*pi* radius**3
# print('The volume of the sphere is: ',Volume)

#Q5
# base=float(input("input the base"))
# height=float(input("input the height of the sphere"))
# print('area of the sphere is: ',(1/2*base*height))

#Q6
# n=5
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')


#Q7
# word = input("Input a word : ")
# print ( word[::-1])

#Q8
# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x,end=' ')
# print("\n")

#Q9
# x,y=0,1

# while y<50:
#     print(y)
#     x,y = y,x+y

#Q10
# s = input("Input a string")
# d=l=0
# for char in s:
#     if char.isdigit():
#         d=d+1
#     elif char.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)