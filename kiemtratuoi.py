def kiem_tra_tuoi(n):
    if(n>=0 and n<=120):
        return True
    else:
        return False
try:
    n=int(input("nhập tuổi: "))
    print(kiem_tra_tuoi(n))
except: print("dữ liệu không hợp lệ")