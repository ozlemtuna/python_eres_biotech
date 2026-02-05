#gerçek veri ile expression matrix
import pandas as pd 
df = pd.read_csv("/Users/ozlemtuna/Desktop/ERES_Biotech/python_bioinfo/expression.csv") # gerçek biyolojik veriyi pythona alır
print(df.head()) #ilk 5 satırı gösterir
print(df.shape) #kaç gen, kaç örnek var onu gösterir

#gen odaklı filtreleme
tp53 = df[df['gene'] == 'TP53']
print(tp53)

meta = pd.read_csv("/Users/ozlemtuna/Desktop/ERES_Biotech/python_bioinfo/metadata.csv")

#plot için long format şarttır
long_df = df.melt(id_vars="gene", var_name="sample", value_name="expression")
merged = long_df.merge(meta, on="sample")
print(merged.head())
#artık ekspression + biyolojik bilgi tek tabloda

#numpy ile bilimsel hesaplama
#hızlı, vektörel, RNA-seq dünyasının temeli
import numpy as np 
#log dönüşümü
merged['log_expr'] =np.log2(merged['expression'] + 1)
print(merged)
#+1 sıfır koruması
#log dağılımı normalize eder

stats = merged.groupby('condition')['log_expr'].agg(['mean','std'])
print(stats)
#Expression değerlerini log2 dönüşümüyle normalize edip, Tumor ve Normal gruplarını istatistiksel olarak özetlemek.
# Çok büyük–çok küçük değerler içerir
# Log alınmazsa analizler yanıltıcı olur
# RNA-seq’te standarttır
# Tumor mean > Normal mean
# → Gen tümörde daha yüksek
# Std büyükse
# → Örnekler arasında fark fazla

#Seaborn ile bilimsel görselleştirme
import seaborn as sns 
import matplotlib.pyplot as plt 
sns.histplot(data=merged, x='log_expr', hue='condition', bins=20)
plt.title("Expression Distribution")
#plt.show()

#boxplot 
sns.boxplot(data=merged, x='condition',y='log_expr')
plt.title("Tumor vs Control Expression")
#plt.show()




