import rsa

public_file = open("rsa_keys/public_key.txt")
private_file = open("rsa_keys/private_key.txt")

public_content = public_file.read()
private_content = private_file.read()

public_key = rsa.PublicKey.load_pkcs1(public_content, 'PEM')
private_key = rsa.PrivateKey.load_pkcs1(private_content, 'PEM')


message = "Hello Again!"

message_bytes = message.encode('utf-8')
print(message_bytes)

message_encrypted = rsa.encrypt(message_bytes, public_key)
print(message_encrypted)

message_bytes_recovered = rsa.decrypt(message_encrypted, private_key)
print(message_bytes_recovered)

message_original = message_bytes_recovered.decode('utf-8')
print(message_original)
