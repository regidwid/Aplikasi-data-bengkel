# ###################################################################################################################
# # Capstone 1
# # Regi Dwi Darmawan JCDS - 0808 - 002
#####################################################################################################################
# 
# # ***MOHON UNTUK MENDAFTARKAN TERLEBIH DAHULU USERNAME DAN PASSWORD***
# # ***MOHON UNTUK INSTALL TABULATE TERLEBIH DAHULU***
#
#####################################################################################################################
# Define login


def login():
    data_akun = {'user_name': [],
             'password': []
             }
    while True:
        koneksi_1 = input('Apakah anda sudah memiliki akun? [Y/N] ')
        if koneksi_1 not in ('y', 'n'):
            print('Silahkan pilih dengan "Y" atau "N"')
            continue
        elif koneksi_1 == 'n':
            tambah_un = input('Masukan username: ')
            tambah_pas = input('masukan password yang diinginkan (hanya bisa huruf dan angka): ')
            if tambah_pas.isalnum():
                data_akun['user_name'] = tambah_un
                data_akun['password'] = tambah_pas
                print('username dan password berhasil dibuat')
                continue
            else:
                continue
        else:
            masuk_user = input('Masukan username anda:')
            masuk_pw = input('Masukan Password anda:')
            if masuk_user == data_akun['user_name'] and masuk_pw == data_akun['password']:
                print(f'Selamat datang kembali {masuk_user}!')
                break
            else:
                print('Username atau password salah!')


####################################################################################################################
# DATA BASE BARANG (TABEL)
data_barang_a = {
    'index':[1,2,3,4,5,6,7,8,9,10],
    'nama_barang':['kampas rem', 'oli', 'kampas kupling', 'busi', 'baut', 'minyak rem', 'lampu depan', 'lampu belakang', 'ban', 'velg'],
    'merk':['Nakas One', 'Top1', 'TDR', 'NGK', 'Heng', 'Faito', 'Osram', 'Luminos', 'Maxxis', 'RCB'],
    'stok_barang': [15, 20, 15, 30, 45, 25, 35, 45, 30, 20],
    'hpp_barang':[30_000, 40_000, 80_000, 20_000, 3000, 10_000, 7000, 5000, 170_000, 450_000 ],
    'harga_barang':[35_000, 50_000, 100_000, 25_000, 5000, 15_000, 10_000, 8000, 200_000, 500_000]
    }

data_terjual = {
    'index':[],
    'nama_barang':[],
    'merk':[],
    'jumlah_terjual': [],
    'hpp_barang':[],
    'harga_barang':[],
    'gross_profit': []
}
###################################################################################################################

# Define input
# Define fungsi input yang memiliki return numeric
def inputnumeric():
    while True:
        userinput = input()
        if userinput == '':
            print('Input tidak boleh kosong')
            continue
        elif userinput.isdigit() == False:
            print('Hanya diizinkan input numeric')
            continue
        elif int(userinput) == 0:
            print('Input 0 tidak diizinkan')
            continue
        else:
            break
    return int(userinput)

# Define fungsi input yang memiliki return tipe data string yang diinginkan.
def konfirmasi():
    while True:
        userinput = input()
        if userinput == '':
            print('Input tidak boleh kosong')
            continue
        elif userinput == ' ':
            print('Input tidak boleh kosong')
            continue
        elif userinput == '  ':
            print('Input tidak boleh kosong')
            continue
        else:
            break
    return userinput

# Define fungsi input yang memiliki return data jawban Ya atau Tidak
def konfirmasi_yt():
    while True:
        userinput = input().lower()
        if userinput == '':
            print('Input tidak boleh kosong')
            continue
        elif userinput.isdigit() == True:
            print('Input numeric tidak diizinkan')
        elif userinput != 'y' and userinput != 'n':
            print('Perintah yang anda masukan salah, harap hanya input perintah "Y" atau "N" !')
            continue
        else:
            break
    return userinput.lower()


###################################################################################################################
# Define sorted / pengurutan Sub menu 1
def pengurutan(f):
    while True:
        print('''Pilih metode pengurutan yang anda inginkan :
    1. Dari besar ke kecil
    2. Dari kecil ke besar  
-------------------------------------------------  
    Masukan pilhanmu disini: ''')
        naik_turun = inputnumeric()
        if naik_turun == 1:
            barang_list = list(zip(data_barang_a['index'], # mengubah data dictionary menjadi list
                                data_barang_a['nama_barang'], 
                                data_barang_a['merk'], 
                                data_barang_a['stok_barang'], 
                                data_barang_a['hpp_barang'],
                                data_barang_a['harga_barang']))
            
            barang_sorted = sorted(barang_list, key=lambda x: x[f - 1], reverse=True) # -1 karena index dimulai dari 0

            tabel_barang_sorted = {
            'index': [row[0] for row in barang_sorted], # mengubah kembali lst yang telah di sorted menjadi dictionary
            'nama_barang': [row[1] for row in barang_sorted],
            'merk': [row[2] for row in barang_sorted],
            'stok_barang' : [row[3] for row in barang_sorted],
            'hpp_barang' : [row[4] for row in barang_sorted],
            'harga_barang' : [row[5] for row in barang_sorted]}

            return print(tabulate(tabel_barang_sorted, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
        elif naik_turun == 2:
            barang_list = list(zip(data_barang_a['index'], # mengubah data dictionary menjadi list
                                data_barang_a['nama_barang'], 
                                data_barang_a['merk'], 
                                data_barang_a['stok_barang'], 
                                data_barang_a['hpp_barang'],
                                data_barang_a['harga_barang']))
            
            barang_sorted = sorted(barang_list, key=lambda x: x[f - 1]) # -1 karena index dimulai dari 0

            tabel_barang_sorted = {
            'index': [row[0] for row in barang_sorted], # mengubah kembali lst yang telah di sorted menjadi dictionary
            'nama_barang': [row[1] for row in barang_sorted],
            'merk': [row[2] for row in barang_sorted],
            'stok_barang' : [row[3] for row in barang_sorted],
            'hpp_barang' : [row[4] for row in barang_sorted],
            'harga_barang' : [row[5] for row in barang_sorted]}

            return print(tabulate(tabel_barang_sorted, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
        
        else:
            print('Harap hanya input angka 1 atau 2, silahkan coba lagi!')
            continue
###################################################################################################################
# Define sorted / pengurutan Sub menu 6
def pengurutan6(f):
   while True:
        print('''Pilih metode pengurutan yang anda inginkan :
    1. Dari besar ke kecil
    2. Dari kecil ke besar
-------------------------------------------------  
    Masukan pilhanmu disini: ''')
        naik_turun = inputnumeric()
        if naik_turun == 1:
            barang_list = list(zip(data_terjual['index'], # mengubah data dictionary menjadi list
                                data_terjual['nama_barang'], 
                                data_terjual['merk'], 
                                data_terjual['jumlah_terjual'], 
                                data_terjual['hpp_barang'],
                                data_terjual['harga_barang'],
                                data_terjual['gross_profit']))
            
            barang_sorted = sorted(barang_list, key=lambda x: x[f - 1], reverse=True) # -1 karena index dimulai dari 0

            tabel_barang_sorted = {
            'index': [row[0] for row in barang_sorted], # mengubah kembali lst yang telah di sorted menjadi dictionary
            'nama_barang': [row[1] for row in barang_sorted],
            'merk': [row[2] for row in barang_sorted],
            'jumlah_barang' : [row[3] for row in barang_sorted],
            'hpp_barang' : [row[4] for row in barang_sorted],
            'harga_barang' : [row[5] for row in barang_sorted],
            'gross_profit' : [row[6] for row in barang_sorted],}

            return print(tabulate(tabel_barang_sorted, headers=['Index', 'Nama Barang', 'Merk', 'Jumlah Terjual','HPP', 'Harga Barang', 'Gross Profit'], tablefmt='fancy_grid'))
        elif naik_turun == 2:
            barang_list = list(zip(data_terjual['index'], # mengubah data dictionary menjadi list
                                data_terjual['nama_barang'], 
                                data_terjual['merk'], 
                                data_terjual['jumlah_terjual'], 
                                data_terjual['hpp_barang'],
                                data_terjual['harga_barang'],
                                data_terjual['gross_profit']))
            
            barang_sorted = sorted(barang_list, key=lambda x: x[f - 1])

            tabel_barang_sorted = {
            'index': [row[0] for row in barang_sorted], # mengubah kembali lst yang telah di sorted menjadi dictionary
            'nama_barang': [row[1] for row in barang_sorted],
            'merk': [row[2] for row in barang_sorted],
            'jumlah_barang' : [row[3] for row in barang_sorted],
            'hpp_barang' : [row[4] for row in barang_sorted],
            'harga_barang' : [row[5] for row in barang_sorted],
            'gross_profit' : [row[6] for row in barang_sorted],}

            return print(tabulate(tabel_barang_sorted, headers=['Index', 'Nama Barang', 'Merk', 'Jumlah Terjual','HPP', 'Harga Barang', 'Gross Profit'], tablefmt='fancy_grid'))
        
        else:
            print('Harap hanya input angka 1 atau 2, silahkan coba lagi!')
            continue

###################################################################################################################
from tabulate import tabulate # Import tabulate untuk membuat tabel berdasarkan data yang diinginkan
# Main menu
print(f'Halo! Selamat datang kembali!')
print(' ')
def main_menu():
    while True:
        from tabulate import tabulate
        print(''' Silahkan pilih nomor menu yang diinginkan!:
    1. Tampilkan data stok
    2. Tambah barang
    3. Kurangi stok
    4. Update Barang
    5. Pembelian barang
    6. Tampilkan data terjual
    7. Exit program
 -------------------------------------------------
    Masukan angka disini: ''')
        pilihan_main_menu = inputnumeric()
        if pilihan_main_menu == 1:
            m1()
        elif pilihan_main_menu == 2:
            m2()
        elif pilihan_main_menu == 3:
            m3()
        elif pilihan_main_menu == 4:
            m4()
        elif pilihan_main_menu == 5:
            m5()
        elif pilihan_main_menu == 6:
            m6()
        elif pilihan_main_menu == 7:
            m7()
        else:
            print('Inputan yang anda masukan salah, hanya pilih angka dari 1-7, silahkan masukan angka kembali')
        print(' ')

###################################################################################################################
# Define Menu 1    
# Read

def m1():
    print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
    print(' ')
    while True:
        print('''Pilih menu yang diinginkan:
    1. Sorted data
    2. Mengambil data tertentu
    3. Kembali ke menu utama''')
        pilihan_m1 = inputnumeric()
        if pilihan_m1 == 1:
            print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
            print('''apakah anda ingin  mensorted data diatas?
    Y untuk Yes
    N untuk kembali ke menu utama ''')
            opsi_menu = konfirmasi_yt()
            if opsi_menu.lower() == 'n':
                break
            elif opsi_menu.lower() == 'y':
                print('''masukan angka untuk memilih pengurutan
        1. Sorted by Index
        2. Sorted by Nama Barang
        3. Soretd by Merk
        4. Sorted by Stok Barang
        5. Sorted by HPP Barang
        6. Sorted by Harga Barang  
    -------------------------------------------------
        Masukan pilihanmu disini: ''')
                opsi_menu1 = inputnumeric()
                if opsi_menu1 == 1:
                    pengurutan(opsi_menu1)
                elif opsi_menu1 == 2:
                    pengurutan(opsi_menu1)
                elif opsi_menu1 == 3:
                    pengurutan(opsi_menu1)
                elif opsi_menu1 == 4:
                    pengurutan(opsi_menu1)
                elif opsi_menu1 == 5:
                    pengurutan(opsi_menu1)
                elif opsi_menu1 == 6:
                    pengurutan(opsi_menu1)
                else:
                    print('harap hanya memasukan angka dari 1 hingga 6, silahkan ulangi!')
                    continue
        elif pilihan_m1 == 2:
            print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
            print('Silahkan masukan nomer index yang anda inginkan')
            indeks = inputnumeric()
            if indeks > len(data_barang_a['index']):
                print(f'Angka yang anda masukan salah tolong hanya masukan angka dari 1 - {len(data_barang_a["index"])}')
                continue
            elif indeks > 0 and indeks <= len(data_barang_a['index']):
                indeks = indeks - 1
                for a in data_barang_a:
                    print(f'''{a}: {data_barang_a[a][indeks]}''')
        elif pilihan_m1 == 3:
            break
        else:
            print('Angka yang anda masukan salah tolong hanya masukan angka dari 1 - 3')

                
    

###################################################################################################################
# Menu 2
# Define menu 2
# Create
def m2():
    while True:
        print('Masukan nama barang: ')
        pilihan_barang = konfirmasi()
        print('Masukan merk barang: ')
        pilihan_merk = konfirmasi()
        print('Masukan stok barang: ')
        pilihan_stok = inputnumeric()
        print('Masukan hpp barang: ')
        hpp_barang = inputnumeric()
        print('Masukan harga barang: ')
        pilihan_harga = inputnumeric()
        if pilihan_barang in data_barang_a['nama_barang']:
            print('Barang yang ingin anda tambahkan sudah ada')
            continue
        elif pilihan_barang not in data_barang_a['nama_barang']:
            print(f'''Apakah anda ingin memasukan:
Nama Barang: {pilihan_barang}
Merk: {pilihan_merk}
Stok: {pilihan_stok}
Hpp: {hpp_barang}
Harga: {pilihan_harga}
[Y/N]
Y untuk Yes
N untuk kembali ke menu utama''')
        masukan = konfirmasi_yt()
        if masukan == 'y':
            inisiator = len(data_barang_a['index']) + 1
            data_barang_a['index'].append(inisiator) 
            data_barang_a['nama_barang'].append(pilihan_barang)
            data_barang_a['stok_barang'].append(pilihan_stok)
            data_barang_a['harga_barang'].append(pilihan_harga)
            data_barang_a['hpp_barang'].append(hpp_barang)
            data_barang_a['merk'].append(pilihan_merk)
            pass
        elif masukan == 'n':
            break
        inisiator = inisiator + 1 # agar pada nomer index tetap berurut
        print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
        print('Stok berhasil di update!')
        print(' ')
        print('''apakah anda ingin memasukan barang yang lain? [Y/N]
Y untuk Yes
N untuk kembali ke menu utama''')
        masukan_def2 = konfirmasi_yt()
        if masukan_def2 == 'y':
            continue
        elif masukan_def2 == 'n':
            break

#################################################################################################################   
# Define menu 3
# Delete
def m3():
    while True:
        print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
        print('Masukan nomer index barang yang ingin dihapus: ')
        kurangi_barang_1 = inputnumeric()
        kurangi_barang = kurangi_barang_1 - 1 # dikurangi 1 karena index dimulai dari 0
        if kurangi_barang > len(data_barang_a['index']) - 1:
            print(f'Perintah yang anda masukan salah, harap hanya memasukan angka dari 1 - {len(data_barang_a['index'])}')
            continue
        else:
            print(f'''apakah anda ingin menghapus {data_barang_a["nama_barang"][kurangi_barang]}? [Y/N]
Y untuk Yes
N untuk kembali ke menu utama''')
            konfir = konfirmasi_yt()
            if konfir == 'n':
                break
            elif konfir == 'y':
                pass
        for a in data_barang_a:
            del data_barang_a[a][kurangi_barang]
            data_barang_a['index'] = list(range(1, (len(data_barang_a['index']) + 1))) # Agar nomor index di tabel tetap utuh
            print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
            print('Penghapusan data berhasil!')
        print('''Apakah anda ingin mengurangi barang yang lain? [Y/N]
Y untuk Yes
N untuk kembali ke menu utama''')
        confirm_kurangi = konfirmasi_yt()
        if confirm_kurangi  == 'y':
            continue
        elif confirm_kurangi == 'n':
            break
        

#################################################################################################################   
# Define menu 4
# Update
def m4():
    while True:
        print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
        print('pilih nomor index barang yang anda ingin update: ')
        update_index_1 = inputnumeric()
        if update_index_1 > len(data_barang_a['index']) or update_index_1 == 0:
            print('Angka index yang anda masukan tidak ada mohon periksa kembali')
            continue
        elif update_index_1  <= len(data_barang_a['index']):
            update_index = update_index_1 - 1
            print('''Silahkan pilih nomor berdasarkan data yang ingin anda update
    1. Update nama barang
    2. Update merk barang
    3. Update stok barang
    4. Update Hpp
    5. Update harga barang
-------------------------------------------------
    Masukan angka yang diinginkan disini: ''')
            pilihan_update = inputnumeric()
            if pilihan_update == 1:
                print(f'data awal adalah {data_barang_a['nama_barang'][update_index]}, akan diubah menjadi: ')
                pergantian =  konfirmasi()
                print(f'''apakah anda yakin akan merubah {data_barang_a['nama_barang'][update_index]} menjadi {pergantian}? [Y/N]
Y untuk Yes
N unutk kembali ke menu utama ''')
                yt = konfirmasi_yt()
                if yt == 'y':
                    data_barang_a['nama_barang'][update_index] = pergantian
                    print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Stok','Harga Barang', 'HPP'], tablefmt='fancy_grid'))
                    print('Data berhasil diubah!')
                    break
                elif yt == 'n':
                    break
            elif pilihan_update == 2:
                print(f'data awal adalah {data_barang_a['merk'][update_index]}, akan diubah menjadi: ')
                pergantian = konfirmasi()
                print(f'''apakah anda yakin akan merubah {data_barang_a['merk'][update_index]} menjadi {pergantian}? [Y/N]
Y untuk Yes
N unutk kembali ke menu utama ''')
                yt = konfirmasi_yt()
                if yt == 'y':
                    data_barang_a['merk'][update_index] = pergantian
                    print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Stok','Harga Barang', 'HPP'], tablefmt='fancy_grid'))
                    print('Data berhasil diubah!')
                    break
                elif yt == 'n':
                    break       
            elif pilihan_update == 3:
                print(f'data awal adalah {data_barang_a['stok_barang'][update_index]}, akan diubah menjadi: ')
                pergantian =  inputnumeric()
                print(f'''apakah anda yakin akan merubah {data_barang_a['stok_barang'][update_index]} menjadi {pergantian}? [Y/N]
Y untuk Yes
N unutk kembali ke menu utama ''')
                yt = konfirmasi_yt()
                if yt == 'y':
                    data_barang_a['stok_barang'][update_index] = pergantian
                    print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Stok','Harga Barang', 'HPP'], tablefmt='fancy_grid'))
                    print('Data berhasil diubah!')
                    break
                elif yt == 'n':
                    break             
            elif pilihan_update == 4:
                print(f'data awal adalah {data_barang_a['hpp_barang'][int(update_index)]}, akan diubah menjadi: ')
                pergantian =  inputnumeric()
                print(f'''apakah anda yakin akan merubah {data_barang_a['hpp_barang'][update_index]} menjadi {pergantian}? [Y/N]
Y untuk Yes
N unutk kembali ke menu utama ''')
                yt = konfirmasi_yt()
                if yt == 'y':
                    data_barang_a['hpp_barang'][int(update_index)] = pergantian
                    print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Stok','Harga Barang', 'HPP'], tablefmt='fancy_grid'))
                    print('Data berhasil diubah!')
                    break
                elif yt == 'n':
                    break
            elif pilihan_update == 5:
                print(f'data awal adalah {data_barang_a['harga_barang'][int(update_index)]}, akan diubah menjadi: ')
                pergantian =  inputnumeric()
                print(f'''apakah anda yakin akan merubah {data_barang_a['harga_barang'][update_index]} menjadi {pergantian}? [Y/N]
Y untuk Yes
N unutk kembali ke menu utama ''')
                yt = konfirmasi_yt()   
                if yt == 'y':
                    data_barang_a['harga_barang'][int(update_index)] = pergantian
                    print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Stok','Harga Barang', 'HPP'], tablefmt='fancy_grid'))
                    print('Data berhasil diubah!')
                    break
                elif yt == 'n':
                    break
            else:
                print('Nomor yang anda masukan salah, silahkan coba lagi!')
                continue



#################################################################################################################   
# Define menu 5
# fungsi belanja
def m5():
    tabel_barang_dibeli = {
                'Index': [],
                'Nama': [],
                'Merk': [],
                'Qty': [],
                'Harga': [],
                'Total Harga': []
                }

    while True:
        print(tabulate(data_barang_a, headers=['Index', 'Nama Barang', 'Merk', 'Stok','HPP', 'Harga Barang'], tablefmt='fancy_grid'))
        print('masukan nomor index barang yang ingin dibeli: ')
        yang_dibeli_1 = inputnumeric()
        print('masukan jumlah yang ingin dibeli: ')
        banyak_yang_dibeli = inputnumeric()
        yang_dibeli = yang_dibeli_1 - 1
        inisiator = len(data_terjual['index']) + 1
        if yang_dibeli_1 > len(data_barang_a['index']):
            print('Angka index barang yang anda masukan salah silahkan coba lagi!')
            continue
        elif data_barang_a['stok_barang'][yang_dibeli] < banyak_yang_dibeli:
            print(f'''Jumlah yang dimasukan terlalu banyak\n{data_barang_a['nama_barang'][yang_dibeli]} tersisa: {data_barang_a['stok_barang'][yang_dibeli]} 
Silahkan ulangi''')
            break
        elif yang_dibeli_1 > 0 and yang_dibeli_1 <= len(data_barang_a['index']):
                data_barang_a['stok_barang'][yang_dibeli] -= banyak_yang_dibeli #untuk mengurangi stok karena pembelian
                total_harga = banyak_yang_dibeli * (data_barang_a['harga_barang'][yang_dibeli])
                # untuk menambahkan ke tabel detail belanja
                tabel_barang_dibeli['Index'].append(data_barang_a['index'][yang_dibeli])
                tabel_barang_dibeli['Nama'].append(data_barang_a['nama_barang'][yang_dibeli])
                tabel_barang_dibeli['Qty'].append(banyak_yang_dibeli)
                tabel_barang_dibeli['Harga'].append(data_barang_a['harga_barang'][yang_dibeli])
                tabel_barang_dibeli['Total Harga'].append(total_harga)
                tabel_barang_dibeli['Merk'].append(data_barang_a['merk'][yang_dibeli])
                print(tabulate(tabel_barang_dibeli, headers=['Index', 'Nama barang','Merk' ,'Jumlah', 'Harga', 'Total Harga'], tablefmt='fancy_grid'))
                # untuk menambahkan ke tabel data terjual
                data_terjual['index'].append(inisiator)
                inisiator += 1
                data_terjual['nama_barang'].append(data_barang_a['nama_barang'][yang_dibeli])
                data_terjual['merk'].append(data_barang_a['merk'][yang_dibeli])
                data_terjual['jumlah_terjual'].append(banyak_yang_dibeli)
                data_terjual['hpp_barang'].append(data_barang_a['hpp_barang'][yang_dibeli])
                data_terjual['harga_barang'].append(data_barang_a['harga_barang'][yang_dibeli])
                data_terjual['gross_profit'].append((data_barang_a['harga_barang'][yang_dibeli] - data_barang_a['hpp_barang'][yang_dibeli]) * banyak_yang_dibeli )
                print('Mau beli yang lain? [Y/N]: ')
                masukan = konfirmasi_yt()
                if masukan == 'y':
                    continue
                elif masukan == 'n':
                    print(' ')

                    print('Detail Belanja')
                    total_keseluruhan = sum(tabel_barang_dibeli['Total Harga'])
                    print(tabulate(tabel_barang_dibeli, headers=['Index', 'Nama barang','Merk' ,'Jumlah', 'Harga', 'Total Harga'], tablefmt='fancy_grid'))
                    print(f' Total yang harus dibayarkan {total_keseluruhan}')
                    print('Masukkan jumlah uang :')
                    uang_diserahkan_1 = inputnumeric()
                    uang_diserahkan = int(uang_diserahkan_1)
                    kembalian = abs(uang_diserahkan - total_keseluruhan)
                    if total_keseluruhan > uang_diserahkan:
                        for x in data_terjual:
                            del data_terjual[x][-(len(tabel_barang_dibeli['Index'])): ]
                        print(f'Uang anda kurang sebesar {kembalian}\nPembelian dibatalkan, silahkan ulangi lagi!')
                        inisiasi = 0
                        for a in tabel_barang_dibeli['Index']:
                            data_barang_a['stok_barang'][a - 1] = data_barang_a['stok_barang'][a - 1] + tabel_barang_dibeli['Qty'][inisiasi]
                            inisiasi += 1 # untuk menambahkan kembali stok barang yang tidak jadi dijual 
                        break
                    elif uang_diserahkan == total_keseluruhan:
                        print(tabulate(data_terjual, headers=['Index', 'Nama Barang', 'Merk', 'Jumlah Terjual','HPP', 'Harga Barang', 'Gross Profit'], tablefmt='fancy_grid'))
                        print('Terima Kasih!')
                        break
                    else:
                        print(f'Terima Kasih! \nkembalian anda {kembalian}')
                        break  
        else:
            print('Angka yang anda masukan salah, silahkan coba lagi!')                              
print(' ')

#################################################################################################################
# Define menu 6
# read data terjual
def m6():
    print(tabulate(data_terjual, headers=['Index', 'Nama Barang', 'Merk', 'Jumlah Terjual','HPP', 'Harga Barang', 'Gross Profit'], tablefmt='fancy_grid'))
    print(f'Total gross profit adalah {sum(data_terjual["gross_profit"])}')
    print(' ')
    while True:
        print('''apakah anda ingin  mensorted data diatas? [Y/N] 
    Y untuk Yes
    N untuk kembali ke menu utama''')
        opsi_menu = konfirmasi_yt()
        if opsi_menu.lower() == 'n':
            break
        elif opsi_menu.lower() == 'y':
            print('''masukan angka untuk memilih pengurutan
    1. Sorted by Index
    2. Sorted by Nama Barang
    3. Soretd by Merk
    4. Sorted by Jumlah terjual
    5. Sorted by HPP Barang
    6. Sorted by Harga Barang
    7. Sorted by Gross Profit 
-------------------------------------------------
    Masukan pilihanmu disini: ''')
            opsi_menu6 = inputnumeric()
            if opsi_menu6 == 1:
                pengurutan6(opsi_menu6)
            elif opsi_menu6 == 2:
                pengurutan6(opsi_menu6)
            elif opsi_menu6 == 3:
                pengurutan6(opsi_menu6)
            elif opsi_menu6 == 4:
                pengurutan6(opsi_menu6)
            elif opsi_menu6 == 5:
                pengurutan6(opsi_menu6)
            elif opsi_menu6 == 6:
                pengurutan6(opsi_menu6)
            elif opsi_menu6 == 7:
                pengurutan6(opsi_menu6)
            else:
                print('harap hanya memasukan angka dari 1 hingga 6, silahkan ulangi!')
                continue

#################################################################################################################
# Define menu 7
# exit program
def m7():
    print('Program dihentikan, Terima kasih!')
    exit()
#################################################################################################################
# Running
login()
main_menu()
