import os
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def load_or_make_example(path="DEG_results.csv", n=1000, seed=42):
    """
    Eğer path diye bir CSV varsa onu oku,
    yoksa gerçekçi örnek yap
    """
    if os.path.exists(path):
        df = pd.read_csv(path)
        print(f"Loaded {path} with {len(df)} rows.")
        return df
    np.random.seed(seed)
    df = pd.DataFrame({
        "gene": [f"Gene_{i}" for i in range(n)],
        "log2FoldChange": np.random.normal(0,2,n),
        "padj": np.clip(np.random.beta(0.8,10,n), 1e-10,1.0)
    })
    df.to_csv(path, index= False)
    print(f"Example file created at {path}")
    return df

def compute_volcano_metrics(df, padj_col="padj", lfc_col="lpg2FoldChange",
                            p_cutoff=0.05, lfc_cutoff=1.0):
    """
    - y = -log10(padj) hesapla
    - status ekle
    """
    eps = 1e-300
    df = df.copy()
    df["y"] = -np.log10(np.maximum(df[padj_col].astype(float),eps))
    df["status"] = "NS"
    df.loc[(df[lfc_col] > lfc_cutoff) & (df[padj_col] < p_cutoff), "status"] = "UP"
    df.loc[(df[lfc_col] < -lfc_cutoff) & (df[padj_col] < p_cutoff), "status"] = "DOWN"
    return df

def plot_volcano(df, lfc_col="log2FoldChange", y_col="y", gene_col="gene",
                p_cutoff=0.05, lfc_cutoff=1.0, top_n=10, figsize=(6,5),
                title="Volcano Plot"):
    """
    -df: metricleri hesaplanmis dataframe
    -top_n: en yüksek y değerlerine göre etiketlenecek gen sayisi
    """
    colors = {"UP":"red", "DOWN":"blue", "NS":"grey"}
    markers = {"UP":"o", "DOWN":"o", "NS":"o"}
    
    fig, ax = plt.subplots(figsize=figsize)
    
    #her grup için ayrı scatter
    for status in ["NS","DOWN","UP"]:
        mask = df["status"] == status
        ax.scatter(df.loc[mask, lfc_col],
                   df.loc[mask, y_col],
                   s=20, #nokta büyüklüğü
                   alpha=0.7, #saydamlık
                   label=status,
                   marker=markers[status],
                   color=colors[status])
    
    #cutoff çizgileri
    ax.axvline(lfc_cutoff, linestyle="--", linewidth=1)
    ax.axvline(-lfc_cutoff, linestyle="--", linewidth=1)
    ax.axhline(-np.log10(p_cutoff), linestyle="--", linewidth= 1)
    
    #axis etiketleri ve başlık
    ax.set_xlabel("log2 Fold Change")
    ax.set_ylabel("-log10 adjusted p-value")
    ax.set_title(title)
    
    #en anlamli genleri etiketle
    top_genes = df.sort_values(by=y_col, ascending=False).head(top_n)
    for _, row in top_genes.iterrows():
        ax.text(row[lfc_col], row[y_col] + 0.5, row[gene_col],
                fontsize=6, ha="center", va="bottom")
        
    ax.legend(frameon=False, fontsize=8)
    ax.set_xlim(df[lfc_col].quantile(0.01)-0.5, df[lfc_col].quantile(0.99) +0.5)
    ax.set_ylim(-0.5, df[y_col].max()+1.0)
    plt.tight_layout()
    return fig,ax

if __name__ == "__main__":
    #1) Veriyi oku veya örnek oluştur
    df = load_or_make_example("DEG_results.csv")
    
    #2) Metriği hesapla (y ve status)
    df = compute_volcano_metrics(df, padj_col="padj", lfc_col="log2FoldChange",
                                p_cutoff=0.05, lfc_cutoff=1.0)
    
    #3) Çiz
    fig, ax = plot_volcano(df, lfc_col="log2FoldChange", y_col="y", gene_col="gene",
                        p_cutoff=0.05, lfc_cutoff=1.0, top_n=12,
                        title="Volcano - example / your data")
    
    fig.savefig("volcano_example.pdf", dpi=300, bbox_inches="tight")
    fig.savefig("volcano_example.png", dpi=300, bbox_inches="tight")
    
    plt.show()