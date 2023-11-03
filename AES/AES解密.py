from cryptography.fernet import Fernet

# 从文件中读取密钥
with open('keyfile', 'rb') as keyfile:
    key = keyfile.read()

cipher_suite = Fernet(key)

# 加密后的文本，这应该是encrypt.py中打印的加密文本
encrypted_text = b'gAAAAABlREryXqtBymF39RDN-k_h0-8nOR0lMSbXbAMxva67GZkb7k5Msm5Y6lD76mvno6R_SGd26yFvWoKczS7dF0TJeP0t6w=='  # 用实际的加密文本替换这里的文本

# 解密文本
decrypted_text_bytes = cipher_suite.decrypt(encrypted_text)
decrypted_text = decrypted_text_bytes.decode('utf-8')

# 打印结果
print(f"加密后文本: {encrypted_text}")
print(f"解密后: {decrypted_text}")
