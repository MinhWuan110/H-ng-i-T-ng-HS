#Nguyễn Đặng Minh Quân 0306221159
#bai1
# PI=3.14
# Bankinh=float(input("nhap ban kinh hinh tron: "))
# ChuVi=2*PI*Bankinh
# DienTich=PI*Bankinh*Bankinh
# print("chu vi hinh tron la:",ChuVi)
# print("Dien tich hinh tron la:",DienTich)

#bai2
# Dongia=float(input("nhap don gia:"))
# Soluong=float(input("nhap so luong:"))
# Tongtientrcthue=Dongia*Soluong;
# tx1="Tong tien truoc thue: {}"#kieu khac
# print(tx1.format(Tongtientrcthue))
# print("Tien thue:",Tongtientrcthue*0.1)
# print("Tong tien sau thue:",Tongtientrcthue+Tongtientrcthue*0.1)

#bai3
# a=float(input("nhap so thu nhat:"))
# b=float(input("nhap so thu hai:"))
# c=float(input("nhap so thu Ba:"))
# trungbinhcong=(a+b+c)/3;
# txt1="Trung binh cong cua 3 so vua nhap la {} "
# print(txt1.format(trungbinhcong))

#bai4
# so=float(input("nhap mot so gom 3 chu so:"))
# a=int(so%10)
# b=int(so%100/10)
# c=int(so/100)
# trungbinhcong=(a+b+c)/3
# print("trung binh cong cua 3 chu so: ",trungbinhcong)

#bai5
# so=float(input("nhap vao so xe:"))
# a=int(so%10)
# b=int(so%100/10)
# c=int(so%1000/100)
# d=int(so%10000/1000)
# e=int(so/10000)
# kq=(a+b+c+d+e)%10
# print("so nut xe la: ",kq)

#bai6
# sothunhat=float(input("nhap vao so thu nhat:"))
# sothuhai=float(input("nhap so thu hai:"))
# hoanvi=0
# hoanvi=sothunhat
# sothunhat=sothuhai
# sothuhai=hoanvi
# print("sau khi hoan vi thi so thu nhat=",sothunhat,"so thu hai bang",sothuhai)

#bai7
# so=float(input("nhap vao mot so nguyen k :"))
# truoc=so+1
# sau=so-1
# print(sau)
# print(truoc)

#bai8
# import math
# a = float(input("Nhập vào số a: "))
# b = float(input("Nhập vào số b: "))
# c = float(input("Nhập vào số c: "))
# delta_check = b * b - 4 * a * c
# if delta_check < 0:
#     print("Phương trình không có nghiệm thực.")
# else:
#     delta = (-b + math.sqrt(delta_check)) / (2 * a)
#     print("Giá trị của delta là: ", delta)

#bai9
# import math
# x=float(input("nhap so x "))
# kq=(math.pow(x,8))-5+(math.fabs(x))# hàm trị tuyệt đôi trong python là fabs
# print("bieu thu x co gia tri la",kq)

#bai10
# so=float(input("nhap vao mot so thuc"))
# kq=int(so)
# print("phan nguyen cua so thuc vua nhap la:",kq)

#bai11
# kitu=input("nhap vao mot ki tu ")
# print("ki tu vua nhap la",kitu)

#bai12
# n=int(input("nhap mot so nguyen"))
# print(f"Bảng cửu chương của {n}:")
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

#bai13
# a=float(input("nhap so a "))
# b=float(input("nhap so b "))
# if a>b:
#     print(a)
# else:  #elif là else if 
#     print(b)


#bai14
# a=float(input("nhap so a"))
# b=float(input(" nhap so b"))
# if(a==0):
#     if(b==0):
#         print('PTVD')
#     else:
#         print("PTVN")
# else:
#     print(-b/a)

# #bai15
# diem=float(input("nhap diem tong ket"))
# if(diem>=5):
#     print("đạt")
# else:
#     print("không đạt")

#bai16
# def chanle(so):
#     if(so%2==0):
#         return print("là số chẵn")
#     else:
#         return print("là số lẽ")
        
# so=float(input("nhap so"))  
# chanle(so)

#bai17
# def ktraso(so):
#     if so<0:
#         return print("là số âm")
#     elif so>0:
#         return print("là số dương")
#     else:
#         return print("là số 0")
# number=float(input(" nhap so: "))
# ktraso(number)

#bai18
# a=float(input("nhap so thu nhat"))
# b=float(input("'nhap so thu hai: "))
# if a>b:
#     print("a lớn hơn b")
# elif a<b:
#      print("b lớn hơn a")
# else:
#      print("hai sôs bằng nhau ")

#bai19 không sử dụng hàm max
# a=float(input("nhap so thu nhat"))
# b=float(input("'nhap so thu hai: "))
# c=float(input("'nhap so thu ba: "))
# if a > b and a > c:
#     print("a là số lớn nhất")
# elif b > a and b > c:
#     print("b là số lớn nhất")
# else:
#     print("c là số lớn nhất")

#bai20 có sử dụng hàm min
# a = int(input("Nhập số nguyên a: "))
# b = int(input("Nhập số nguyên b: "))
# c = int(input("Nhập số nguyên c: "))
# d = int(input("Nhập số nguyên d: "))
# so = min(a, b, c, d)
# print("Số nhỏ nhất là:", so)

#bai21
# diemchuyencan = float(input("Nhập điểm chuyên cần: "))
# diemtrungbinh = float(input("Nhập điểm trung bình: "))
# diemthi = float(input("Nhập điểm thi: "))
# diemtongket = diemchuyencan * 0.1 + diemtrungbinh * 0.4 + diemthi * 0.5
# print("Điểm tổng kết:", diemtongket)
# if diemtongket >= 5:
#     print("Đạt")
# else:
#     print("Thi lại")







