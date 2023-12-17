print('praktikum-2\n\n')
a= True
b= False
print('======ini and======')
hasil= a and a
print('nilai',a,'and',a,'adlah',hasil)
hasil= a and b
print('nilai',a,'and',b,'adlah',hasil)
hasil= b and a
print('nilai',b,'and',a,'adlah',hasil)
hasil= b and b
print('nilai',b,'and',b,'adlah',hasil)

print('\n======ini or======')
hasil= a or a
print('nilai',a,'or',a,'adlah',hasil)
hasil= a or b
print('nilai',a,'or',b,'adlah',hasil)
hasil= b or a
print('nilai',b,'or',a,'adlah',hasil)
hasil= b or b
print('nilai',b,'or',b,'adlah',hasil)

print('\n======ini not======')
hasil = not a
print('hasil not',a,'adalah',hasil)
hasil = not b
print('hasil not',b,'adalah',hasil)

print('\n======ini xor======')
hasil= a ^ a
print('nilai',a,'xor',a,'adlah',hasil)
hasil= a ^ b
print('nilai',a,'xor',b,'adlah',hasil)
hasil= b ^ a
print('nilai',b,'xor',a,'adlah',hasil)
hasil= b ^ b
print('nilai',b,'xor',b,'adlah',hasil)

print('\n======ini nand======')
hasil= not (a and a)
print('nilai',a,'nand',a,'adlah',hasil)
hasil= not (a and b)
print('nilai',a,'nand',b,'adlah',hasil)
hasil= not (b and a)
print('nilai',b,'nand',a,'adlah',hasil)
hasil= not (b and b)
print('nilai',b,'nand',b,'adlah',hasil)

print('\n======ini nor======')
hasil= not (a or a)
print('nilai',a,'nor',a,'adlah',hasil)
hasil= not (a or b)
print('nilai',a,'nor',b,'adlah',hasil)
hasil= not (b or a)
print('nilai',b,'nor',a,'adlah',hasil)
hasil= not (b or b)
print('nilai',b,'nor',b,'adlah',hasil)

print('\n======ini nxor======')
hasil= a ^ a
print('nilai',a,'nxor',a,'adlah',not hasil)
hasil= a ^ b
print('nilai',a,'nxor',b,'adlah',not hasil)
hasil= b ^ a
print('nilai',b,'nxor',a,'adlah',not hasil)
hasil= b ^ b
print('nilai',b,'nxor',b,'adlah',not hasil)

print('========15')
a= 5
b= 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)
a= 6
b= 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

print('\n========15')
a= 5
b= 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
a= 6
b= 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

print('\n ========in')
nama = 'Bharuddin Jusuf Habibie'

test = 'rud'
cek = test in nama 
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'bach'
cek = test in nama 
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'ib'
cek = test in nama 
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'a'
cek = test in nama 
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'i'
cek = test in nama 
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'u'
cek = test in nama 
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'e'
cek = test in nama 
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'o'
cek = test in nama 
print(test,'terdapat di',nama,'adalah'+str(cek))

print('\n ========in')
data = ['institut','teknologi','baharuddin','jusuf','habibie']
print('data adalah',data)
test1 = 'habibie'
test2 = 'parepare'
test3 = 'kampus'
test4 = 'institut'

cek = test1 in data 
print(test1,'terdapat di data adalah'+str(cek))
cek = test2 in data 
print(test2,'terdapat di data adalah'+str(cek))
cek = test3 in data 
print(test3,'terdapat di data adalah'+str(cek))
cek = test4 in data 
print(test4,'terdapat di data adalah'+str(cek))

# INI OPERATOR BITWISE
a = 26
b = 4
b += 80
print('\n========AND')
print('nilai',a,'dalam biner           =',format(a,'08b'))
print('nilai',b,'dalam biner           =',format(b,'08b'))
print('----------------------------AND')
c = a & b
print('nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))

print('\n========== not In')
#tugas nama not in
nama = 'Muhammad Aprisal Sawal'
test = 'mad'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'muha'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ri'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n========== not In')
#Tugas dengan cara yang sama buat operator untuk not in
data=['Institut',
      'Teknologi',
      'Bacharuddin',
      'Jusuf',
      'Habibie']
print()
print('Data adalah',data)
test1='Habibie'
test2='Parepare'
test3='Kampus'
test4='Institut'
print()
cek=test1 not in data
print(test1,'Terdapat di data adalah',cek)
cek=test2 not in data
print(test2,'Terdapat di data adalah',cek)
cek=test3 not in data
print(test3,'Terdapat di data adalah',cek)
cek=test4 not in data
print(test4,'Terdapat di data adalah',cek)
print()
# Tugas Untuk Operator XOR c= a^n
print('=========================XOR')
print('Nilai',a,'Dalam biner           =',format(a,'08b'))
print('Nilai',b,'Dalam biner           =',format(b,'08b'))
print('-----------------------------------------------------XOR')
c= a ^ b
print('Nilai',a,'&',b,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT c= ~a
print('=========================NOT a')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------NOT a')
c= ~a
print('Nilai','~','\b',a,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT c= ~b
print('=========================NOT a')
print('Nilai',b,'Dalam biner         =',format(b,'08b'))
print('-----------------------------------------------------NOT a')
c= ~b
print('Nilai','~','\b',b,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator Geser Kanan, c= a>>2
print('=========================>>')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('----------------------------------------------------->>')
c= a>>2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator Geser kiri , c= a<<2
print('=========================<<')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------<<')
c= a<<2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT and, c= ~(a&b)
print('=========================not and')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------not and')
c=~(a&b)
print('Nilai','~(',a,'&',b,')','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT or, c= ~(a|b)
print('=========================not OR')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------OR')
c= ~(a|b)
print('Nilai','~(',a,'|',b,')','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator not xor, c = ~(a^b)
print('=========================not XOR')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('Nilai',b,'Dalam biner                =',format(b,'08b'))
print('-----------------------------------------------------not XOR')
c= ~(a ^ b)
print('Nilai ~(',a,'^',b,')Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk Operasi not geser kanan, c = ~(a >> 2)
print('=========================not Geser kanan')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kanan')
c= ~(a >> 2)
print('Nilai ~(',a,'>> 2)','Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk Operasi not geser Kiri, c = ~(a << 2)
print('=========================not Geser kanan')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kiri')
c= ~(a << 2)
print('Nilai ~(',a,'<< 2)','Dalam Biner Adalah',format(c,'08b'))
