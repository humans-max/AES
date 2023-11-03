from cryptography.fernet import Fernet

# 生成AES密钥
key = Fernet.generate_key()

# 将生成的密钥写入文件
with open('keyfile.txt', 'wb') as keyfile:
    keyfile.write(key)
