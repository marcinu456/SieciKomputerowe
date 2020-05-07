#ip  = []
#ip.append(int(input("ip p1 ")))
#ip.append(int(input("ip p2 ")))
#ip.append(int(input("ip p3 ")))
#ip.append(int(input("ip p4 ")))
#inpMask = int(input("mask "))

def getmask(hosts):
    i = 1
    while(hosts >  2**i - 2 ):
        i+=1
    return 32-i

def getip(ip,argmask):
    inpMask = argmask

    hostnumber = 2**(32-inpMask) - 2

    wasfist = False

    mask = []
    antiMask = []
    netip = []
    rozg = []
    zakr = []
    for p in range(0,4):
        mask.append(0)
        maximum = 0
        if inpMask > 8:
            maximum = 8
            inpMask -= 8
        else:
            maximum = inpMask
            inpMask = 0
        
        for num in  range(0, maximum):
            num = 7 - num
            mask[p] += int(2**(num))
        antiMask.append(255 - mask[p])
        netip.append(mask[p] & ip[p] )
        rozg.append(antiMask[p] + netip[p])


        if mask[p] != 255 and p == 3:
            if not wasfist:
                zakr.append(str(netip[p] + 1) +"-"+ str(rozg[p]-1) )
                wasfist = True
            else:
                zakr.append(str(netip[p] ) +"-"+ str(rozg[p]-1))
        elif mask[p] != 255 : 
            if not wasfist:
                zakr.append(str(netip[p] + 1) +"-"+ str(rozg[p]) )
                wasfist = True
            else:
                zakr.append(str(netip[p] ) +"-"+ str(rozg[p]))
        

        else:
            zakr.append(str(netip[p]))

    # print("ip sieci",netip,"/",argmask)
    # print("maska",mask)
    # #print(antiMask)
    # print("rozgłoszeńe",rozg)
    # print("liczba hostów", hostnumber)
    #print("zakres nie działa",zakr)
    print(f"ip sieci=[{netip[0]}.{netip[1]}.{netip[2]}.{netip[3]}/{argmask}]")
    print(f"maska=[{mask[0]}.{mask[1]}.{mask[2]}.{mask[3]}]")
    print(f"rozgłoszeńe=[{rozg[0]}.{rozg[1]}.{rozg[2]}.{rozg[3]}]")
    print("liczba hostów",hostnumber)
    return netip, rozg, hostnumber



def getback(ip,argmask):
    inpMask = argmask

    hostnumber = 2**(32-inpMask) - 2

    wasfist = False

    mask = []
    antiMask = []
    netip = []
    rozg = []
    zakr = []
    for p in range(0,4):
        mask.append(0)
        maximum = 0
        if inpMask > 8:
            maximum = 8
            inpMask -= 8
        else:
            maximum = inpMask
            inpMask = 0
        
        for num in  range(0, maximum):
            num = 7 - num
            mask[p] += int(2**(num))
        antiMask.append(255 - mask[p])
        netip.append(mask[p] & ip[p] )
        rozg.append(antiMask[p] + netip[p])


        if mask[p] != 255 and p == 3:
            if not wasfist:
                zakr.append(str(netip[p] + 1) +"-"+ str(rozg[p]-1) )
                wasfist = True
            else:
                zakr.append(str(netip[p] ) +"-"+ str(rozg[p]-1))
        elif mask[p] != 255 : 
            if not wasfist:
                zakr.append(str(netip[p] + 1) +"-"+ str(rozg[p]) )
                wasfist = True
            else:
                zakr.append(str(netip[p] ) +"-"+ str(rozg[p]))
        

        else:
            zakr.append(str(netip[p]))


    print(f"ip sieci=[{netip[0]}.{netip[1]}.{netip[2]}.{netip[3]}/{argmask}]")
    print(f"maska=[{mask[0]}.{mask[1]}.{mask[2]}.{mask[3]}]")
    print(f"rozgłoszeńe=[{rozg[0]}.{rozg[1]}.{rozg[2]}.{rozg[3]}]")
    print("liczba hostów",hostnumber)
    # print("ip sieci",netip,"/",argmask)
    # print("maska",mask)
    # #print(antiMask)
    # print("rozgłoszeńe",rozg)
    # print("liczba hostów", hostnumber)
    # #print("zakres nie działa",zakr)
    return netip, rozg, hostnumber


# prz1
#ip = [192,168,1,0]
#hostnum = [40,40,20,4,4]
#mask = 24

# prz2
# ip = [10,1,1,0]
# hostnum = [60,40,40,4,4,4]
# mask = 24

# p3
ip = [10,1,1,0]
hostnum = [500,100,40,2,2,2]
mask = 22



print("całość")
ip, notip, absolutehostnumber = getip(ip,mask)
absolutehostnumber+=2

totalnethostnumber = 0
for host in hostnum:
    print()
    print(host)
    mask = getmask(host)
    notip, newip, nethostnumber = getip(ip,mask)
    ip = newip
    totalnethostnumber += nethostnumber + 2
    if ip[3] != 255:
        ip[3] += 1
    elif ip[2] != 255:
        ip[3] = 0
        ip[2] = ip[2] + 1
    elif ip[1] != 255:
        ip[3] = 0
        ip[2] = 0
        ip[1] = ip[1] + 1

print("\nreszta", ip)
getip(ip, getmask(absolutehostnumber - totalnethostnumber - 2))


print(absolutehostnumber, totalnethostnumber, absolutehostnumber -totalnethostnumber-2)