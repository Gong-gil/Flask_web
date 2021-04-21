from passlib.hash import sha256_crypt

password = sha256_crypt.encrypt("password")
# 인코딩(암호화)하는 것
# 암호가 맞는지 확인은 해야한다. 

print(sha256_crypt.verify("password", password))
# 자체확인해서 맞는지 아닌지 확인은 해준다. = verify
# 반환값 = Ture

print(sha256_crypt.verify("password1", password))
# 반환값 = False