f=open("user_details.txt","r")
a=f.readlines()
print(a)
user_names=[]
passcodes=[]
for i in a:
    passcodes.append(int(i.split()[-1]))
    user_names.append(i.split()[0])
print(user_names)
print(passcodes)
                
    