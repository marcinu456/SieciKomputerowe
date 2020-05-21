#Marcin Pietrzak beta
#308025@uwr.edu.pl
#must instal by pip 'pip install mac-vendor-lookup'
from mac_vendor_lookup import MacLookup


thisdict={"not found mac vendor":0}
macarray=[]


# Using readlines() 
file1 = open('lista_mac.txt', 'r') 
Lines = file1.readlines() 
file1.close()

count = 0
# Strips the newline character 
for line in Lines: 
    if len(line) == 18:
        try:
            mac=MacLookup().lookup(line.strip())
            asd=line.strip()+" - "+mac
            # print(asd)
            macarray.append(asd)
            if mac not in thisdict:
                thisdict[mac] = 0
            if mac in thisdict:
                thisdict[mac] += 1
        except:
            thisdict["not found mac vendor"] += 1

# print(thisdict)
# print(macarray)

file1 = open('myfile.txt', 'w') 
name_mail="#Autor:Marcin Pietrzak\n#email:308025@uwr.edu.pl\n\n1.LIST\n\n"
file1.writelines(name_mail) 


for x in macarray:
    file1.writelines(x+"\n") 


file1.writelines("\n\n2.SUMMARY\n\n") 

for key, value in thisdict.items():
    L=key+":"+str(value)+"\n"
    file1.writelines(L) 




file1.close() 