import streamlit as st
import librosa
import numpy as np
import tensorflow as tf
import pandas as pd
import hashlib
import json
import os

st.set_page_config(page_title="Müzik Türü Tanıyan Yapay Zeka", layout="wide")
st.title("müzik türü tanıyan yapay zeka")

TURLER = ['Blues', 'Klasik Müzik', 'Country', 'Disco', 'Hip-Hop', 'Caz', 'Metal', 'Pop', 'Reggae', 'Rock']
KLASOR_ISIMLERI = {
    'Blues': 'blues', 'Klasik Müzik': 'classical', 'Country': 'country',
    'Disco': 'disco', 'Hip-Hop': 'hiphop', 'Caz': 'jazz',
    'Metal': 'metal', 'Pop': 'pop', 'Reggae': 'reggae', 'Rock': 'rock'
}

st.sidebar.header("Analiz Ayarları")
intro_guveni = st.sidebar.slider("Giriş Bölümü Güven Çarpanı", 0.0, 1.0, 0.4)

@st.cache_resource
def modeli_yukle():
    return tf.keras.models.load_model('muzik_modeli.keras')

model = modeli_yukle()

HAFIZA_DOSYASI = "hafiza.json"
def hafizayi_getir():
    if os.path.exists(HAFIZA_DOSYASI):
        with open(HAFIZA_DOSYASI, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def hafizaya_yaz(veri):
    with open(HAFIZA_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)

hafiza = hafizayi_getir()

yuklenen_dosya = st.file_uploader("Analiz edilecek .wav dosyasını seçiniz", type=["wav"])

if yuklenen_dosya is not None:
    dosya_baytlari = yuklenen_dosya.getvalue()
    dosya_hash = hashlib.md5(dosya_baytlari).hexdigest()
    
    st.audio(yuklenen_dosya, format='audio/wav')
    
    # 1. HER DURUMDA ANALİZİ YAP (Hafızada olsa bile)
    with st.spinner('Ses dalgaları taranıyor ve spektral analiz yapılıyor...'):
        y, sr = librosa.load(yuklenen_dosya, sr=None)
        toplam_sure = librosa.get_duration(y=y, sr=sr)
        segment_suresi = 30
        num_segments = int(toplam_sure // segment_suresi)
        
        puanlar = []
        agirliklar = []
        tablo_verisi = []

        for i in range(num_segments):
            agirlik = intro_guveni if i == 0 else 1.0
            chunk = y[i*30*sr : (i+1)*30*sr]
            mfcc = librosa.feature.mfcc(y=chunk, sr=sr, n_mfcc=40).T
            
            if len(mfcc) >= 1200:
                mfcc_input = np.expand_dims(mfcc[:1200, :], axis=0)
                tahmin = model.predict(mfcc_input, verbose=0)[0]
                
                puanlar.append(tahmin * agirlik)
                agirliklar.append(agirlik)
                
                tablo_verisi.append({
                    "Zaman Aralığı": f"{i*30}-{i*30+30} sn",
                    "Modelin Ham Tahmini": TURLER[np.argmax(tahmin)],
                    "Bölüm Güven Skoru": f"%{np.max(tahmin)*100:.2f}",
                    "Etki Payı": agirlik
                })

        if len(puanlar) > 0:
            genel_sonuc = np.sum(puanlar, axis=0) / np.sum(agirliklar)
            model_kazanan_tur = TURLER[np.argmax(genel_sonuc)]
            
            # 2. EKRANA YAZDIRMA AŞAMASI (Hafıza Kontrolü Burada Devreye Girer)
            if dosya_hash in hafiza:
                # EĞER ŞARKI HAFIZADAYSA
                ogretilen_tur = hafiza[dosya_hash]
                st.success(f"🧠 **Hafıza Devrede:** Bu şarkıyı hatırlıyorum! Daha önce bana bunun bir **{ogretilen_tur}** şarkısı olduğunu öğretmiştin. Kesin Sonuç: **{ogretilen_tur}**")
                
                st.write("---")
                st.markdown("#### 🔍 Modelin Arka Plan Analizi")
                st.caption(f"Eğer bana doğrusunu öğretmeseydin, sistem şu anki kısıtlı eğitimiyle bu şarkıyı **{model_kazanan_tur}** olarak tahmin edecekti. İşte nedeni:")
                
                st.table(pd.DataFrame(tablo_verisi))
                st.bar_chart(pd.DataFrame({"Türler": TURLER, "Olasılık": genel_sonuc*100}).set_index("Türler"))
                
            else:
                # EĞER ŞARKI YENİYSE (Normal İşleyiş)
                st.subheader("1. Genel Sonuç")
                st.success(f"Yapay zeka tahmini: Bu şarkı büyük olasılıkla bir **{model_kazanan_tur}** parçasıdır. (Güven: %{np.max(genel_sonuc)*100:.2f})")
                
                st.subheader("2. Bölüm Bazlı Güven Skorları")
                st.table(pd.DataFrame(tablo_verisi))
                
                st.subheader("3. Olasılık Dağılımı")
                st.bar_chart(pd.DataFrame({"Türler": TURLER, "Olasılık": genel_sonuc*100}).set_index("Türler"))

                # ÖĞRETME FORMU (Sadece şarkı hafızada YOKSA görünür)
                st.write("---")
                st.markdown("### Yapay Zeka Yanıldı Mı? Doğrusunu Öğret!")
                st.caption("Eğer yukarıdaki tahmin yanlışsa, doğru türü seçerek sistemin öğrenmesini sağlayabilirsiniz.")
                
                with st.form("ogretme_formu"):
                    secilen_dogru_tur = st.selectbox("Bu şarkının GERÇEK türü nedir?", TURLER)
                    ogret_butonu = st.form_submit_button("Sistemi Eğit ve Kaydet")
                    
                    if ogret_butonu:
                        hafiza[dosya_hash] = secilen_dogru_tur
                        hafizaya_yaz(hafiza)
                        
                        klasor_adi = KLASOR_ISIMLERI.get(secilen_dogru_tur, 'diger')
                        hedef_klasor = os.path.join("Data", klasor_adi)
                        
                        if not os.path.exists(hedef_klasor):
                            os.makedirs(hedef_klasor)
                        
                        hedef_dosya_yolu = os.path.join(hedef_klasor, f"user_taught_{dosya_hash[:8]}.wav")
                        with open(hedef_dosya_yolu, "wb") as f:
                            f.write(dosya_baytlari)
                        
                        st.success(f"Başarılı! Bu şarkı kalıcı olarak **{secilen_dogru_tur}** kategorisine eklendi ve hafızaya kazındı.")
                        st.rerun()

st.markdown("<br><hr><p style='text-align: center; font-size: 12px; color: gray;'>bertu deler tarafından yapıldı</p>", unsafe_allow_html=True)