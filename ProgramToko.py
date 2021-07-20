import sys
list_tanaman = []
list_perawatan = []
list_karyawan = []
list_keuangan = []


def tabel(panjang):
    print("*"*((16*4)+4))
    print("Data Tanaman Toko GREAT FLORIST".center(65))
    if panjang != 0:
        for baris in range(len(list_tanaman)):
            for kolom in range(1):
                if baris == 0 :
                    print("|"+"KODE".center(15)+"|","NAMA".center(15)+"|","JENIS".center(15)+"|","HARGA".center(15)+"|")
                    print("="*((16*4)+4))

            for kolom in range(4) :
                if kolom == 0:
                    print("|"+str(list_tanaman[baris][kolom]).center(15)+"|", end=" ")
                else:
                    print(str(list_tanaman[baris][kolom]).center(15)+"|", end=" ")
            
            print(" ")
            print("="*((16*4)+4))
    else:
        print("="*((16*4)+4))
        print("|"+"KODE".center(15)+"|","NAMA".center(15)+"|","JENIS".center(15)+"|","HARGA".center(15)+"|")
        print("="*((16*4)+4))
        print("Data Kosong".center(66)+"|")
        print("="*((16*4)+4))

def perawatan(panjang):
    print("*"*((16*4)+3))
    print("Data Perawatan Toko GREAT FLORIST".center(65))
    if panjang != 0:
        for baris in range(len(list_perawatan)):
            for kolom in range(1):
                if baris == 0 :
                    print("|"+"Bulan".center(15)+"|","Jumlah".center(15)+"|","JENIS".center(15)+"|")
                    print("="*((16*3)+3))

            for kolom in range(3) :
                if kolom == 0:
                    print("|"+str(list_perawatan[baris][kolom]).center(15)+"|", end=" ")
                else:
                    print(str(list_perawatan[baris][kolom]).center(15)+"|", end=" ")
            
            print(" ")
            print("="*((16*3)+3))
    else:
        print("="*((16*3)+3))
        print("|"+"Bulan".center(15)+"|","Jumlah".center(15)+"|","JENIS".center(15)+"|")
        print("="*((16*3)+3))
        print("Data Kosong".center(50)+"|")
        print("="*((16*3)+3))
        
def header_data(panjang):
    print("*"*((16*4)+4))
    print("Data Karyawan Toko GREAT FLORIST".center(65))
    if panjang != 0:
        for baris in range(len(list_karyawan)):
            for kolom in range(1):
                if baris == 0 :
                    print("|"+"Nama".center(15)+"|","Alamat".center(15)+"|","No.Telp".center(15)+"|","Shift".center(15)+"|")
                    print("="*((16*4)+4))

            for kolom in range(4) :
                if kolom == 0:
                    print("|"+str(list_karyawan[baris][kolom]).center(15)+"|", end=" ")
                else:
                    print(str(list_karyawan[baris][kolom]).center(15)+"|", end=" ")
            
            print(" ")
            print("="*((16*4)+4))
    else:
        print("="*((16*4)+4))
        print("|"+"Nama".center(15)+"|","Alamat".center(15)+"|","No.Telp".center(15)+"|","Shift".center(15)+"|")
        print("="*((16*4)+4))
        print("Data Kosong".center(66)+"|")
        print("="*((16*4)+4))

def cuan():
    print("*"*((16*4)+4))
    print("Data Keuangan Toko GREAT FLORIST".center(65))
    print("*"*((16*4)+4))
    if list_keuangan == []:
    #if cuan != 0:
        print("|"+"Debit".center(15)+"|","Kredit".center(15)+"|","Saldo".center(15)+"|","Keterangan".center(15)+"|")
        print("="*((16*4)+4))
        print ("|"+"Data Kosong".center(65)+"|")
        print("="*((16*4)+4))
    for baris in range(len(list_keuangan)):
        for kolom in range(1):
            if baris == 0 :
                print("|"+"Debit".center(15)+"|","Kredit".center(15)+"|","Saldo".center(15)+"|","Keterangan".center(15)+"|")
                print("="*((16*4)+4))

        for kolom in range(4) :
            if kolom == 0:
                print("|"+str(list_keuangan[baris][kolom]).center(15)+"|", end=" ")
            else:
                print(str(list_keuangan[baris][kolom]).center(15)+"|", end=" ")
        print(" ")
        print("="*((16*4)+4))

def hapus():
    print("[A] hapus tanaman")
    print("[B] hapus perawatan")
    print("[C] hapus karyawan")
    print("[D] hapus keuangan")
    pilihan=input("apakah yang ingin anda hapus:")
    if pilihan == "A":
        #tanaman
        kode =  input("Kode : ")
        nama_tnm = input("Nama : ")
        jenis = input("Jenis : ")
        harga = input("Harga : ")
        list_tanaman.remove((kode, nama_tnm, jenis, harga))
        print("\n")
        print("Data telah dihapus")

    elif pilihan == "B" :
        #data perawatan
        bulan =  input("Bulan : ")
        jumlah = input("Jumlah : ")
        jenis = input("Jenis : ")
        list_perawatan.remove((bulan, jumlah, jenis))
        print("\n")
        print("Data telah dihapus")

    elif pilihan == "C" :
        #data karyawan
        nama =  input("Nama Karyawan : ")
        alamat = input("Alamat : ")
        no_telp = input("No Telp : ")
        shif = input("Shift : ")
        list_karyawan.remove((nama, alamat, no_telp, shif))
        print("\n")
        print("Data telah dihapus")
    
    elif pilihan == "D":
        #data keuangan
        debit =  input("Debit : ")
        kredit = input("Kredit : ")
        saldo = input("Saldo : ")
        keterangan = input("Keterangan : ")
        list_keuangan.remove((debit, kredit, saldo, keterangan))
        print("\n")
        print("Data telah dihapus")
    
    else:
        print("pilihan tidak valid !!")
    #seterusnya sampai elif pilihan D

def data_baru():
    print("[A] data tanaman")
    print("[B] data perawatan")
    print("[C] data karyawan")
    print("[D] data keuangan")
    pilihan=input("data apakah yang ingin anda buat:")
    if pilihan == "A":
        # Tanaman
        kode = input("Kode : ")
        nama_tnm = input("Nama : ")
        jenis = input("Jenis : ")
        harga = input("Harga : ")
        list_tanaman.append((kode, nama_tnm, jenis, harga))
        print("\n")
        lagi=input("apakah anda ingin menambahkan data lagi,Y/N??  ")
        if lagi == "Y":
            kode=input("Kode: ")
            nama_tnm=input("Nama tanaman: ")
            jenis=input("Jenis: ")
            harga=input("Harga: ")
            list_tanaman.append((kode, nama_tnm, jenis, harga))
            print("\n")
            lagi=input("apakah anda ingin menambahkan data lagi,Y/N??  ")
        else:
            return start
        
    elif pilihan =="B":
        # Perawatan
        bulan = input("Bulan : ")
        jumlah = input("Jumlah : ")
        jenis = input("Jenis : ")
        list_perawatan.append((bulan, jumlah, jenis,))
        print("\n")
        lagi=input("apakah anda ingin menambahkan data lagi,Y/N??  ")
        if lagi == "Y":
            bulan=input("Bulan: ")
            jumlah=input("Jumlah: ")
            jenis=input("Jenis: ")
            list_perawatan.append((bulan, jumlah, jenis,))
            print("\n")
            lagi=input("apakah anda ingin menambahkan data lagi,Y/N??  ")
        else:
            return start

    elif pilihan == "C":
        # Karyawan
        nama=input("Nama Karyawan: ")
        alamat=input("Alamat: ")
        no=input("Nomor telepon: ")
        print("shift pagi(07.00-12.00) atau shift siang (13.00-17.00)")
        shif=input("shif yang didapat: ")
        list_karyawan.append((nama,alamat,no,shif))
        print("\n")
        lagi=input("apakah anda ingin menambahkan data lagi,Y/N??  ")
        if lagi == "Y":
            nama=input("Nama Karyawan: ")
            alamat=input("Alamat: ")
            no=input("Nomor telepon: ")
            print("shift pagi(07.00-12.00) atau shift siang (13.00-17.00)")
            shif=input("shif yang didapat: ")
            list_karyawan.append((nama,alamat,no,shif))
            print("\n")
            lagi=input("apakah anda ingin menambahkan data lagi,Y/N??  ")
        else:
            return start
    
    elif pilihan == "D":
        # Keuangan
        saldo = 25000000
        kredit = 0
        pilihan = 0
        debit = 0
        print("[A] Cek Saldo")
        print("[B] masukan Debit")
        print("[C] masukan Kredit")
        pilihan=input("Masukan Pilihan anda :")
        print("\n")
        if pilihan == "A":
            print("saldo anda sekarang : ", saldo)

        elif pilihan == "B":
            keterangan = input("Keterangan : ")
            debit = int(input("Jumlah yang akan ditabung: Rp"))
            print("Jumlahnya yang akan ditabung yaitu Rp" + str(debit))
            saldo = saldo + debit
            list_keuangan.append((debit, kredit, saldo, keterangan))
            return

        elif pilihan == "C":
            print("Jumlah yang akan ditarik yaitu: Rp" + str(saldo))
            while True:
                keterangan = input("Keterangan : ")
                kredit = int(input("Penarikan: Rp"))
                if kredit > saldo:
                    print("Saldo anda tidak mencukupi untuk melakukan transaksi ini")
                    continue
                saldo = saldo - kredit
                list_keuangan.append((debit, kredit, saldo, keterangan))
                break
            return
        elif pilihan == "D":
            sys.exit("Terima kasih")

    else:
        print("!!!!!")        

def cari():
    input("Masukkan Kode yang dicari: ")
    ketemu = False
    for i in range(0, len(list_tanaman)):
        if cari == list_tanaman[i]:
            ketemu = True
        break
    
    if ketemu :
        print("Kode : ", cari, "Berhasil ditemukan")
    else:
        print("Kode : ", cari, "Tidak ditemukan")

def bubble_sort(array):
    n = len(array) # jumlah list
    # perulangan pertama
    for i in range(n): 
        # perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing" elemen
            if array[j] > array[j + 1]:
                # jika lebih besar, tukar.
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

start = True
while start :
    print("\n")
    print("===========================")
    print("[1] Lihat Daftar Tanaman")
    print("[2] Lihat Daftar Perawatan")
    print("[3] Lihat Daftar Tenaga Kerja")
    print("[4] Lihat Daftar Keuangan")
    print("[5] Tambah Barang")
    print("[6] Hapus Tanaman")
    print("[7] Cari Barang")
    print("[0] Tutup")
    print("===============================")
    pilih = input("Pilih menu> ")

    if(pilih == "1"):
        tabel(len(bubble_sort(list_tanaman)))
    elif(pilih == "2"):
        perawatan(len(bubble_sort(list_perawatan)))
    elif(pilih == "3"):
        header_data(len(bubble_sort(list_karyawan)))
    elif(pilih == "4"):
        cuan()
    elif(pilih == "5"):
        data_baru()
    elif(pilih == "6"):
        hapus() 
    elif(pilih == "7"):
        cari()
    elif(pilih == "0"):
        break
    else:
        print("Kamu memilih menu yang salah!")