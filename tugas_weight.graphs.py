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
 distance = {}
        # melakukan looping pada daftar kota
        for kota in self.daftarkota:
            # memasukkan hasil looping ke  variabel kota dan dgn nilai infinite
            distance[kota] = float('inf')
        # men set agar jarak ke kota asal adalah o
        distance[source] = 0
    
        # membuat variiabel kota mula
        kota_mula = []
        # melakukan looping untuk memasukkan nama kota ke list kota mula
        for kota in self.daftarkota:
            kota_mula.append(kota)
        
        # melakukan looping selama kota mula masih ada isinya
        while kota_mula:
            # buat variabel jarak minimum
            min_distance = float('inf')
            # buat variabel kota terdekat
            kota_terdekat = None
            
            # melakukan looping pada kota mula
            for kota in kota_mula:
                # jika ditemukan kota dengan jarak kota lebih kecil daripada min distances
                if distance[kota] < min_distance:
                # maka closest kota dirubah ke kota tersebut
                    min_distance = distance[kota]
                    kota_terdekat = kota
            
            # menghapus kota yang telah ketemu pada kota mula agar tdk di terbaca berulang
            kota_mula.remove(kota_terdekat)
            
            #perbarui nilai jarak dari semua vertex yang berdekatan
            for neighbor, jarak in self.daftarkota[kota_terdekat].items():
                # Ini menghitung total jarak dari kota asal ke tetangga melalui kota_terdekat.
                Neighbor_distance = distance[kota_terdekat] + jarak
                # Memeriksa apakah jarak baru yang dihitung lebih pendek dari jarak yang telah tercatat sebelumnya untuk tetangga tersebut.
                if Neighbor_distance < distance[neighbor]:
                    distance[neighbor] = Neighbor_distance
        return distance

    # membuat fungsi untuk mengeprint daftar kota dan kota yang memiliki akses jalan ke kota lain
    def print_daftar_kota(self):
        print('Berikut merupakan daftar kota yang terdaftar pada sistem peta:')
        # melakukan iterasi pada daftarkota untuk mendapatkan daftar kota yang telah terdaftar
        for kota in self.daftarkota:
            # print nama kota
            print("-", kota)
            # cek apakah list jalan kota kosong atau tidak
            if self.daftarkota[kota]:
                # jika list jalan terdapat nama kota, maka print :
                print("  Akses ke kota lain:")
                # dan iterasi list jalan yang ada pada kota dan print jalan aksesnya serta jaraknya
                for jalan, jarak in self.daftarkota[kota].items():
                    print("  *", jalan, "->", jarak, "KM")
            # dan jika list kosong, maka print :
            else:
                print("  Tidak memiliki akses ke kota lain")



# membuat list peta
PetaJepang = Peta()

# tambahkan kota
PetaJepang.tambahkanKota("Ueno")
PetaJepang.tambahkanKota("Shimonita")
PetaJepang.tambahkanKota("Annaka")
PetaJepang.tambahkanKota("Takasaki")
PetaJepang.tambahkanKota("Ogano")
PetaJepang.tambahkanKota("Chichibu")
PetaJepang.tambahkanKota("Minano")
PetaJepang.tambahkanKota("Nagatoro")
PetaJepang.tambahkanKota("Yorii")
PetaJepang.tambahkanKota("Honjo")
PetaJepang.tambahkanKota("Isesaki")
PetaJepang.tambahkanKota("Maebashi")

# tambahkan jalan
PetaJepang.tambahkanJalan("Shimonita","Annaka",21)
PetaJepang.tambahkanJalan("Shimonita","Ueno",141)
PetaJepang.tambahkanJalan("Ueno","Ogano",115)
PetaJepang.tambahkanJalan("Ogano","Nagatoro",17)
PetaJepang.tambahkanJalan("Ogano","Minano",13)
PetaJepang.tambahkanJalan("Ogano","Chichibu",13)
PetaJepang.tambahkanJalan("Chichibu","Minano",10)
PetaJepang.tambahkanJalan("Chichibu","Yorii",21)
PetaJepang.tambahkanJalan("Minano","Nagatoro",81)
PetaJepang.tambahkanJalan("Minano","Yorii",74)
PetaJepang.tambahkanJalan("Nagatoro","Yorii",11)
PetaJepang.tambahkanJalan("Nagatoro","Honjo",26)
PetaJepang.tambahkanJalan("Nagatoro","Takasaki",34)
PetaJepang.tambahkanJalan("Takasaki","Annaka",12)
PetaJepang.tambahkanJalan("Takasaki","Maebashi",11)
PetaJepang.tambahkanJalan("Takasaki","Isesaki",20)
PetaJepang.tambahkanJalan("Takasaki","Honjo",21)
PetaJepang.tambahkanJalan("Honjo","Maebashi",32)
PetaJepang.tambahkanJalan("Honjo","Isesaki",8)
PetaJepang.tambahkanJalan("Isesaki","Maebashi",16)

# untuk print hasil program
PetaJepang.print_daftar_kota()
print("===============================")
# untuk print jarak kota-kota yang ada pada program terhadap kota honjo
jarak_kota = PetaJepang.djikstra("Honjo")
print("jarak kota Honjo ke kota lainnya adalah :")
for kota, jarak in jarak_kota.items():
    print(kota, "->", jarak, "KM")
