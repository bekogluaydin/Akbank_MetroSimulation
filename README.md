# Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu) 

Bu proje, **Akbank Python ve Yapay Zekaya Giriş Bootcamp** kapsamında geliştirilmesi beklenen, bir metro ağı içinde **en hızlı** ve **en az aktarmalı** rotayı bulmaya yönelik bir simülasyondur.

## 📌 A. Kullanılan Algoritmalar

1. **BFS (Genişlik Öncelikli Arama - Breadth First Search)** => En az aktarmalı rotayı bulmak için kullanıldı.
2. **A\* (A-Star)** => En hızlı rotayı, en kısa sürede tamamlanan güzergahı bulmak için kullanıldı.

## 🛠️ B. Kullanılan Teknolojiler ve Kütüphaneler

Bu projede **Python** dili kullanılarak **graf veri yapısı** ile metro ağı modellenmiştir.

**Kütüphaneler:**
1. **collections.deque** => BFS kuyruğu oluşturmak için
2. **heapq** => A* algoritmasında öncelik kuyruğu oluşturmak için
3. **typing** => Tip belirleyici (List, Dict, Tuple, Optional) kullanımı

## 🧠 C. Algoritmaların Çalışma Mantığı

### 1️⃣ BFS (Breadth First Search - En Az Aktarmalı Rota)

📌 **Amaç**: **İstasyonlar arasındaki en az aktarmalı rotayı bulmak**  

> #### Adım Adım Çalışma Mantığını Özetliyelim:
1. Kuyruk oluşturulur (deque).
2. Başlangıç istasyonu kuyruğa eklenir.
3. Kuyruk boşalana kadar döngü devam eder:
   + İlk eleman kuyruktan çıkarılır.
   + Eğer hedefe ulaşıldıysa, rota döndürülür.
   + Komşu istasyonlar kuyruğa eklenir.

> #### Neden BFS (Breadth First Search - En Az Aktarmalı Rota) ?
BFS, **en az geçiş (minimum aktarma)** için **en uygun algoritmadır**. Çünkü **katman katman** genişleyerek **en kısa yolu** bulur.

<hr>

### 2️⃣ A* (A Star - En Hızlı Rota)

**Amaç**: **İstasyonlar arasındaki en kısa sürede ulaşılabilecek rotayı bulmak** 

> #### Adım Adım Çalışma Mantığını Özetliyelim:
1. Öncelik kuyruğu (heapq) oluşturulur.
2. Başlangıç istasyonu kuyruğa eklenir.
3. Kuyruk boşalana kadar döngü devam eder:
   + En kısa sürede ulaşılabilen istasyon seçilir.
   + Eğer hedefe ulaşıldıysa, rota döndürülür.
   + Komşu istasyonlar kuyruğa eklenir ve toplam süre hesaplanır.
  
> #### Neden A* ?
\* algoritması, **en kısa süreyi garanti eder.** **Öncelik kuyruğu (`heapq`)** kullanarak **her zaman en hızlı yolu tercih eder.**  

## 📊 D. Örnek Kullanım ve Test Sonuçları 
***Test Senaryosu 1: AŞTİ → OSB***

```python
rota = metro.en_az_aktarma_bul("M1", "K4")
print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
```

![Örnek Kullanım ve Test Sonuçları](https://github.com/user-attachments/assets/86313a69-5431-4ba3-9191-370744e64aef)

## E. Projeyi Geliştirme Fikirleri

1. Metro hattının görselleştirilmesi (Matplotlib veya NetworkX kullanarak graf üzerinde metro ağı çizilebilir)
2. Gerçek dünya verileri ile çalışma (İstanbul veya Ankara metrosu gibi)
3. Yoğunluk bazlı hız hesaplamaları, farklı saat dilimlerinde seyahat süresi değişebilir (örneğin: sabah ve akşam yoğun saatler).
