class ManajemenKaryawan:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    # Metode untuk menampilkan informasi karyawan
    def tampilkan_karyawan(self):
        print("=========Informasi Karyawan=========")
        print(f"Nama: {self.nama}")
        print(f"Jabatan: {self.jabatan}")
        print(f"Gaji: Rp {self.gaji}")
        print("===================================")

    # Metode untuk memberikan kenaikan gaji
    def bonus_gaji(self, persen_bonus):
        bonus = self.gaji * (persen_bonus / 100)
        total = self.gaji + bonus
        self.gaji = total
        print(f"Bonus tahunan untuk {self.nama}" )
        print(f"persentase Bonus: Rp {persen_bonus} atau Rp {bonus}")
        print(f"Total gaji setelah bonus: Rp {self.gaji}")
        print("===================================")

        #static method 
        @staticmethod
        def info_perusahaan():
            print("Perusahaan: PT. Maju Mundur")
            print("Alamat: Jl. Merdeka No. 123, Jakarta")
            print("Telepon: (021) 12345678")
            print()

    #=========================
    # INSTANSIASI OBJECT
    #=========================

karyawan1 = ManajemenKaryawan("Andi", "Manager", 10000000)
karyawan2 = ManajemenKaryawan("Budi", "Staff", 5000000)     

#=========================
# pemanggilan method
#=========================

karyawan1.tampilkan_karyawan()
karyawan2.tampilkan_karyawan()
karyawan1.bonus_gaji(10)
karyawan2.bonus_gaji(5)

#==========================
# pemanggilan static method
#========================== 

#==========================
# pemanggilan static method
#==========================

