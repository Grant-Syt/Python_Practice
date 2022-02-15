print("The following is a test:")

array = []
for x in range (0, 99):
    array.append(0x1234)
    
print ("size:")
print (len(array))
print ("index 0:")
print (hex(array[0]))

array.append(0x1234)

print ("size:")
print (len(array))
print ("last index:")
print (hex(array[len(array) - 1]))

i = 0
for x in range (0, 100, 2):
    temp = array[x]
    temp = temp << 16
    temp = temp | array[x + 1]
    array[i] = temp
    i += 1

for x in range (50, 100):
    array[x] = 0x0

print ("size:")
print (len(array))
print ("array:")

for x in range (0, 100):
    print ("index " + str(x) + ":")
    print (hex(array[x]))

print (array)
