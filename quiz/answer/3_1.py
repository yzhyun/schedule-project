import sys
sys.stdin=open("input.txt", "rt")

n=int(input())

bRslt=False
for i in range(n):
    str = input().upper()
    nCenter=len(str)//2
    #stttttts
    # print(nCenter)
    # print(str[0:nCenter], str[::-1][0:nCenter])
    if(str[0:nCenter] == str[::-1][0:nCenter]):
            print("#%d" % (i + 1), "YES")
    else:   print("#%d" %(i+1) , "NO"  )
    # if(bRslt):    print("#%d" %(i+1) , "YES" )
    # else :        print("#%d" %(i+1) , "NO"  )
