# “Şu ana kadar ne yaptık?
# FASTA dosyasını okuduk, sekansları temizledik, GC hesapladık.
# Ama dikkat edin:
# Sonuçlar şu an sadece Python dict içinde.
# Gerçek biyoinformatikte analiz burada bitmez.
# Biz bu sonuçları:
# karşılaştırmak
# filtrelemek
# sıralamak
# kaydetmek
# isteriz.
# İşte burada numpy ve pandas devreye giriyor.”

#Neden NumPy?
# pythonda normal liste: 
lengths = [100,200,300] # bu sadece bir liste
#python bunu eleman eleman işler.
#numpy ise:
import numpy as np 
lengths = np.array([100,200,300])
#bu tek parça sayısal veri gibi davranır.
#biyoinformatikte neden önemli?
#binlerce gen, on binlerce hücre, yüz binlerce sekans
#python yavaş, numpy hızlı ve matematiksel

#numpy neyi değiştiriyor? 
#python listesi ile:
gc_values= [0.42, 0.51, 0.39]
total = 0
for x in gc_values:
    total += x
mean_gc = total / len(gc_values)
print(mean_gc)
#numpy ile
gc = np.array([0.42,0.51,0.39])
numpy_mean_gc = gc.mean()
print(numpy_mean_gc)

#hatayı azaltır, kodu sadeleştirir, döngüyü gizler

#fasta çıktıısının numpya bağlayalım

from python_bioinfo.day_1.fasta_parser import parse_fasta_file, gc_content

records = parse_fasta_file("example.fasta")
lengths = []
for seq in records.values():
    lengths.append(len(seq))
    
lengths = np.array(lengths)
print(lengths)

mean = lengths.mean()
print(mean)
print(lengths.mean())
print(lengths.min())
print(lengths.max())


#filtreleme:
print(lengths[lengths > 20])

