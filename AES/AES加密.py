from cryptography.fernet import Fernet

# 生成AES密钥
key = Fernet.generate_key()

# 保存生成的密钥到文件
with open('keyfile', 'wb') as keyfile:
    keyfile.write(key)

cipher_suite = Fernet(key)

# 要加密的文本
text = "gogogo!"
text_bytes = text.encode('utf-8')

# 加密文本
encrypted_text = cipher_suite.encrypt(text_bytes)

# 打印结果
print(f"原始文本: {text}")
print(f"加密后: {encrypted_text}")
