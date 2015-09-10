#BiMonBUPyCon - First meeting - 3/22/2015

#Iterables

#Example 1 - Loop through a string
#-----------------------------------------------------------------------------------------
string = 'Hello World'

for letter in string:
	print(letter)

print()	
stop = input('Moving onto Ex. 2...')
print()
#-----------------------------------------------------------------------------------------





#Example 2 - Loop through a list
#-----------------------------------------------------------------------------------------

number_list = [0,2,4,6,8]

for number in number_list:
	print(number)
	
print()	
stop = input('Moving onto Ex. 3...')
print()
#-----------------------------------------------------------------------------------------

	
	
	
	
	
#Example 3 - Use a loop to assign values in a list
#-----------------------------------------------------------------------------------------
number_squared = []

for number in number_list:
	number_squared.append(number**2)
print(number_squared)

print()	
stop = input('Moving onto Ex. 4...')
print()
#-----------------------------------------------------------------------------------------






#Example 4 - Basic while loop
#-----------------------------------------------------------------------------------------
start = 0
stop = 10
while start <=  !=
 stop:
	print(start)
	start += 1
	
print()	
stop = input('Moving onto Ex. 5...')
print()
#-----------------------------------------------------------------------------------------

	
	
	
	
	
#Example 5 - While not example
#-----------------------------------------------------------------------------------------
start = 0
fail = 10
while not start>10:
	print(start)
	start += 1	
	
print()	
stop = input('Moving onto Ex. 6...')
print()
#-----------------------------------------------------------------------------------------
	
	
	
	
	
	
	
#Example 6 - Do while loop
#-----------------------------------------------------------------------------------------
i=0
while 1:
	print(i)
	if i > 10:
		print('Breaking now')
		break
	else: i += 1
	
print()	
stop = input('Moving onto Ex. 7...')
print()
#-----------------------------------------------------------------------------------------







#Example 7 - Break in a for loop
#-----------------------------------------------------------------------------------------
for letter in 'Bi-Mon-BU-Py-Con':     
	if letter == 'U':
		break
	print('Current Letter : ', letter)


print()	
stop = input('Moving onto Ex. 8...')
print()
#-----------------------------------------------------------------------------------------








#Example 8 - Break in a for loop
for letter in 'Python':     
	if letter == 'h':
		continue
	print('Current Letter :', letter)






