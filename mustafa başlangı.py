
def is_ascii(text):
    try:
        text.encode('ascii')
        return True
    except:
        return False


print("lütfen kullanıcı adınızı ve parolanızı belirleyiniz!!!"
      "(kullanıcı adı ve parolanızın karakter toplamı 30 u geçmemelidir")

kullanıcı_adı = input("kullanıcı adınızı giriniz : \t")
parola =("\nparolanızı giriniz : \t")

if not is_ascii(kullanıcı_adı):
    print('Lutfen turkce karakter kullanmayın')
    quit()

print("========================================"
      "TURGUT MOTOR BAKIM SERVİSİNE HOŞGELDİNİZ"
      "========================================"
      "YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ:"
      "1) motor bakım servisi"
      "2) motor yedek parça"
      "3) elimizdeki parçalar"
      "4) çıkış"
      "========================================\n")



