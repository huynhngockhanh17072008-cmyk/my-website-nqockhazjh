def ktsnt(n):
    i=2
    while (i<n) and (n%i !=0): i +=1
    if i==n: return False
    else : return True
try:
    n=int(input("nhập một số: "))
    i=2
    while i<=n:
        if ktsnt(i): print (i, end=" ")
        i+=1
except:
    print("dữ liệu không đúng")