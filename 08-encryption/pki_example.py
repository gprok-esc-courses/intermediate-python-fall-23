import rsa

public_key, private_key = rsa.newkeys(1024)

print(public_key)
print(private_key)

message = "Hello World!"

message_bytes = message.encode('utf-8')
print(message_bytes)

message_encrypted = rsa.encrypt(message_bytes, public_key)
print(message_encrypted)

message_bytes_recovered = rsa.decrypt(message_encrypted, private_key)
print(message_bytes_recovered)

message_original = message_bytes_recovered.decode('utf-8')
print(message_original)
