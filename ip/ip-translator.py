#ip  = []
#ip.append(int(input("ip p1 ")))
#ip.append(int(input("ip p2 ")))
#ip.append(int(input("ip p3 ")))
#ip.append(int(input("ip p4 ")))
#inpMask = int(input("mask "))

ip = [10,100,200,200]
inpMask = 22

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

print(f"maska=[{mask[0]}.{mask[1]}.{mask[3]}.{mask[3]}]")
#print(antiMask)
print(f"ip sieci=[{netip[0]}.{netip[1]}.{netip[3]}.{netip[3]}]")
print(f"rozgłoszeńe=[{rozg[0]}.{rozg[1]}.{rozg[3]}.{rozg[3]}]")
print("liczba hostów",hostnumber)
print("zakres nie działa",zakr)
