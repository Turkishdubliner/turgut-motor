while True:
    def is_ascii(text):
        try:
            text.encode('ascii')
            return True
        except:
            return False


    print("lütfen kullanıcı adınızı ve parolanızı belirleyiniz!!!\n"
          "(kullanıcı adı ve parolanızda turkce karakter kullanmayınız\n")

    kullanıcı_adı = input("kullanıcı adınızı giriniz : \t")
    parola = input("\nparolanızı giriniz : \t")


    if not is_ascii(kullanıcı_adı):
        print('Lutfen turkce karakter kullanmayın\n')
        quit()
    if not is_ascii(parola):
        print("lutfen turkce karakter kullanmayın\n")
        quit()


    print("========================================\n"
          "TURGUT MOTOR BAKIM SERVİSİNE HOŞGELDİNİZ\n"
          "========================================\n"
          "1) motor bakım servisi\n"
          "2) motor yedek parça servisi\n"
          "3) elimizdeki parçalar\n"
          "4) çıkış\n"
          "========================================\n")
    seçim = input("YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ:   \n")
    if seçim == "1":
        file1 = open("file1.txt", encoding='utf-8')
        print(file1.read())
        file1.close()
    elif seçim == "3":
        file2 = open("file2.txt",encoding='utf-8')
        print(file2.read())
        file2.close()
    elif seçim == "2":
        file3 = open("file3.txt",encoding='utf-8')
        print(file3.read())
        file3.close()

