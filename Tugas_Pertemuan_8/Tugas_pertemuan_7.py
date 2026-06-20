# Parent Class
class AlatPembayaran:
    def proses_bayar(self, jumlah):
        print(f"Memproses pembayaran sebesar Rp{jumlah}")


# Child Class 1
class KartuKredit(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah} berhasil menggunakan Kartu Kredit.")


# Child Class 2
class EWallet(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah} berhasil menggunakan E-Wallet.")


# Class lain yang tidak mewarisi AlatPembayaran
# Digunakan untuk menunjukkan Duck Typing
class TransferBank:
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah} berhasil melalui Transfer Bank.")


# Fungsi Duck Typing
def jalankan_transaksi(objek, jumlah):
    objek.proses_bayar(jumlah)


# Program Utama
if __name__ == "__main__":
    kartu = KartuKredit()
    ewallet = EWallet()
    transfer = TransferBank()

    print("=== Simulasi Transaksi ===")

    jalankan_transaksi(kartu, 500000)
    jalankan_transaksi(ewallet, 250000)
    jalankan_transaksi(transfer, 1000000)