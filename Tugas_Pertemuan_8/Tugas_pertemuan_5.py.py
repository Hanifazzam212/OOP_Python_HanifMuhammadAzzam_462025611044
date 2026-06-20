class DompetDigital:
    def __init__(self, nama_pengguna, id_pengguna, pin, saldo):
        self.nama = nama_pengguna
        self.id_pengguna = id_pengguna
        self.pin = pin
        self.saldo = saldo

    def get_nama_pengguna(self):
        return self.nama
    
    def get_id_pengguna(self):
        return self.id_pengguna 
    
 #method validsai untuk melihat saldo 
    def cek_saldo(self, pin):
        if pin == self.pin:
            return f"Saldo Anda : {self.saldo}"
        else:
            return "PIN salah. Akses ditolak."
        
        if jumlah > self.saldo:
            return "Saldo tidak cukup untuk melakukan transaksi."   
        
        else:
            self.saldo -= jumlah
            return f"Transaksi berhasil. Sisa saldo Anda : {self.saldo}"
        
#method validasi untuk mengubah pin 
    def ubah_pin(self, pin_lama, pin_baru):
        if pin_lama == self.pin:
            self.pin = pin_baru
            return "PIN berhasil diubah."
        else:
            return "PIN lama salah. PIN tidak diubah."
        
#==================================
# INSTANSIASI OBJEK 
#==================================

akun1 = DompetDigital("Azzam", "Azzam123", "1234", 1000000)

#================================
# pengujian Getter
#===============================

print("=== DATA PENGGUNA ===   ")
print(f"Nama: {akun1.get_nama_pengguna()}")
print(f"ID Pengguna: {akun1.get_id_pengguna()}")

#================================
# PENGUJIAN VALIDASI 
#================================

print("\n=== CEK SALDO ===")    
print(akun1.cek_saldo("1234"))  # PIN benar     
print(akun1.cek_saldo("0000"))  # PIN salah

print("\n=== UBAH PIN ===")
print(akun1.ubah_pin("1234", "5678"))  # PIN lama benar
print(akun1.ubah_pin("0000", "5678"))  # PIN lama salah 

print("\n=== CEK SALDO SETELAH UBAH PIN ===")
print(akun1.cek_saldo("5678"))  # PIN baru benar
print(akun1.cek_saldo("1234"))  # PIN lama salah    

