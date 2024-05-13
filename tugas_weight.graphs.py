# deklarasi class peta
class Peta:

    # deklarasi constructor daftar kota
    def __init__(self):
        self.daftarkota = {}
    
    # membuat fungsi untuk menambahkan kota
    def tambahkanKota(self,kota,):
        # cek apakah kota yang di tambahkan sudah ada atau belum
        if kota not in self.daftarkota:
            self.daftarkota[kota] = {}
            return True
        # jika sudah ada maka return ke false
        return False
    
    # membuat fungsi untuk menghapus kota
    def hapusKota(self,kotaDihapus):
        # mengecek apakah kota yang akan dihapus adda pada dictionary daftar kota atau tidak
        if kotaDihapus in self.daftarkota:
            # melakukan iterasi terhadap daftar kota untuk mencari kota yang akan dihapus pada kota lain
            for kotalain in self.daftarkota:
                # jika kota ditemukan
                if kotaDihapus in self.daftarkota[kotalain]:
                    #akses jalan dihapus
                    del self.daftarkota[kotalain][kotaDihapus]
            # dan terakhir hapus kota dari daftarkota
            del self.daftarkota[kotaDihapus]
            return True
        return False
    
    # membuat fungsi untuk menambahkan jalan antar kota
    def tambahkanJalan(self,kota1,kota2,jarak):
        # cek apakah kkedua kota ada pada daftar kota atau tidak
        if kota1 in self.daftarkota and kota2 in self.daftarkota:
            # jika ada, maka masukkan kota 1 ke list kota 2 dan sebaliknya
            self.daftarkota[kota2][kota1] = jarak
            self.daftarkota[kota1][kota2] = jarak
            return True
        return False
        
    # membuat fungsi untuuk menghapus jalan antar kota
    def hapusJalan(self,kota1,kota2):
        # cek apakah kedua kota ada pada daftar kota atau tidak
        if kota1 in self.daftarkota and kota2 in self.daftarkota:
            # jika ada, maka hapus kota 1 pada list kota 2 dan sebaliknya
            self.daftarkota[kota2].remove(kota1)
            self.daftarkota[kota1].remove(kota2)
            return True
        return False

   # membuat algoritma  djikstra 
#untuk mencari kota tedekat dan menghitung jarak antar kota


