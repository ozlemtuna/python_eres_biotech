print("Hello Bioinformatics")

#Python Temelleri (değişkenler, tipler, listeler, döngüler)

#Değişkenler ve tipleri
name = "Özlem"
age = 25
pi = 3.14

print(name, type(name))
print(age, type(age))
print(pi, type(pi))

#Liste ve for döngüsü
genes = ["TP53", "EGFR", "KRAS", "BRCA1"]
for gene in genes:
    print(gene, len(gene))
    
genes.append("MYC") #tekli ekleme
print(genes)
genes.extend(["PTEN", "CDK2"]) #çoklu ekleme
print(genes)
genes.remove("KRAS") #eleman çıkarma
print(genes)
genes.remove("ABC") #eleman çıkarma
print(genes)
genes.pop(1)
print(genes)


#Dictionary : gene expression
expr = {"TP53" : 10.5, "EGFR" : 2.1, "KRAS": 7.3}
for gene, val in expr.items():
    print(gene, "->", val)
print(expr)
#yeni ekleme
expr["BRCA1"] = 5.2
for gene, val in expr.items():
    print(gene, "->", val)
#değiştirme
expr["TP53"] = 12.0
print(expr)

#silme 
del expr["EGFR"]
print(expr)

#koşul + liste filtreleme
high = [gene for gene, v in expr.items() if v > 5]
print("High expression:", high)

high = []
for gene, v in expr.items():
    if v > 7:
        high.append(gene)
print(high)


#practice
genes = ["TP53", "EGFR", "KRAS", "MYC", "PTEN", "BRCA1"]
long_genes = [gene for gene in genes if len(gene) > 4]
print("Long genes:", long_genes)

long_genes_2 = []
for gene in genes:
    if len(gene) > 4:
        long_genes_2.append(gene)
print("Long genes (loop):", long_genes_2)

#İki yöntem de aynı sonucu verir; comprehension kısadır, döngü daha açıklayıcı.
cancer_types = ["lung", "breast", "colon", "brain"]
cancers = [cancer_type for cancer_type in cancer_types if len(cancer_type) == 5]
print("Cancers:", cancers)

cancer_types = ["lung", "breast", "colon", "brain"]
unmatch_cancers = [cancer_type for cancer_type in cancer_types if len(cancer_type) != 5]
print("Unmatch Cancers:", unmatch_cancers)

#fonksiyonlar
def gc_content(seq):
    seq = seq.upper() # büyük harf
    if len(seq) == 0: #boş dizi koruması
        return None
    gc = seq.count("G") + seq.count("C") # G ve C sayısı
    return gc / len(seq) 

sequnces = ["ATGCCG", "tctgcat", ""]
for s in sequnces:
    print(f"Seq: {s!r} -> GC: {gc_content(s)}")

#!r repr() boşluk var mı string var mı kontrol ediyor 
s = "ATGC "
print(s)
ATGC
print(f"{s!r}")
'ATGC '


#veride n ya da başka harfler olabilir
def gc_content_clean(seq):
    seq = seq.upper()
    nucs = [c for c in seq if c in ("A", "T", "G", "C")]
    if len(nucs) == 0:
        return None
    gc = nucs.count("G") + nucs.count("C")
    return gc/len(nucs)
sequnces = ["ATGCCG", "tctgcat", ""]
for s in sequnces:
    print(f"Seq: {s!r} -> GC: {gc_content(s)}")

#gc_content("GCGTAA") çalıştırın #0.5
def gc_content_clean(seq):
    seq = seq.upper()
    nucs = [c for c in seq if c in ("A", "T", "G", "C")]
    if len(nucs) == 0:
        return None
    gc = nucs.count("G") + nucs.count("C")
    return gc/len(nucs)
sequnces = ["GCGTAA"]
for s in sequnces:
    print(f"Seq: {s!r} -> GC: {gc_content(s)}")
    
    
# multiline string ile demo
fasta_text = """>seq1
ATGCGCGTATCGA
>seq2
TCGCGATCGATCGATCGA
"""
#satır satır oku
records = {}  # boş dict oluşturduk
current_header = None
for line in fasta_text.splitlines(): #satır satır dolaş
    line =line.strip()   #baş/son boşluğu kaldır  
    if not line:
        continue   #boş satır atla 
    if line.startswith(">"):    #header satırı mı?
        current_header = line[1:] #'>' işaretini at
        records[current_header] = [] #yeni liste başlatıcaz
    else:
        records[current_header].append(line) #sekans satırını ekle
print(records)
# join seqs ve GC hesapla:
for h, seq_lines in records.items():   #headera ait olan satır listesini al
    seq = "".join(seq_lines)
    print(h,seq, "len:" ,len(seq), "GC:" , gc_content(seq) )

"".join(...) ne yapar?
"".join(["ATGC", "GCTA"])
"ATGCGCTA"


#gerçek data bul yap

# IndentationError: Python girintiye duyarlı; 4 boşluk veya tab seç, karıştırma.
# NameError: Değişken tanımlanmadan kullanılmış. Sıralamayı kontrol et.
# FileNotFoundError: Dosya yolu yanlış. pwd / ls ile doğrula.
# KeyError: dict içinde olmayan anahtar. in ile kontrol et veya get() kullan.
# TypeError: yanlış tiple işlem yapılmış (örn. None ile len()). Tip kontrolü ekle.
