__author__ = 'Dark-Knight'


f=open('bell.txt','w+',encoding='utf-8')
choice = ""
count = 0
while choice.upper() != 'Q':
        choice = input("Enter a string:")
        if choice.upper() != "Q":
            f.write(choice+"\n")
            count += 1
f.seek(0)
for i in range(count):
    print(f.readline().strip('\r\n'))
f.close()
