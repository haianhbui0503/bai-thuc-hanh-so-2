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

#Bai13
xau11_1 = [1, 2, 2, 4, 3, 4]
xau11_2 = [1, 5, 6, 8, 9, 4]
xau11 = sorted(xau11_1 + xau11_2)
print(xau11)

#Bai14


