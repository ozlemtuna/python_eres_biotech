#FASTA PARSER

#fasta dosyalarıını perse edeceğiz
#duplicate header, boş satır, satır içi boşluk, küçük/büyük harf, N bunlar olabilir 
#gedef: hatalara dayanıklı (robust) bir parser yazmak

#satır satır oku > ile başlayan satırları header, diğer sequence.
#header geldiğinde önceki kaydı bitir ve kaydet. Sequence satırlarını liste olarak topla - en sonda ''.join() ile birleştiriyoruz.

from typing import Dict,Tuple,Iterator
import sys

def parse_fasta_lines(lines: Iterator[str]) -> Dict[str, str]:
    """line: iterable of lines (already stripped or raw)
    returns: dict mapping header -> seq (joined string)
    """
    records = {}
    current_header = None
    for raw in lines:
        line = raw.strip() #baş/son boşlık ve yeni satır karakterlerini temizliyoruz
        if not line:
            #boş satırları atla
            continue
        if line.startswith(">"):
            header = line[1:].split()[0] #sadece ilk token ID
            #duplicate header handling: suffix ekle
            if header in records:
                i = 1
                new_header = f"{header}_dup{i}"
                while new_header in records:
                    i += 1 # i = i +1 
                    new_header = f"{header}_dup{i}"
                header = new_header
            records[header] = [] #sekans satırlarını topladığımız yer
            current_header = header
        else: 
            if current_header is None:
                raise ValueError("FASTA format error: sequence line seen before any header")
            records[current_header].append(line.upper()) #büyük harfe çevir
    #join
    for h in list(records.keys()):
        records[h] = "".join(records[h])
    return records

#encoding = utf-8 dosyayı hangi dilde hangi karakterler setinde okuyacağını söylüyoruz python'a 
#bu dosya türünde her türlü karakter olabilir, ben onları doğrı okuyayım
#ASCII dar UTF-8 dünya dillerindeki tüm karakterleri destekleyen uluslararaso bir kodlama standardı

#"seq1_id" : "ATCGAGCTC...."

def parse_fasta_file(path:str) -> Dict[str, str]:
    with open(path, "r", encoding="utf-8") as f:
        return parse_fasta_lines(f)
    

def gc_content(seq: str) -> float:
    if not seq:
        return 0.0
    nucs = [c for c in seq if c in ("A", "T", "G", "C")]
    if len(nucs) == 0:
        return 0.0
    gc = nucs.count("G") + nucs.count("C")
    return gc / len(nucs)

def fasta_to_table(path_in: str, path_out: str, sep: str = ",") -> None: #sonuçları tsv/csv
    records = parse_fasta_file(path_in) #fasta dosyasını okuyup dict döndürüyor #  "seq1": "ATGCGTAA"
    with open(path_out, "w", encoding="utf-8") as out:  #çıkıt dosyasını yazma modunda aç
        out.write(sep.join(["id","lenght", "gc"]) + "\n") # csv dsoyasına başlık yazıyor
        for hid, seq in records.items():   #tüm fasta kayıtlarında döngü hid: header , seq: nükleotid dizisi
            out.write(sep.join([hid, str(len(seq)), f"{gc_content(seq):.4f}"]) + "\n") #her sekans için şu blgileri yazıyor: id, sekans uzunluğu, 4 ondalık gc yüzdesi
if __name__ == "__main__":  #bu dosya direkt çalıştırıldığında aşaküdaki kod çalışsın
    if len(sys.argv) < 3:  #komut satırına yeterli argüman veirlmezse uyarı ver
        print("Usage: python fasta_parser.py input.fasta output.csv")
        sys.exit(1)
    fasta_to_table(sys.argv[1],sys.argv[2]) #fonksiyonu gerçek parametrelewrle çalıştır 
    
#sys.argv[1] → input.fasta
#sys.argv[2] → output.csv


#python fasta_parser.py example.fasta example_summary.csv


# with open(path) as f: → kullan
# for line in f: → satır satır oku
# line.strip() → temizle
# line.startswith(">") → header
# records[hdr].append(line) → satır satır topla, sonra ''.join()
# len(seq) ve gc_content(seq) → özetle