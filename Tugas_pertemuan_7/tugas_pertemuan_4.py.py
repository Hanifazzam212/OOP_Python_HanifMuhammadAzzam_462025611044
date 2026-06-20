class Produk : 
    def __init__(self, nama, harga) :
        self.nama = nama
        self.harga = harga

    def __str__(self) :
        return f"Nama Produk : {self.nama}, Harga Produk : {self.harga}"    

    #perbandingan == 
    def __eq__(self, other) :
       return self.harga == other.harga
    #perbandingan >
    def __gt__(self, other) :
        return self.harga > other.harga 
    #perbandingan <
    def __lt__(self, other) :
        return self.harga < other.harga 
    
    #membuat object 
produk1 = Produk("Laptop", 10000000)
produk2 = Produk("Smartphone", 5000000) 
produk3 = Produk("Tablet", 7000000)

#menampilkan info produk
print(produk1)
print(produk2)
print(produk3)

print("\nPerbandingan Harga Produk :")

#perbandingan harga produk
print(f"{produk1.nama} == {produk2.nama} : {produk1 == produk2}")

print(f"{produk1.nama} > {produk2.nama} : {produk1 > produk2}")

print(f"{produk1.nama} < {produk2.nama} : {produk1 < produk2}")
