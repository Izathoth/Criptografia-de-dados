import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from cryptography.fernet import Fernet
import os
import datetime

def create_directories():
    os.makedirs("Arquivos_Criptografados", exist_ok=True)
    os.makedirs("Arquivos_Descriptografados", exist_ok=True)
    os.makedirs("Registro", exist_ok=True)

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("secret.key"):
        generate_key()
    return open("secret.key", "rb").read()

def log_operation(operation, file_name):
    with open("Registro/operacoes.log", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {operation} - {file_name}\n")

def encrypt_message():
    try:
        message = entry_message.get()
        key = load_key()
        cipher_suite = Fernet(key)
        encrypted_message = cipher_suite.encrypt(message.encode())
        entry_encrypted.delete(0, tk.END)
        entry_encrypted.insert(0, encrypted_message.decode())
        log_operation("Criptografada", "Mensagem")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def decrypt_message():
    try:
        encrypted_message = entry_encrypted.get()
        key = load_key()
        cipher_suite = Fernet(key)
        decrypted_message = cipher_suite.decrypt(encrypted_message.encode())
        entry_decrypted.delete(0, tk.END)
        entry_decrypted.insert(0, decrypted_message.decode())
        log_operation("Descriptografada", "Mensagem")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def encrypt_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        key = load_key()
        cipher_suite = Fernet(key)

        with open(file_path, "rb") as file:
            file_data = file.read()

        encrypted_data = cipher_suite.encrypt(file_data)
        encrypted_file_path = os.path.join("Arquivos_Criptografados", os.path.basename(file_path) + ".enc")

        with open(encrypted_file_path, "wb") as file:
            file.write(encrypted_data)

        log_operation("Criptografado", os.path.basename(file_path))
        messagebox.showinfo("Sucesso", f"Arquivo criptografado e salvo em: {encrypted_file_path}")

def decrypt_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        key = load_key()
        cipher_suite = Fernet(key)

        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = cipher_suite.decrypt(encrypted_data)
        decrypted_file_path = os.path.join("Arquivos_Descriptografados", os.path.basename(file_path[:-4]))

        with open(decrypted_file_path, "wb") as file:
            file.write(decrypted_data)

        log_operation("Descriptografado", os.path.basename(file_path))
        messagebox.showinfo("Sucesso", f"Arquivo descriptografado e salvo em: {decrypted_file_path}")

def view_log():
    try:
        with open("Registro/operacoes.log", "r") as log_file:
            log_content = log_file.read()
        log_window = tk.Toplevel()
        log_window.title("Registro de Operações")
        log_window.geometry("400x300")
        log_text = scrolledtext.ScrolledText(log_window, wrap=tk.WORD)
        log_text.insert(tk.END, log_content)
        log_text.config(state=tk.DISABLED)
        log_text.pack(padx=10, pady=10)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Nenhum registro encontrado.")

create_directories()
load_key()

root = tk.Tk()
root.title("Criptografia de Dados")
root.geometry("400x600")
root.config(bg="#f0f0f0")

frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
frame.pack(pady=20)

label_message = tk.Label(frame, text="Mensagem:", bg="#ffffff")
label_message.pack(anchor="w")
entry_message = tk.Entry(frame, width=50)
entry_message.pack(pady=5)

button_encrypt = tk.Button(frame, text="Criptografar Mensagem", command=encrypt_message, bg="#4CAF50", fg="white")
button_encrypt.pack(pady=10)

label_encrypted = tk.Label(frame, text="Mensagem Criptografada:", bg="#ffffff")
label_encrypted.pack(anchor="w")
entry_encrypted = tk.Entry(frame, width=50)
entry_encrypted.pack(pady=5)

button_decrypt = tk.Button(frame, text="Descriptografar Mensagem", command=decrypt_message, bg="#2196F3", fg="white")
button_decrypt.pack(pady=10)

button_encrypt_file = tk.Button(frame, text="Criptografar Arquivo", command=encrypt_file, bg="#FF9800", fg="white")
button_encrypt_file.pack(pady=10)

button_decrypt_file = tk.Button(frame, text="Descriptografar Arquivo", command=decrypt_file, bg="#f44336", fg="white")
button_decrypt_file.pack(pady=10)

button_view_log = tk.Button(frame, text="Ver Registro de Operações", command=view_log, bg="#9C27B0", fg="white")
button_view_log.pack(pady=10)

root.mainloop()