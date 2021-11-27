import rsa
import base64
# i = int(input())
# (pubkey, privkey) = rsa.newkeys(i) # 512  bits длина ключа, рекомендуется не меньше 1024
# # Save private and pub key
# priv_key_file = open("keys/private.pem", "w")
# priv_key_file.write(privkey.save_pkcs1().decode('utf-8'))
# priv_key_file.close()
# pub_key_file = open("keys/public.pem", "w")
# pub_key_file.write(pubkey.save_pkcs1().decode('utf-8'))
# pub_key_file.close()
#
# i *= 0.04
# print('Длина сообщения не должна превышать', int((i * 8) // 3 - 11), "символов" )
# message = input().encode('utf8')

def rsa_encode_p(message):
    message = message.encode('utf8')
    with open('keys/public.pem', mode='rb') as pubfile:
        keydata = pubfile.read()
    pubkey = rsa.PublicKey.load_pkcs1(keydata)

    crypto = rsa.encrypt(message, pubkey)  # Зашифровка
    crypto = base64.b64encode(crypto)
    crypto = crypto.decode('utf8')
    return(crypto)


def rsa_decode_p(crypto):
    crypto = crypto.encode('utf8')
    crypto = base64.b64decode(crypto)
    with open('keys/private.pem', mode='rb') as privatefile:
        keydata = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(keydata)

    message = rsa.decrypt(crypto, privkey)  # Расшифровка
    return(message.decode('utf8'))

# rsa_decode_p(input())

def rsa_generate_keys(bits):
    (pubkey, privkey) = rsa.newkeys(bits)
    priv_key_file = open("keys/private.pem", "w")
    priv_key_file.write(privkey.save_pkcs1().decode('utf-8'))
    priv_key_file.close()
    pub_key_file = open("keys/public.pem", "w")
    pub_key_file.write(pubkey.save_pkcs1().decode('utf-8'))
    pub_key_file.close()


# def rsa_encode(message):
#     with open('keys/public.pem', mode='rb') as privatefile:
#         keydata = privatefile.read()
#     print(1)
#     pubkey = rsa.PublicKey.load_pkcs1(keydata)
#     print(2)
#     crypto = rsa.encrypt(message, pubkey)
#     print(3)
#     print(type(crypto))
#     return crypto
#
# rsa_encode(input())

