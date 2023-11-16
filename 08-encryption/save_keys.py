import rsa

public_key, private_key = rsa.newkeys(1024)

public_file = open("rsa_keys/public_key.txt", "w")
public_file.write(public_key.save_pkcs1().decode('utf-8'))
public_file.close()

private_file = open("rsa_keys/private_key.txt", "w")
private_file.write(private_key.save_pkcs1().decode('utf-8'))
private_file.close()
