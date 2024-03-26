#anagram
kata_1=input("masukan kata pertama:")
kata_2=input("masukan kata kedua:")
def anagram(kata_1,kata_2):
    kata_1=kata_1.lower()
    kata_1= ''.join([i for i in kata_1 if i.isalpha()])
    kata_2=kata_2.lower()
    kata_2= ''.join([i for i in kata_2 if i.isalpha()])
    kata_1=kata_1[::-1]
    if kata_1==kata_2:
        print("merupakan anagram")
    else:
        print("bukan angram")
    
anagram(kata_1,kata_2)

    