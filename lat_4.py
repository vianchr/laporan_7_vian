# Buatlah suatu program mengetahui kata terpendek dan terpanjang dari suatu
# kalimat yang diinputkan! Misal: "red snakes and a black frog in the pool" Output: terpendek: a,
# terpanjang: snakes
kalimat ="red snakes and a black frog in the pool"
kata=kalimat.split(" ")
print (kata)
kata_pendek=kata_panjang=kata[0]

for kata in kata:
    if len(kata)<len(kata_pendek):
            kata_pendek=kata
    if len(kata)>len(kata_panjang):
            kata_panjang=kata
print(f" kata terpanjang adalah {kata_panjang} dan kata terpendek adalah {kata_pendek} ")

