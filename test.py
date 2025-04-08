from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# 1. 대칭키(128비트 = 16바이트) 생성
key = get_random_bytes(16)

# 2. 초기화 벡터 (IV) 생성 (CBC 모드에서 필요)
iv = get_random_bytes(16)

# 3. 평문 입력 (bytes로 변환, 패딩 필요)
plaintext = b"Hello AES, let's encrypt this!"
plaintext_padded = pad(plaintext, AES.block_size)  # 16바이트 단위로 맞추기

# 4. 암호화 객체 만들기 (AES-CBC 모드)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(plaintext_padded)

# 5. 복호화 흐름
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_padded = decipher.decrypt(ciphertext)
decrypted = unpad(decrypted_padded, AES.block_size)

# 6. 결과 출력
print(f"🔑 Key: {key.hex()}")
print(f"🧊 IV: {iv.hex()}")
print(f"📩 Plaintext: {plaintext}")
print(f"🧱 Ciphertext (hex): {ciphertext.hex()}")
print(f"📤 Decrypted: {decrypted}")

