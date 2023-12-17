a = True

while a:
    jawab = input('Apakah Ingin Lanjutkan? (y/n)')
    if jawab == 'y':
        print('Terima Kasih >_<')
        a = True
    elif jawab == 'n':
        print('Sampai Jumpa :D')
        a = False
    else:
        print('Jangan Aneh Blok -_-')
        a = True
        
