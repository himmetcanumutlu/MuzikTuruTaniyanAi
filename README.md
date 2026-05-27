# MuzikTuruTanima / Music Genre Recognition

## Türkçe

MuzikTuruTanima, verilen bir müzik dosyasının türünü tahmin etmeye yönelik geliştirilmiş bir projedir. Sistem, müziği 30 saniyelik bölümlere ayırır ve her bölümü daha önce öğrendiği müzik türleriyle karşılaştırır. Bu karşılaştırmalar sonucunda müziğin çoğunluk olarak hangi türe ait olduğunu saptar.

Proje, tahmin sonucunun hatalı olduğunu düşündüğünüz durumlarda doğru türü öğretme imkanı da sunar. Böylece kullanıcı, sistemin verdiği sonuca müdahale ederek doğru bilgiyi ekleyebilir.

## English

MuzikTuruTanima is a project developed to predict the genre of a given music file. The system divides the music into 30-second segments and compares each segment with the music genres it has previously learned. Based on these comparisons, it determines which genre the music mostly belongs to.

The project also provides the option to teach the correct genre if you think the prediction is wrong. This allows the user to correct the system's result by adding the accurate genre information.

---

# Proje Hakkında / About the Project

## Türkçe

Bu proje, müzik türü tanıma mantığı üzerine kuruludur. Verilen müzik tek parça halinde değerlendirilmez; bunun yerine 30 saniyelik bölümlere ayrılarak analiz edilir. Her bölüm sistemin öğrendiği türlerle karşılaştırılır ve parçanın genel türü çoğunluk sonucuna göre belirlenir.

Bu yaklaşım sayesinde müzik dosyasının farklı bölümleri ayrı ayrı değerlendirilir. Sonuç olarak sistem, bölümlerden elde edilen tahminleri kullanarak müziğin genel olarak hangi türe daha yakın olduğunu ortaya koyar.

## English

This project is based on music genre recognition logic. The given music is not evaluated as a single whole; instead, it is divided into 30-second segments and analyzed. Each segment is compared with the genres learned by the system, and the overall genre of the track is determined according to the majority result.

With this approach, different parts of the music file are evaluated separately. As a result, the system uses the predictions obtained from the segments to identify which genre the music is mostly closest to.

---

# Temel Özellikler / Main Features

## Türkçe

MuzikTuruTanima, verilen müziği 30 saniyelik bölümlere ayırarak analiz eder. Her bölüm, sistemin öğrendiği türlerle karşılaştırılır. Bu analizlerin sonucunda çoğunluk olarak öne çıkan tür, müziğin genel türü olarak belirlenir.

Sistem ayrıca yanlış tahmin durumlarında doğru türü öğretme imkanı sunar. Kullanıcı, sistemin hata yaptığını düşünürse doğru tür bilgisini ekleyebilir.

## English

MuzikTuruTanima analyzes the given music by dividing it into 30-second segments. Each segment is compared with the genres learned by the system. As a result of these analyses, the genre that appears most frequently is determined as the overall genre of the music.

The system also allows the correct genre to be taught in cases of incorrect prediction. If the user thinks the system made a mistake, they can add the correct genre information.

---

# Çalışma Mantığı / How It Works

## Türkçe

Sistem, verilen müzik dosyasını önce 30 saniyelik parçalara böler. Daha sonra bu parçaların her birini kendi öğrendiği türlerle karşılaştırır. Her bölüm için elde edilen sonuçlar birlikte değerlendirilir ve çoğunlukta olan tür final sonuç olarak belirlenir.

Eğer kullanıcı sistemin verdiği sonucun yanlış olduğunu düşünürse doğru türü sisteme öğretebilir. Bu özellik, projenin kullanıcı tarafından düzeltilmesine imkan tanır.

## English

The system first divides the given music file into 30-second parts. It then compares each of these parts with the genres it has learned. The results obtained for each segment are evaluated together, and the genre that appears in the majority is determined as the final result.

If the user thinks the result given by the system is wrong, they can teach the correct genre to the system. This feature allows the project to be corrected by the user.

---

# Kullanım / Usage

## Türkçe

Projeyi kullanmak için sisteme bir müzik dosyası verilir. Sistem bu müziği 30 saniyelik bölümlere ayırır, bölümleri öğrendiği türlerle karşılaştırır ve müziğin çoğunluk olarak hangi türe ait olduğunu kullanıcıya gösterir.

Tahmin sonucunun yanlış olduğu düşünülürse kullanıcı doğru türü öğretebilir. Böylece sistemin verdiği sonuç üzerinde düzeltme yapılabilir.

## English

To use the project, a music file is provided to the system. The system divides this music into 30-second segments, compares the segments with the genres it has learned, and shows the user which genre the music mostly belongs to.

If the prediction result is considered incorrect, the user can teach the correct genre. This makes it possible to correct the result provided by the system.

---

# Not / Note

## Türkçe

Bu README yalnızca mevcut proje açıklamasında verilen bilgilere dayanarak hazırlanmıştır. Projede kullanılan teknoloji, kurulum komutları veya dosya yapısı hakkında kaynak metinde bilgi bulunmadığı için bu bölümlere ekleme yapılmamıştır.

## English

This README has been prepared only based on the information provided in the existing project description. Since the source text does not include information about the technologies used, installation commands, or file structure, no additional sections have been added for those topics.
