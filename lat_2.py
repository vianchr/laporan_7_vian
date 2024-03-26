kata= "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata=kata.lower()
kata=''.join([i for i in kata if i.isspace() or i.isalpha()])
kata=kata.split(' ')
total=0
for x in ['makan']:
    jml = kata.count(x)
    # jml=a_string.count(x)
    total += jml
print(total) #hasil = 4


