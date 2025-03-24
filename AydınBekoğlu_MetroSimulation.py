from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        # BFS algoritması kullanarak en az aktarmalı rotayı bulur (en kısa yolu bulmada kullanılan bir arama algoritmasıdır.)
        

        # Başlangıç ve hedef istasyonların varlığı kontrol edildi.
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        kuyruk = deque([(baslangic, [baslangic])]) # collections.deque kullanarak bir çift uçlu kuyruk oluşturduk. 
        
        # Ziyaret edilen İstasyonları takip etmek için "ziyaret_edildi" set/küme oluşturduk. İlk olarak içine başlangıcı ekledik.
        ziyaret_edildi = {baslangic}

        while kuyruk:
            mevcut, yol = kuyruk.popleft() # yol => Başlangıçtan mevcuta kadar olan rota

            if mevcut == hedef: # Hedefe ulaşıldığında mevcut yolu/path döndürüyoruz.
                return yol  
            
            # Ziyaret edilen istasyonları takip edebilmek için "ziyaret_edildi" kümesine ekliyoruz mevcut istasyonumuzu.
            if mevcut not in ziyaret_edildi:
                ziyaret_edildi.add(mevcut)

            # Her adımda komşu istasyonları keşfederiz.
            for komsu, _ in mevcut.komsular:
                if komsu not in ziyaret_edildi:
                    kuyruk.append((komsu, yol + [komsu])) # Yeni yolu kuyruğa ekliyoruz.

                    ziyaret_edildi.add(komsu) # Ziyaret edilen komşuları ekliyoruz.
        
        return None # Rota bulunamazsa, hedefe ulaşılamazsa None döndürür.
              


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
         # A* algoritması kullanarak en hızlı rotayı bulur (toplam süre açısından en kısa yolu bulmak)
         # En kısa yolu bulmada en verimli yöntemlerden biridir.
        
         # En düşük süreye sahip rotayı seçin

        # Başlangıç ve hedef istasyonların varlığını kontrol edildi
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = [(0, id(baslangic), baslangic, [baslangic])] # heapq modülünü kullanarak bir öncelik kuyruğu oluşturduk.
        
        #  Her eleman: (şu ana kadar geçen süre, istasyonun IDsi, mevcut istasyon, gidilen rota) olamk üzere 4 parametreden oluşur.


        # Ziyaret edilen istasyonları ve süreleri takip etmek için bir sözlük oluşturduk.
        ziyaret_edildi = {}

        while pq:
            sure, _, mevcut, yol = heapq.heappop(pq) # Öncelik kuyruğundan en düşük süreli yolu çıkarıyoruz/seçiyoruz.

            if mevcut in ziyaret_edildi and ziyaret_edildi[mevcut] <= sure: # Eğer öncesinden daha düşük süreli ziyaret varsa ekleme işlemi atlanır.
                continue

            ziyaret_edildi[mevcut] = sure # Mevcut istasyon için en düşük süreyi ekliyoruz.

            if mevcut == hedef: # Hedefe ulaşıldığında mevcut yolu/path ve süreyi döndürüyoruz.
                return yol, sure
            
            # Her adımda komşu istasyonları keşfederiz.
            for komsu, ek_sure in mevcut.komsular:
                yeni_sure = sure + ek_sure # Her adımda toplam süreyi hesaplıyoruz.
                heapq.heappush(pq, (yeni_sure, id(komsu), komsu, yol + [komsu]))
        
        return None # Rota bulunamazsa, hedefe ulaşılamazsa None döndürür.


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 