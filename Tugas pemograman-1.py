vd = {'key1' : 'Nilai 1', 
      'key2' : 'Nilai 2',
      'key3' : 'Nilai 3'
      }

Vl = ['Nilai1',
      'Nilai2',
      'Nilai3']

print(Vl[1])
print(vd['key2'])

print('\n')

data = {'nama' : 'Muhammad Fajrin Nur', 
        'nim'  : '231031101',
        'lulus': False
        }
print(data)
# mengakses data
print(data['nama'])

#Mengupdate data
data.update({'lulus':True})
data['lulus'] = True # mengupdate
# data['Lulus'] = True # Tambah data

del data['nama'] # menghapus data

print(data)

print('\n')
biodata = {'nama'  : 'Muhammad Fajrin Nur', 
       'umur'   : '19',
       'status' : 'mahasiswa',
       'prodi'  : 'sistem informasi',
       'nim'    : '231031101',
       'alamat' : 'jln Brimob',
        'a.s'   : 'sman 2 pare-pare',

       }
print(biodata['nama'])
print(biodata['umur'])
print(biodata['status'])
