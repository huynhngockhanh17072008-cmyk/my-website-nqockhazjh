def tinh_luy_thua(co_so,so_mu=2):
    s=1
    i=1
    while i<=so_mu:
        s=s*co_so
        i+=1
    return s
try:
    n=int(input("nhập cơ số: "))
    i=int(input("nhập số mũ: "))
    print (n,"^",i,"=",tinh_luy_thua(n,i))
except:
    print("dữ liệu không hợp lệ")