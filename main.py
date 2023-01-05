import time

from Cryptodome import Random
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, DES3

from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Cipher import DES

messageToEncrypt = b'The feeling of soreness awakens me to a new day. I stretch my arms and arc my back The feeling of soreness awakens me to a new day.'

PadSize = 32


def AESEncryption():
    encInitTime = time.perf_counter()
    while True:
        try:
            key = get_random_bytes(16)
            break
        except ValueError:
            pass

    cipher = AES.new(key, AES.MODE_ECB)

    plainText = messageToEncrypt

    msg = cipher.encrypt(pad(plainText, PadSize))
    encFinTime = time.perf_counter()
    print(msg, "\n(Message Encrypted in AES in", encFinTime - encInitTime, "seconds )")

    decInitTime = time.perf_counter()
    decipher = AES.new(key, AES.MODE_ECB)
    cipherMsg = decipher.decrypt(msg)
    decFinTime = time.perf_counter()
    print(unpad(cipherMsg, PadSize), "\n(Message Decrypted in AES in", decFinTime - decInitTime, "seconds )")


initTime = time.perf_counter()
AESEncryption()
finTime = time.perf_counter()
print("total time elapsed : ", str(finTime - initTime) + "seconds\n\n")


def DES3Encryption():
    encInitTime = time.perf_counter()

    while True:
        try:
            key = get_random_bytes(16)
            break
        except ValueError:
            pass
    iv = Random.new().read(DES3.block_size)  # DES3.block_size==8
    cipher_encrypt = DES3.new(key, DES3.MODE_ECB)
    # padded with spaces so than len(plaintext) is multiple of 8
    encrypted_text = cipher_encrypt.encrypt(pad(messageToEncrypt, PadSize))
    encFinTime = time.perf_counter()
    print(encrypted_text, "\n(Message Encrypted in 3DES in", encFinTime - encInitTime, "seconds )")

    decInitTime = time.perf_counter()

    cipher_decrypt = DES3.new(key,
                              DES3.MODE_ECB)  # you can't reuse an object for encrypting or decrypting other data with the same key.
    decFinTime = time.perf_counter()
    print(unpad(cipher_decrypt.decrypt(encrypted_text), PadSize), "\n(Message Decrypted in 3DES in",
          decFinTime - decInitTime, "seconds )")


initTime = time.perf_counter()
DES3Encryption()
finTime = time.perf_counter()
print("total time elapsed : ", str(finTime - initTime) + "seconds\n\n")


def DESEncryption():
    encInitTime = time.perf_counter()

    while True:
        try:
            DesKey = get_random_bytes(8)
            break
        except ValueError:
            pass

    text1 = messageToEncrypt

    des = DES.new(DesKey, DES.MODE_ECB)

    encrypted_text = des.encrypt(pad(text1, PadSize))
    encFinTime = time.perf_counter()
    print(encrypted_text, "\n(Message Encrypted in DES in", encFinTime - encInitTime, "seconds )")

    decInitTime = time.perf_counter()
    decrypted_message = des.decrypt(encrypted_text)
    decFinTime = time.perf_counter()

    print(unpad(decrypted_message, PadSize), "\n(Message Decrypted in DES in", decFinTime - decInitTime,
          "seconds )")


initTime = time.perf_counter()
DESEncryption()
finTime = time.perf_counter()
print("total time elapsed : ", str(finTime - initTime) + "seconds\n\n")
