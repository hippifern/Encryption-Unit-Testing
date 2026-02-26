import string

def encrypt(message, shift = 1):
    if len(message) <= 1:
        raise ValueError("Message must be at least 2 characters")
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    value_check = [abc.find(char) for idx, char in enumerate(message)]
    if -1 in value_check:
        raise ValueError("Message contains invalid characters")

    encrypted_message = "".join([abc[abc.find(char) + shift] if len(abc) > (abc.find(char) + shift) else abc[0] for idx, char in enumerate(message)])
    return encrypted_message

def decrypt(encrypted_message, shift = 1):
    if len(encrypted_message) <= 1:
        raise ValueError("Message must be at least 2 characters")
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    value_check = [abc.find(char) for idx, char in enumerate(encrypted_message)]
    if -1 in value_check:
        raise ValueError("Message contains invalid characters")
    decrypted_message = "".join([abc[abc.find(char) - shift] if abc.find(char) - shift >= 0 else abc[-1] for idx, char in enumerate(encrypted_message)])
    return decrypted_message