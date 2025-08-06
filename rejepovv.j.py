# def toliq_ati(ati,familyasi):
#     """Paydalaniwshinin' atin ham familyasin qaytaradi"""
#     print(f"Paydalaniwshinin' ati: {ati.title()}\n"
#           f"Paydalaniwshinin' familyasi: {familyasi.title()}")
# toliq_ati("Jaras", "Rejepov")

# def jas_esaplaydi(tuwilgan_jili, kazirgi_jil=2025):
#     """ Paydalaniwshinin' jasin qaytaradi """
#     print(f"Siz {kazirgi_jil-tuwilgan_jili } jasdasiz")
# jas_esaplaydi(1999,2023)
# jas_esaplaydi(1999)

# def toliq_ati(ati, familyasi):
#     """Paydalaniwshinin' atin ham familyasin qaytaradi"""
#     at_fam = f"{ati.title()} {familyasi.title()}"
#     return at_fam
# natija=toliq_ati("Jaras", "Rejepov")
# print(natija)

# def araliq(min,max,araliq=1):
#     sanlar = []
#     while min<max:
#         sanlar.append(min)
#         min += araliq
#     return sanlar
# print(araliq(1,20,3))


# a,b=map(int,input("A ham B sanlar kiritin:").split())
# c=1
# for i in range(a,b+1):
#     if i==b:
#         print(i,end="\n")
#     else:
#         print(i,end=" ")
#         c+=1
# print(f'ortasinda {c} san bar')
    
# a,n=map(int,input("A ham B sanlar kiritin:").split())
# summa=1
# for i in range(1,n+1):
#     dareje=a**i
#     summa+=dareje
# print(summa)
    







# print("Jaqin doslar dizler")
# atlari=[]
# n =1
# while True:
#     soraw = f"{n}) dostinizdin atin jazin?:"
#     ati = input(soraw)
#     atlari.append(ati)
#     qaytalaw=input("jane dos qosasizba? (yaq/awa) ")
#     n += 1
#     if qaytalaw== 'yaq':
#         break
# san = 0
# while san  <= 1:
#     print(san, end=" ")
#     san += 1
# print('Dastur tawsildi')


# import random

# def santap(x=10):
#     shama_san = random.randint(1, x)
#     print(f"Men 1 den {x} shekem san oyladim. Tawalasizba?", end="")
#     shamalar = 0
#     while True:
#         shamalar += 1
        
#         shama = int(input(">>>"))
#         if shama < shama_san:
#             print("Ulkenlew san aytin':", end="")
#         elif shama > shama_san:
#             print("Kishlew san aytin:", end="")
#         else:
#             print("You win!")
#             break
#     print(f"Qutliqlayman. {shamalar} marte shama menen tawdiniz")
#     return shamalar
# santap()
# import random
# def santap_pc(x=10):
#      input(f"1 den {x} shekem san oylan ham qalegen tuymeni basin'. Men tawaman.")
#      tomen = 1
#      joqari = x
#      shamalar = 0
#      while True:
#          shamalar += 1
#          if tomen != joqari:
             
#              shama = random.randint(tomen, joqari)
#          else:
#              shama = tomen
#          juwap = input(f"siz {shama} sanin' oyladiniz: duris bolsa (t),"
#             f"Men oylagan san budan ulken bolsa (+), yaki Kishi bolsa (-)".lower())
#          if juwap == "-":
#             joqari = shama - 1
#          elif juwap == "+":
#             tomen = shama + 1
#          else:
#             break 
#      print(f"Men {shamalar} marte shama menen tawdim!")
#      return shamalar

# santap_pc()

        







































































