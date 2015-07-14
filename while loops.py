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

s = ""
while True:
    input = raw_input("enter line: ")
    if input == ".":
        break
    s += input
print s

v = 0
while True:
    input = raw_input("enter line: ")
    if input == ".":
        break
    if not isdigit(input):
        print "not an int"
        continue
    v += int(input)

print v