from cryptography.fernet import Fernet

# Функция для генерации и сохранения ключа
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Ключ шифрования сгенерирован и сохранён в 'secret.key'.")

# Функция для загрузки ключа
def load_key():
    return open("secret.key", "rb").read()

# Функция для шифрования сообщения
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Функция для расшифровки сообщения
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Пример использования
if name == "main":
    generate_key()  # сгенерировать ключ, выполните только один раз

    original_message = "Привет, это секретное сообщение!"
    print(f"Оригинальное сообщение: {original_message}")

    encrypted = encrypt_message(original_message)
    print(f"Зашифрованное сообщение: {encrypted}")

    decrypted = decrypt_message(encrypted)
    print(f"Расшифрованное сообщение: {decrypted}")
