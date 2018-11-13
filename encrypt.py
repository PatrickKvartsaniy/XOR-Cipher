text = "HELLO WORLD"
key = 15

# Шифрование
crypt = ""
for i in text:
	try:
		crypt += chr(ord(i)^ord(key))
	except TypeError:
		crypt += chr(ord(i)^key)

# A = 65 ASCII
# B = 66
# C = 67 ...


with open("crypt.txt","w") as file:
	file.write(crypt)

print(crypt)

# Расшифрование
decrypt = ""
'''
for j in crypt:
	try:
		decrypt += chr(ord(j)^ord(key))
	except TypeError:
		decrypt += chr(ord(j)^key)
'''
with open("crypt.txt","r") as file:
	for j in file.read():
		try:
			decrypt += chr(ord(j)^ord(key))
		except TypeError:
			decrypt += chr(ord(j)^key)
print(decrypt)

# XOR исключающее ИЛИ

# XOR:
# 1 ^ 1 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 0 ^ 0 = 0

x = 10; y = 5

# x = 1010
# y = 0101
x = x ^ y # 1010 ^ 0101 = 1111 
y = x ^ y # 1111 ^ 0101 = 1010 
x = x ^ y # 1111 ^ 1010 = 0101 
# x = 0101
# y = 1010

# Шифр Цезаря с ключом 1: IFMMP XPSME
# XOR Шифрование с ключом 1: IDMMN!VNSME