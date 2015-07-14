__author__ = 'MegEllis'
hungry = 1
while hungry:
    print "yum"
    hungry = hungry - 1

i = 1
while i <= 10:
    print i
    i += 1

print i

s = ""
i = 0
while i < 10:
    i +=1
    s += "hi"

print s

#s = ""
#while True:
 #   input = raw_input("enter line: ")
  #  if input == ".":
   #     break
    #s += input
#print s

#v = 0
#while True:
    #input = raw_input("enter line: ")
    #if input == ".":
     #   break
    #if not isdigit(input):
     #   print "not an int"
      #  continue
    #v += int(input)

#print v

# nested loops

print "Times Table"
n = 0
m = 0
stop = 5
while n <= 5:
    print "%d %d %d" %(n, m, n*m)
    n += 1
    m +=1

print "\n"
print "Times Table"
n = 0
stop = 4
while n <= stop:
    m = 0
    while m <= stop:
        print "%d %d %d" %(n, m, n*m)
        m += 1
    n +=1