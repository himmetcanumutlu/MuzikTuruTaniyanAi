import os
import librosa
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split

DATA_YOLU = r"C:\Users\goygo\Desktop\MuzikTuruTanima\Data"
TURLER = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

def veri_hazirla(data_yolu):
    X = []
    y = []
    print("Gelişmiş özellik çıkarımı (n_mfcc=40) başladı...")
    for i, tur in enumerate(TURLER):
        tur_yolu = os.path.join(data_yolu, tur)
        print(f"Eğitiliyor: {tur}")
        for dosya in os.listdir(tur_yolu):
            if dosya.endswith('.wav'):
                try:
                    # n_mfcc değerini 40 yaparak detayı artırdık
                    signal, sr = librosa.load(os.path.join(tur_yolu, dosya), duration=30)
                    mfcc = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=40) 
                    mfcc = mfcc.T
                    if len(mfcc) >= 1200:
                        X.append(mfcc[:1200, :])
                        y.append(i)
                except: pass
    return np.array(X), np.array(y)

X, y = veri_hazirla(DATA_YOLU)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# DAHA DERİN MODEL (Katmanlar artırıldı)
model = models.Sequential([
    layers.Conv1D(64, 3, activation='relu', input_shape=(1200, 40)),
    layers.MaxPooling1D(2),
    layers.Conv1D(128, 3, activation='relu'),
    layers.MaxPooling1D(2),
    layers.Conv1D(256, 3, activation='relu'), # Yeni katman
    layers.GlobalAveragePooling1D(), # Daha iyi genelleme için
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5), # Ezberlemeyi önlemek için
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

print("Güçlendirilmiş eğitim başlıyor (50 Epoch)...")
model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test), batch_size=32)
model.save('muzik_modeli.keras')
print("Model başarıyla güncellendi!")