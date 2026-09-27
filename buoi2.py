#Bai1
a = "Xin chao moi nguoi"
print("Độ dài chuỗi:", len(a))
x = a.count("x")
i = a.count("i")
print("Số ký tự x trong xâu là:", x)
print("Số ký tự i trong xâu là:", i)

#Bai2
def is_palindrome(string):
  return string == string[::-1]
print(is_palindrome("madam"))
print(is_palindrome("hello"))

#Bai3
chuoi = input("Nhập chuỗi: ").lower()
nguyen_am= "aeiou"
demnguyenam = 0
demphuam = 0
for i in chuoi:
  if i.isalpha():
    if i in nguyen_am:
      demnguyenam += 1
    else:
      demphuam += 1
print ("số lượng nguyên âm:", demnguyenam)
print ("số lượng phụ âm:", demphuam)

#Bai4
cau = input("nhập câu: ")
cau.title()

#Bai5
chuoi5 = "Python là một ngôn ngữ lập trình"
chuoi5.replace("Python","AI")

#Bai6
chuoi6 = "hoc lap trinh"
chuoi6_1= chuoi6.split()
print(chuoi6_1)
print(chuoi6_1.join())

#Bai7
chuoi7 = "hoc lap trinh"
print(len(chuoi7.split()))

#Bai8
n = int (input("Nhập số lượng phấn tử: "))
k = []
for i in range(n):
  x = int(input(f"Nhập số thứ {i+1}: "))
  k.append(x)
  a += x
b = x/n
print("Tổng:", a)
print("Trung bình:", b)
print(max(k))

#Bai9
xau9 = [1, 2, 3, 4, 6, 2, 4, 6]
print(list(set(xau9)))

#Bai10
xau10 = ["python", "AI", "Java"]
print(list(reversed(xau10)))

#Bai11
day_so_11 = [int(x) for x in input("Nhập dãy số:").split(',')]
tong = 0
for x in day_so_11:
  if x %2 == 0:
    tong += x
print("Tong cac so chan:", tong)

#Bai12
day_so_12 = input("Nhập dãy số:").split(',')
dem = 0
for x in day_so_12:
  dem_nhieu_nhat = day_so_12.count(x)
  if dem_nhieu_nhat > dem:
    dem = dem_nhieu_nhat
print(f"Phần tử xuất hiện nhiều nhất: {x} và số lần xuất hiện của nó {dem}")
  
#Bai13
xau11_1 = [1, 2, 2, 4, 3, 4]
xau11_2 = [1, 5, 6, 8, 9, 4]
xau11 = sorted(xau11_1 + xau11_2)
print(xau11)

#Bai14
danh_sach_truoc = ("Nhập dãy số:").split(',')
danh_sach_sau = [ x for x in danh_sach_truoc if x>10 ]
print("Danh sách các số lớn hơn 10:", danh_sach_sau)

#Bai15
van_ban = input("Nhập văn bản: ")
for dau_cau in ['.', ',', '!', '?']:
  van_ban = van_ban.replace(dau_cau, "")
van_ban = van_ban.lower()
cac_tu = van_ban.split()
dem = {}
for tu in cac_tu:
  if tu in dem:
    dem[tu] += 1
  else:
    dem[tu] = 1
sap_xep = sorted(dem.items(), key=lambda item: item[1], reverse=True)
print("\nDanh sách từ sắp xếp theo tần suất xuất hiện giảm dần:")
for tu, so_lan in sap_xep:
    print(f"'{tu}': {so_lan} lần")




