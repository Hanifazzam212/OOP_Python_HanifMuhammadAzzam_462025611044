import sys
from abc import ABC, abstractmethod
from datetime import datetime


# ==========================================
# 1. ROBUSTNESS: CUSTOM EXCEPTION
# ==========================================
class InvalidDataError(Exception):
    """Custom exception digunakan untuk menangani kesalahan input domain pemancingan"""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


# ==========================================
# 2. ABSTRACTION & POLYMORPHISM BASE CLASS
# ==========================================
class LayananPemancingan(ABC):
    """Abstract Base Class sebagai blueprint semua jenis layanan"""

    @abstractmethod
    def hitung_biaya(self) -> float:
        """Polymorphic method untuk kalkulasi biaya layanan"""
        pass

    @abstractmethod
    def get_detail_layanan(self) -> str:
        """Polymorphic method untuk rincian deskripsi layanan"""
        pass


# ==========================================
# 3. INHERITANCE & ENCAPSULATION (USER SYSTEM)
# ==========================================
class User:
    """Superclass untuk pengguna sistem"""

    def __init__(self, id_user: str, nama: str):
        # Encapsulation: Protected Attributes
        self._id_user = id_user
        self._nama = nama

    # Instance Methods & Encapsulation Getters
    def get_id_user(self) -> str:
        return self._id_user

    def get_nama(self) -> str:
        return self._nama

    # Magic Method __str__
    def __str__(self) -> str:
        return f"User ID: {self._id_user} | Nama: {self._nama}"


class Pelanggan(User):
    """Subclass Pelanggan menuruni sifat User"""

    def __init__(self, id_user: str, nama: str, nomor_telepon: str):
        super().__init__(id_user, nama)
        # Encapsulation: Private Attribute
        self.__nomor_telepon = nomor_telepon

    def get_nomor_telepon(self) -> str:
        return self.__nomor_telepon

    def set_nomor_telepon(self, nomor_telepon: str):
        if len(nomor_telepon) < 10:
            raise InvalidDataError("Nomor telepon tidak valid! Minimal 10 digit.")
        self.__nomor_telepon = nomor_telepon

    # Overriding Magic Method __str__
    def __str__(self) -> str:
        return f"[Pelanggan] {self._nama} ({self._id_user}) - HP: {self.__nomor_telepon}"


class Admin(User):
    """Subclass Admin menuruni sifat User"""

    def __init__(self, id_user: str, nama: str, role: str):
        super().__init__(id_user, nama)
        self.__role = role

    def get_role(self) -> str:
        return self.__role

    def __str__(self) -> str:
        return f"[Admin] {self._nama} ({self._id_user}) - Role: {self.__role}"


# ==========================================
# 4. CONCRETE SERVICES (POLYMORPHISM & INHERITANCE)
# ==========================================
class ReservasiLapak(LayananPemancingan):
    """Sewa tempat/lapak pemancingan berbasis durasi"""

    TARIF_PER_JAM = 25000.0

    def __init__(self, nomor_lapak: int, durasi_jam: int):
        if nomor_lapak <= 0 or durasi_jam <= 0:
            raise InvalidDataError("Nomor lapak dan durasi jam harus lebih dari 0!")
        self.__nomor_lapak = nomor_lapak
        self.__durasi_jam = durasi_jam

    # Implementation Polymorphism 1
    def hitung_biaya(self) -> float:
        return self.__durasi_jam * self.TARIF_PER_JAM

    # Implementation Polymorphism 2
    def get_detail_layanan(self) -> str:
        return f"Sewa Lapak #{self.__nomor_lapak} ({self.__durasi_jam} Jam)"


class PenyewaanAlat(LayananPemancingan):
    """Sewa alat pancing berbasis unit"""

    def __init__(self, nama_alat: str, harga_sewa_unit: float, jumlah: int):
        if harga_sewa_unit < 0 or jumlah <= 0:
            raise InvalidDataError("Harga sewa tidak boleh negatif dan jumlah harus > 0!")
        self.__nama_alat = nama_alat
        self.__harga_sewa_unit = harga_sewa_unit
        self.__jumlah = jumlah

    # Implementation Polymorphism 1
    def hitung_biaya(self) -> float:
        return self.__harga_sewa_unit * self.__jumlah

    # Implementation Polymorphism 2
    def get_detail_layanan(self) -> str:
        return f"Sewa Alat: {self.__nama_alat} x{self.__jumlah} (@Rp {self.__harga_sewa_unit:,.0f})"


class HasilTangkapan:
    """Modul pencatatan hasil tangkapan ikan"""

    def __init__(self, jenis_ikan: str, berat_kg: float):
        if berat_kg <= 0:
            raise InvalidDataError("Berat ikan harus lebih dari 0 kg!")
        self.__jenis_ikan = jenis_ikan
        self.__berat_kg = berat_kg

    def get_jenis(self) -> str:
        return self.__jenis_ikan

    def get_berat(self) -> float:
        return self.__berat_kg

    def __str__(self) -> str:
        return f"{self.__jenis_ikan} ({self.__berat_kg} kg)"


# ==========================================
# 5. BILLING & TRANSAKSI SYSTEM
# ==========================================
class Transaksi:
    """Kelas pengelola checkout & pembuatan nota tagihan"""

    def __init__(self, id_transaksi: str, pelanggan: Pelanggan):
        self.__id_transaksi = id_transaksi
        self.__pelanggan = pelanggan
        self.__daftar_layanan = []
        self.__daftar_tangkapan = []
        self.__waktu_transaksi = datetime.now()

    def tambah_layanan(self, layanan: LayananPemancingan):
        self.__daftar_layanan.append(layanan)

    def tambah_tangkapan(self, tangkapan: HasilTangkapan):
        self.__daftar_tangkapan.append(tangkapan)

    def hitung_total_biaya(self) -> float:
        """Polymorphism secara dinamis memanggil hitung_biaya() objek anak"""
        return sum(layanan.hitung_biaya() for layanan in self.__daftar_layanan)

    # ADVANCED METHOD: STATIC METHOD
    @staticmethod
    def format_rupiah(nominal: float) -> str:
        """Utility function tanpa ketergantungan pada instance"""
        return f"Rp {nominal:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    # MAGIC METHOD: __len__ (Jumlah item layanan yang disewa)
    def __len__(self) -> int:
        return len(self.__daftar_layanan)

    def cetak_nota(self):
        total = self.hitung_total_biaya()
        print("\n" + "=" * 50)
        print("          SISTEM PEMANCINGAN KALIMANTAN          ")
        print("                 NOTA TRANSAKSI                  ")
        print("=" * 50)
        print(f"ID Transaksi : {self.__id_transaksi}")
        print(f"Waktu        : {self.__waktu_transaksi.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Pelanggan    : {self.__pelanggan.get_nama()}")
        print(f"No. HP       : {self.__pelanggan.get_nomor_telepon()}")
        print("-" * 50)
        print("Rincian Layanan:")
        if not self.__daftar_layanan:
            print("  (Tidak ada layanan yang dipilih)")
        else:
            for idx, item in enumerate(self.__daftar_layanan, 1):
                biaya = item.hitung_biaya()
                print(f"  {idx}. {item.get_detail_layanan():<33} = {self.format_rupiah(biaya)}")

        print("-" * 50)
        print("Hasil Tangkapan Ikan Hari Ini:")
        if not self.__daftar_tangkapan:
            print("  (Belum ada data tangkapan)")
        else:
            for idx, t in enumerate(self.__daftar_tangkapan, 1):
                print(f"  {idx}. {str(t)}")

        print("=" * 50)
        print(f"TOTAL TAGIHAN  : {self.format_rupiah(total)}")
        print("STATUS PAYMENT : LUNAS")
        print("=" * 50 + "\n")


# ==========================================
# 6. INTERACTIVE CLI APPLICATION (INPUT/OUTPUT)
# ==========================================
class MainApp:
    """Driver class untuk mengontrol antarmuka interaktif pengguna"""

    def __init__(self):
        self.__admin = Admin("ADM001", "Pak Hanif Azzam", "Manager Operasional")
        self.__pelanggan = None
        self.__transaksi_aktif = None

    def registrasi_pelanggan(self):
        print("\n--- Registrasi Pelanggan Baru ---")
        id_pel = input("Masukkan ID Pelanggan (misal: PLG01): ").strip()
        nama = input("Masukkan Nama Pelanggan: ").strip()
        hp = input("Masukkan No. Telepon: ").strip()

        if not id_pel or not nama:
            raise InvalidDataError("ID dan Nama tidak boleh kosong!")

        self.__pelanggan = Pelanggan(id_pel, nama, hp)
        self.__transaksi_aktif = Transaksi("TRX-" + datetime.now().strftime("%d%m%H%M"), self.__pelanggan)
        print(f"\n[OK] Pelanggan berhasil terdaftar: {self.__pelanggan}")

    def menu_reservasi_lapak(self):
        print("\n--- Reservasi Lapak Pemancingan ---")
        print(f"Tarif Standar Lapak: {Transaksi.format_rupiah(ReservasiLapak.TARIF_PER_JAM)}/Jam")
        lapak = int(input("Nomor Lapak Pemancingan (1-20): "))
        durasi = int(input("Durasi Sewa (Jam): "))

        reservasi = ReservasiLapak(lapak, durasi)
        self.__transaksi_aktif.tambah_layanan(reservasi)
        print(f"[OK] Reservasi berhasil ditambahkan! Subtotal: {Transaksi.format_rupiah(reservasi.hitung_biaya())}")

    def menu_sewa_alat(self):
        print("\n--- Penyewaan Alat Pancing ---")
        print("Daftar Alat Pancing Tersedia:")
        print("1. Joran Carbon Shimano (Rp 20.000/unit)")
        print("2. Reel Pflueger Spinning (Rp 15.000/unit)")
        print("3. Set Pancing Lengkap + Umban (Rp 35.000/unit)")
        pilihan = input("Pilih Jenis Alat (1-3): ").strip()

        alat_map = {
            "1": ("Joran Carbon Shimano", 20000.0),
            "2": ("Reel Pflueger Spinning", 15000.0),
            "3": ("Set Pancing Lengkap", 35000.0),
        }

        if pilihan not in alat_map:
            raise InvalidDataError("Pilihan item alat pancing tidak valid!")

        nama_alat, harga = alat_map[pilihan]
        jumlah = int(input(f"Jumlah unit '{nama_alat}' yang disewa: "))

        sewa = PenyewaanAlat(nama_alat, harga, jumlah)
        self.__transaksi_aktif.tambah_layanan(sewa)
        print(f"[OK] Penyewaan berhasil! Subtotal: {Transaksi.format_rupiah(sewa.hitung_biaya())}")

    def menu_pencatatan_tangkapan(self):
        print("\n--- Pencatatan Hasil Tangkapan Ikan ---")
        jenis = input("Jenis Ikan (misal: Patin, Haruan, Gurame): ").strip()
        berat = float(input("Berat Total Tangkapan (Kg): "))

        tangkapan = HasilTangkapan(jenis, berat)
        self.__transaksi_aktif.tambah_tangkapan(tangkapan)
        print(f"[OK] Tangkapan tercatat: {tangkapan}")

    def run(self):
        print("=" * 55)
        print("   SISTEM MANAJEMEN PEMANCINGAN DAERAH KALIMANTAN    ")
        print(f"   Petugas Admin On-Duty: {self.__admin.get_nama()}")
        print("=" * 55)

        # Wajib registrasi awal
        while self.__pelanggan is None:
            try:
                self.registrasi_pelanggan()
            except InvalidDataError as e:
                print(f"[ERROR] {e.message}")
            except Exception as e:
                print(f"[ERROR System] Error input: {e}")

        # Main Loop Menu Terminal Interaktif
        while True:
            print("\n================ MENU UTAMA ================")
            print("1. Tambah Reservasi Lapak")
            print("2. Sewa Alat Pancing")
            print("3. Catat Hasil Tangkapan Ikan")
            print("4. Cek Total & Cetak Nota Pembayaran")
            print("5. Keluar Aplikasi")
            print("============================================")

            pilihan = input("Pilih menu (1-5): ").strip()

            try:
                if pilihan == "1":
                    self.menu_reservasi_lapak()
                elif pilihan == "2":
                    self.menu_sewa_alat()
                elif pilihan == "3":
                    self.menu_pencatatan_tangkapan()
                elif pilihan == "4":
                    if len(self.__transaksi_aktif) == 0:
                        print("\n[PERINGATAN] Layanan masih kosong! Tambahkan reservasi/sewa alat dulu.")
                    else:
                        self.__transaksi_aktif.cetak_nota()
                elif pilihan == "5":
                    print("\nTerima kasih telah menggunakan sistem pemancingan!")
                    sys.exit()
                else:
                    print("\n[ERROR] Pilihan menu tidak valid!")
            except InvalidDataError as e:
                # Custom Exception Handling
                print(f"\n[ERROR DATA] {e.message}")
            except ValueError:
                # Robustness Exception Handling
                print("\n[ERROR FORMAT] Masukkan input angka yang valid!")
            except Exception as e:
                print(f"\n[ERROR SISTEM] Terjadi kesalahan tak terduga: {e}")


if __name__ == "__main__":
    app = MainApp()
    app.run()