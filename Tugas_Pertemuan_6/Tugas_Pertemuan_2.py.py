class Rekening :
    nama = ""
    saldo = ""

    def __init__(self, nama, saldo):
        self.nama = nama
        if saldo < 0:
            raise ValueError("saldo tidak boleh negatif")
        self.saldo = saldo
    def cek_saldo(self):
        return f"hasil dari method_str_"
    
rekening1 = Rekening("Andi", 1000000)
rekening1.cek_saldo()
rekening2 = Rekening("Aldo", -1000000)

print(rekening1)