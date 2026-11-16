from database import akun_admin, akun_user
from utils import ambil_password

def login():
    print("")
    print("=== SILAHKAN LOGIN ===")
    username = input("Masukkan Username Akun : ")
    password = ambil_password("Masukkan Password Akun : ")
    
    if username in akun_admin and akun_admin[username] == password:
        return username, "admin"
    elif username in akun_user and akun_user[username] == password:
        return username, "user"
    else:
        print("\n❌ Username atau Password yang Anda Masukkan Salah!")
        return None, None

def registrasi():
    print("\n=== REGISTRASI AKUN USER BARU ===")
    user_baru = input("Masukkan Username Baru : ")
    if user_baru in akun_user or user_baru in akun_admin:
        print("❌ Username tersebut sudah terdaftar! Silakan gunakan nama lain.")
    else:
        pass_baru = ambil_password("Masukkan Password Baru : ")
        akun_user[user_baru] = pass_baru
        print(f"✅ Registrasi berhasil! Akun dengan username '{user_baru}' sekarang dapat digunakan untuk login.")