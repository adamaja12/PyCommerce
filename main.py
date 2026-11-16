
from auth import login, registrasi
from admin import tampilkan_menu_admin
from user import tampilkan_menu_user
from utils import menu_awal

def main():
    while True:
        print("")
        print("Selamat Datang di PyCommerce : Sistem E-Commerce. Silahkan Login Terlebih Dahulu!")
        print("============================================================================")
        
        menu_awal()
        
        pilihan_awal = input("Silahkan Pilih Opsi Menu (1-3) : ")
        
        if pilihan_awal == "1":
            username, role = login()
            if role == "admin":
                tampilkan_menu_admin()
            elif role == "user":
                tampilkan_menu_user(username)
                
        elif pilihan_awal == "2":
            registrasi()
            
        elif pilihan_awal == "3":
            print("✅ Berhasil Keluar dari Program!")
            break
        else:
            print("Opsi Menu yang Dimasukkan Tidak Valid/Terdeteksi")

if __name__ == "__main__":
    main()

print("APD Cintaku")