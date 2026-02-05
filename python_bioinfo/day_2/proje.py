#TP53 geninin tumor ve control örneklerde ekspresyon farkının analizi
#amaç: bir genin (TP53) biyolojil dizisini tanımak, GC içeriğini hesaplamak, gen ekspresyonu PANDAS ile analiz etmek,
#klinik bilgiyle birleştirmek, istatiksel dönüşüm uygulamak, sonucu grafikle göstermek

from python_bioinfo.day_1.fasta_parser import parse_fasta_file, gc_content

records = parse_fasta_file("/Users/ozlemtuna/Desktop/ERES_Biotech/python_bioinfo/tp53.fasta")  #fasta: biyolojik bilginin en ham hali
tp53_seq = records["TP53_human"]

print("TP53 length:", len(tp53_seq))
print("TP53 GC content:", gc_content(tp53_seq)) #gc içeriği: gen stabilitesi, regülasyon, teknik bias

#pandas ile veri okuma
import pandas as pd 
expr = pd.read_csv("/Users/ozlemtuna/Desktop/ERES_Biotech/python_bioinfo/proje_expression.csv")
meta = pd.read_csv("/Users/ozlemtuna/Desktop/ERES_Biotech/python_bioinfo/proje_metadata.csv")

print(expr) #expression sayısal biyolojik ölçüm
print(meta) #metadata klinik/deneysel bağlam

#pandas merge 
df = expr.merge(meta, on="sample_id")
print(df) #biyolojik analiz = veri bağlam

#NumPy ile log dönüşümü
import numpy as np 
df["log_expression"] = np.log2(df["expression"] + 1)
print(df) #RNA-seq/expression verileri log olmadan yorumlanmaz, büyük değerleri normalize eder, istatistiğe hazırlar

#Seaborn ile görselleştirme

import seaborn as sns 
import matplotlib.pyplot as plt 

sns.boxplot(data=df, x="condition", y="log_expression")

plt.title("TP53 Expression: Tumor vs. Control")
plt.ylabel("log2(Expression + 1)")
plt.xlabel("Condition")
plt.show()

#hangisi daha yüksek?
#TP53 geninin tumor örneklerinde ekspresyonu control grubuna göre daha yüksektir.


# “Bir sonraki adım diferansiyel ekspresyon analizidir”
