# MuzikTuruTanima / Music Genre Recognition

## Türkçe

MuzikTuruTanima, kullanıcı tarafından verilen bir müzik dosyasını analiz ederek parçanın çoğunlukla hangi müzik türüne ait olduğunu tahmin eden bir müzik türü tanıma projesidir. Sistem, müziği 30 saniyelik bölümlere ayırır ve her bölümü daha önce öğrendiği tür özellikleriyle karşılaştırır. Ardından elde edilen sonuçları değerlendirerek parçanın genel türünü belirler.

Proje yalnızca tahmin yapmakla kalmaz; kullanıcı sistemin verdiği sonucun hatalı olduğunu düşünürse doğru tür bilgisini öğretebilir. Bu sayede sistem zamanla yeni örneklerden öğrenebilir ve daha doğru tahminler yapabilecek şekilde geliştirilebilir.

## English

MuzikTuruTanima is a music genre recognition project that analyzes a music file provided by the user and predicts which genre the track mostly belongs to. The system divides the music into 30-second segments and compares each segment with the genre features it has previously learned. It then evaluates the results and determines the overall genre of the track.

The project does not only make predictions; if the user thinks the prediction is incorrect, they can teach the system the correct genre. In this way, the system can learn from new examples over time and improve its prediction accuracy.

---

# Proje Hakkında / About the Project

## Türkçe

Bu proje, müzik türlerini otomatik olarak tanımak için geliştirilmiştir. Bir müzik parçası tek bir bölüm üzerinden değerlendirilmek yerine 30 saniyelik parçalara ayrılır. Her bölüm ayrı ayrı analiz edilir ve sistemin daha önce öğrendiği türlerle karşılaştırılır. Bu yöntem, özellikle uzun müzik dosyalarında daha dengeli ve güvenilir bir tür tahmini yapılmasına yardımcı olur.

Sistemin temel mantığı çoğunluk kararına dayanır. Yani her 30 saniyelik bölüm için bir tür tahmini yapılır ve en çok tekrar eden tür, parçanın genel türü olarak kabul edilir. Böylece müziğin yalnızca kısa bir kısmına göre değil, tamamına yayılan bir analiz sonucuna göre karar verilmiş olur.

## English

This project was developed to automatically recognize music genres. Instead of evaluating a music track based on a single section, the track is divided into 30-second segments. Each segment is analyzed separately and compared with the genres previously learned by the system. This method helps produce a more balanced and reliable genre prediction, especially for longer music files.

The core logic of the system is based on majority voting. A genre prediction is made for each 30-second segment, and the genre that appears most frequently is accepted as the overall genre of the track. This allows the system to make a decision based on the full structure of the music rather than only a short part of it.

---

# Özellikler / Features

## Türkçe

MuzikTuruTanima, müzik dosyalarını otomatik olarak 30 saniyelik bölümlere ayırarak analiz eder. Her bölüm, sistemin daha önce öğrendiği müzik türleriyle karşılaştırılır ve bölüm bazında bir tahmin üretilir. Daha sonra bu tahminler bir araya getirilerek parçanın genel türü belirlenir.

Proje, kullanıcı geri bildirimiyle öğrenme özelliği sunar. Eğer kullanıcı sistemin yanlış tahmin yaptığını düşünürse doğru tür bilgisini sisteme öğretebilir. Bu özellik, projenin zaman içinde daha fazla örnekle gelişmesine ve farklı türleri daha iyi ayırt edebilmesine katkı sağlar.

Sistem, müzik türü tahmin sürecini daha anlaşılır hale getirmek için parça bazlı analiz yaklaşımı kullanır. Bu yapı sayesinde hem kısa hem de uzun müzik dosyalarında daha tutarlı sonuçlar elde edilmesi hedeflenir.

## English

MuzikTuruTanima automatically divides music files into 30-second segments for analysis. Each segment is compared with the music genres previously learned by the system, and a prediction is generated for each segment. These predictions are then combined to determine the overall genre of the track.

The project provides a learning feature through user feedback. If the user believes that the system made an incorrect prediction, they can teach the system the correct genre. This feature helps the project improve over time with more examples and distinguish between different genres more effectively.

The system uses a segment-based analysis approach to make the music genre prediction process more understandable. With this structure, the goal is to obtain more consistent results for both short and long music files.

---

# Çalışma Mantığı / How It Works

## Türkçe

Sistem ilk olarak kullanıcıdan alınan müzik dosyasını işler ve dosyayı 30 saniyelik parçalara böler. Her parça ayrı bir örnek gibi ele alınır. Daha sonra bu parçalar, sistemin öğrendiği tür verileriyle karşılaştırılır ve her bölüm için en olası müzik türü belirlenir.

Tüm bölümler analiz edildikten sonra sistem, çıkan sonuçları sayar ve çoğunlukta olan türü ana sonuç olarak kullanıcıya sunar. Kullanıcı sonucu doğru bulursa işlem tamamlanır. Eğer sonuç hatalıysa kullanıcı doğru türü belirterek sistemin öğrenme sürecine katkı sağlayabilir.

## English

The system first processes the music file provided by the user and divides it into 30-second parts. Each part is treated as a separate sample. These parts are then compared with the genre data learned by the system, and the most likely music genre is determined for each segment.

After all segments are analyzed, the system counts the results and presents the genre with the majority of predictions as the final result. If the user finds the result correct, the process is completed. If the result is incorrect, the user can provide the correct genre and contribute to the system's learning process.

---

# Kullanım Senaryosu / Usage Scenario

## Türkçe

Kullanıcı sisteme bir müzik dosyası verir. Sistem bu dosyayı otomatik olarak analiz eder, 30 saniyelik parçalara ayırır ve her parçanın türünü tahmin eder. Analiz tamamlandığında kullanıcıya müziğin çoğunlukla hangi türe ait olduğu gösterilir.

Örneğin, bir şarkının bazı bölümleri rock, bazı bölümleri pop özellikleri taşıyorsa sistem her bölüm için ayrı değerlendirme yapar. Eğer bölümlerin çoğu rock olarak sınıflandırılırsa genel sonuç rock olarak verilir. Kullanıcı bu sonucun yanlış olduğunu düşünürse doğru türü seçerek sisteme geri bildirim verebilir.

## English

The user provides a music file to the system. The system automatically analyzes the file, divides it into 30-second segments, and predicts the genre of each segment. When the analysis is complete, the user is shown which genre the music mostly belongs to.

For example, if some parts of a song contain rock characteristics and other parts contain pop characteristics, the system evaluates each segment separately. If most segments are classified as rock, the final result is given as rock. If the user thinks this result is incorrect, they can select the correct genre and provide feedback to the system.

---

# Kurulum / Installation

## Türkçe

Projeyi kullanmak için öncelikle kaynak kodları bilgisayarınıza indirmeniz gerekir. Ardından proje klasörüne girerek gerekli bağımlılıkları kurabilirsiniz. Kullanılan teknolojilere göre bağımlılıklar değişebilir, bu nedenle varsa `requirements.txt`, `package.json` veya proje içinde belirtilen kurulum dosyaları kontrol edilmelidir.

Örnek kurulum akışı aşağıdaki gibi olabilir:

```bash
git clone https://github.com/KULLANICI_ADINIZ/MuzikTuruTanima.git
cd MuzikTuruTanima
```

Eğer proje Python tabanlıysa gerekli paketler aşağıdaki şekilde kurulabilir:

```bash
pip install -r requirements.txt
```

## English

To use the project, first download the source code to your computer. Then enter the project folder and install the required dependencies. The dependencies may vary depending on the technologies used, so files such as `requirements.txt`, `package.json`, or any installation files included in the project should be checked.

An example installation flow may look like this:

```bash
git clone https://github.com/YOUR_USERNAME/MuzikTuruTanima.git
cd MuzikTuruTanima
```

If the project is Python-based, the required packages can be installed as follows:

```bash
pip install -r requirements.txt
```

---

# Kullanım / Usage

## Türkçe

Proje çalıştırıldıktan sonra kullanıcıdan analiz edilecek müzik dosyası alınır. Sistem dosyayı 30 saniyelik bölümlere ayırır, her bölümü analiz eder ve genel tür tahminini kullanıcıya sunar. Eğer kullanıcı tahmini yanlış bulursa doğru tür bilgisini girerek sistemin öğrenmesine katkı sağlayabilir.

Çalıştırma komutu, projenin yapısına göre değişebilir. Python tabanlı bir kullanımda örnek komut şu şekilde olabilir:

```bash
python main.py
```

## English

After the project is started, the user provides the music file to be analyzed. The system divides the file into 30-second segments, analyzes each segment, and presents the overall genre prediction to the user. If the user finds the prediction incorrect, they can enter the correct genre and help the system learn.

The run command may vary depending on the structure of the project. For a Python-based usage, an example command may be:

```bash
python main.py
```

---

# Geri Bildirim ve Öğrenme / Feedback and Learning

## Türkçe

MuzikTuruTanima'nın önemli özelliklerinden biri, kullanıcıdan gelen geri bildirimle geliştirilebilir olmasıdır. Sistem yanlış tahmin yaptığında kullanıcı doğru türü belirterek bu bilgiyi sisteme kazandırabilir. Bu yaklaşım, sistemin zamanla daha fazla örnek görmesini ve müzik türlerini daha doğru ayırt etmesini sağlar.

Bu öğrenme mantığı, özellikle farklı müzik türlerinin birbirine yakın olduğu durumlarda faydalıdır. Kullanıcı katkıları sayesinde sistem, benzer türler arasındaki farkları daha iyi öğrenebilir ve gelecekte daha isabetli tahminler yapabilir.

## English

One of the important features of MuzikTuruTanima is that it can be improved through user feedback. When the system makes an incorrect prediction, the user can provide the correct genre and add this information to the system. This approach allows the system to see more examples over time and distinguish music genres more accurately.

This learning logic is especially useful when different music genres are similar to each other. With user contributions, the system can better learn the differences between similar genres and make more accurate predictions in the future.

---

# Geliştirme Fikirleri / Future Improvements

## Türkçe

Gelecek sürümlerde daha fazla müzik türü desteği eklenebilir. Modelin doğruluğunu artırmak için daha geniş ve dengeli veri setleri kullanılabilir. Ayrıca kullanıcı arayüzü geliştirilerek analiz sonuçları daha görsel ve anlaşılır hale getirilebilir.

Bölüm bazlı tahmin sonuçlarının grafiklerle gösterilmesi, kullanıcıya müziğin hangi kısımlarında hangi tür özelliklerinin baskın olduğunu daha net gösterebilir. Bunun yanında model eğitimi, veri güncelleme ve geri bildirim süreçleri daha otomatik hale getirilebilir.

## English

In future versions, support for more music genres can be added. Larger and more balanced datasets can be used to improve model accuracy. The user interface can also be enhanced to make the analysis results more visual and easier to understand.

Displaying segment-based prediction results with charts can help users clearly see which genre characteristics are dominant in different parts of the music. In addition, model training, data updating, and feedback processes can be made more automated.

---

# Not / Note

## Türkçe

Bu proje, müzik türü tanıma ve makine öğrenmesi süreçlerini deneyimlemek amacıyla geliştirilmiştir. Sonuçlar kullanılan veri setine, model yapısına ve müzik dosyasının kalitesine göre değişiklik gösterebilir. Daha doğru sonuçlar için çeşitli türlerden dengeli ve kaliteli örneklerle sistemi eğitmek önerilir.

## English

This project was developed to experiment with music genre recognition and machine learning processes. The results may vary depending on the dataset used, the model structure, and the quality of the music file. For more accurate results, it is recommended to train the system with balanced and high-quality examples from various genres.
