import string

def encrypt(message):
    if len(message) <= 1:
        raise ValueError("Message must be at least 2 characters")
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    value_check = [abc.find(char) for idx, char in enumerate(message)]
    if -1 in value_check:
        raise ValueError("Message contains invalid characters")

    encrypted_message = "".join([abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(message)])
    return encrypted_message

def decrypt(encrypted_message):
    if len(encrypted_message) <= 1:
        raise ValueError("Message must be at least 2 characters")
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    value_check = [abc.find(char) for idx, char in enumerate(encrypted_message)]
    if -1 in value_check:
        raise ValueError("Message contains invalid characters")
    decrypted_message = "".join([abc[abc.find(char) - 1] if abc.find(char) - 1 > 0 else abc[-1] for idx, char in enumerate(encrypted_message)])
    return decrypted_message