import librosa
import os

# Veri setindeki ilk 'blues' şarkısının yolunu belirtelim
# Eğer dosya yapın farklıysa buradaki "Data/blues/..." kısmını kendine göre düzenle
dosya_yolu = r"C:\Users\goygo\Desktop\MuzikTuruTanima\Data\blues\blues.00000.wav"

print("Sistem kontrol ediliyor...\n" + "-"*30)

# Dosya gerçekten orada mı kontrol edelim
if os.path.exists(dosya_yolu):
    print(f"✅ Harika! Dosya bulundu: {dosya_yolu}")
    
    # Sesi librosa ile yükleyelim
    print("⏳ Ses dosyası yükleniyor (bu birkaç saniye sürebilir)...")
    
    # y: sesin dalga formu verisi, sr: sample rate (örnekleme hızı)
    y, sr = librosa.load(dosya_yolu, sr=None) 
    
    # Süreyi hesaplayıp yazdıralım (Veri boyutu / Örnekleme hızı = Saniye)
    sure = len(y) / sr
    
    print("-" * 30)
    print("🎉 TEST BAŞARILI!")
    print(f"🎵 Şarkının uzunluğu: {sure:.2f} saniye")
    print(f"📊 Örnekleme Hızı (Sample Rate): {sr} Hz")
    
else:
    print(f"❌ HATA: Dosya bulunamadı! Aranan yol: {dosya_yolu}")
    print("Lütfen VS Code'da sol taraftaki dosya yapısını kontrol et.")