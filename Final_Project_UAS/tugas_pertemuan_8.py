# Custom Exception
class SaldoTidakCukupError(Exception):
    """Exception untuk saldo yang tidak mencukupi"""
    pass


# Class Utama
class RekeningBank:
    def __init__(self, nama_pemilik, saldo):
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo

    def tarik_uang(self, jumlah):
        # Validasi jumlah penarikan
        if jumlah > self.saldo:
            raise SaldoTidakCukupError(
                f"Penarikan gagal! Saldo Anda hanya Rp{self.saldo}"
            )

        self.saldo -= jumlah
        print(f"Penarikan berhasil sebesar Rp{jumlah}")
        print(f"Sisa saldo: Rp{self.saldo}")


# Program Utama
rekening = RekeningBank("Hanif", 5000000)

try:
    jumlah_tarik = int(input("Masukkan jumlah uang yang ingin ditarik: Rp"))
    rekening.tarik_uang(jumlah_tarik)

except SaldoTidakCukupError as e:
    print("ERROR:", e)

except ValueError:
    print("Input harus berupa angka!")

finally:
    print("Proses pemeriksaan transaksi telah selesai.")