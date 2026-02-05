#pandas
#neden numpy yetmez
#numpy sayıları sever ama bizim biyoinformatik verilerinde expression matrix, annotation table, metadata hepsi tablo
#programlanabilir excell gibi
#temel yapı DataFrame
import pandas as pd 

#fasta sonuçlarını DataFrame'e dönüştürme
#satır=gözlem, kolon=özellik

from python_bioinfo.day_1.fasta_parser import parse_fasta_file, gc_content

records = parse_fasta_file("example.fasta")
rows = []
for hid, seq in records.items():
    row = {
        "id": hid, 
        "length": len(seq),
        "gc": gc_content(seq)
    }
    rows.append(row)
    
#her fasta kaydı 1 satır, biyolojik özellik kolon

#DataFrame oluştur
df = pd.DataFrame(rows)

#filtreleme
df[df["length"] > 200]
#sıralama
df.sort_values("gc", ascending=False)

#özel istatistik
df.describe()
#ortalama, standart sapma, min/max verir

#csv yazma:
df.to_csv("fasta_summary.csv", index=False)


