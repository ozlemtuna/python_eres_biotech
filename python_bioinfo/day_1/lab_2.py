#Gerçek veriler

# Şimdiye kadar Python’da her şeyi ekranın içinde yazdık.
# Ama gerçek biyoinformatikte biz hiçbir zaman veriyi böyle yazmayız.
# Veri dışarıdan gelir: FASTA dosyası gelir, expression matrix gelir, VCF gelir.

# “Şimdi dosya okumayı yapacağız ama önce şunu netleştirelim:
# Python’da dosya açmanın iki yolu var.”
# “Teknik olarak ikisi de çalışır.
# Ama biyoinformatikte sadece bir tanesini kullanacağız.”
# “Çünkü biz:
# Büyük dosyalarla çalışıyoruz
# Hata olasılığı yüksek
# Pipeline yazıyoruz”

f = open("example.fasta")
data = f.read()
f.close

# “Bu kod çalışır.
# Ama burada üç büyük problem var.”
# Problem 1: Dosyayı kapatmayı unutabilirim
# “f.close() yazmayı unutursam, dosya bellekte açık kalır.”
# “Bu küçük dosyada problem olmaz ama:
# 10 GB’lık FASTA dosyasında sisteminiz kilitlenir.”
# Problem 2: Hata olursa dosya kapanmaz
# Problem 3: Temiz değil, güvenilir değil

with open("example.fasta") as f:
    data = f.read()
    
# with open dediğimizde Python’a şunu söylüyoruz:
# ‘Bu dosyayla işim bittiğinde,
# nasıl biterse bitsin, dosyayı sen kapat.’”
# “İster hata olsun
# ister hata olmasın
# dosya otomatik kapanır.”

with open("example.fasta") as f:
    for line in f:
        line = line.strip()
        print(line)
        
        
    for line in f:
# “Python dosyayı satır satır okur.”
# “Bu ne demek?”
# “10 GB’lık dosya varsa:
# RAM’e 10 GB yüklemez
# Sadece o anki satırı okur”

#    data = f.read()

# read() tüm dosyayı tek seferde belleğe alır.”
# “Küçük dosyada olur ama:
# FASTA
# BAM
# VCF
# gibi dosyalarda kullanılmaz.”

# with open("example.fasta") as f:
#     line_count = 0
#     for line in f:
#         line_count += 1
# print("Toplam satır:", line_count)

#raw dosyalar kirlidr
# with open("example.fasta") as f:
#     for line in f:
#         print("Ham satır:", repr(line))
#         clean  = line.strip()
#         print("Temiz satır:", repr(clean))

# #dosyayı tekrar okumak için
# with open("example.fasta") as f:
#     for line in f:
#         print(line.strip())

#     # 2. kez denemek
#     data = f.read()
#     print("read() sonrası:", repr(data))

# #seek(0) başa sarma
# with open("example.fasta") as f:
#     for line in f:
#         print(line.strip())

#     f.seek(0)
#     data = f.read()
#     print(data)

# # “Bu yöntem teknik olarak çalışır,
# # ama büyük dosyada tercih edilmez.”
# # “Biyoinformatikte her zaman:
# # ‘dosyayı tekrar açmak’
# # en temiz çözümdür.”

# # Biyoinformatik Dosya Okuma Kuralı
# # --------------------------------
# # 1) with open(...) as f:
# # 2) for line in f:
# # 3) line.strip()
# # 4) Belleğe asla tamamını read() ile alma
# # 5) Dosyayı bittiğinde Python otomatik kapatsın

# # “Gerçek bir FASTA dosyasında:
# # header satırı >
# # altındaki satırlar sekans
# # sekans birden fazla satır olabiliyor”
# # “Bu yüzden sadece satır okumak yetmez,
# # sekansları doğru şekilde biriktirmeyi bilmemiz lazım