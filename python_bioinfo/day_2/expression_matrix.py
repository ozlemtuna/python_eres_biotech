#Expression_matrix
#satırlar: genler, sütunlar: örnekler, hücreler: count/TPM/CPM
#bulk RNA-seq ve scRNA-seq

import pandas as pd 
data= {
    "Gene" : ["TP53", "EGFR", "MYC"],
    "Sample1" : [10.2, 4.5, 5.6],
    "Sample2" : [5.2, 4.7, 5.7],
    "Sample3" : [3.7, 8.9, 7.9]
}

df = pd.DataFrame(data).set_index("Gene") #set_index("Gene") -> genleri satır ismi yapar
print(df)

#[gene,sample]
#gen bazlı ortalama
print(df.mean(axis=1))

#sample bazlı toplam ifade
print(df.sum(axis=0))

#belirli genleri seç
print(df.loc[["TP53","EGFR"]])

#pandas+metadata+merge
#metadata: örneklerin klinik / deneysel bilgileri
#sample, condition, OS, Status
#merge neden gerekir: expression matrix sayısal, metadata anlamsal bilgidir analiz için ikisini birleştirmek gerekir

meta = pd.DataFrame({
    "Sample": ["Sample1", "Sample2", "Sample3"],
    "Condition": ["Tumor", "Normal", "Tumor"]
})
expr = df.T
expr["Sample"] = expr.index

merged = expr.merge(meta, on="Sample")
print(merged)

#.T -> expression matrix transpose

#merged.groupby("Condition").mean()

#histogram:gen uzunluğu
from python_bioinfo.day_1.fasta_parser import parse_fasta_file, gc_content
records = parse_fasta_file("/Users/ozlemtuna/Desktop/ERES_Biotech/python_bioinfo/example.fasta")

import matplotlib.pyplot as plt 
lengths = [len(seq) for seq in records.values()]
plt.hist(lengths, bins=10)
plt.xlabel("Sequence Length")
plt.ylabel("Count")
plt.title("FASTA Length Distribution")
#plt.show()

#Boxplot - GC content
gcs = [gc_content(seq) for seq in records.values()]
plt.boxplot(gcs)
plt.ylabel("GC Content")
#plt.show()

#k-mer: DNA dizisini k uzunluğunda parçalara bölmek
# ATGCGT, k=3
# -> ATG, TGC, GCG, CGT

from collections import Counter
def count_kmers(seq, k=3):
    return Counter(seq[i:i+k] for i in range(len(seq)-k+1)
                   if "N" not in seq[i:i+k])

#fasta üstünde uygulama
all_kmers = Counter()
for seq in records.values():
    all_kmers.update(count_kmers(seq, k=3))
    
print(all_kmers.most_common(10))



