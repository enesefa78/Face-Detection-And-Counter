

Bu proje, kameradan alınan görüntülerde insanları ve yüzleri algılayarak belirli bir çizgiyi geçen kişileri sayar. İki farklı dosya bulunmaktadır: `handdetetionandcounter.py` ve `facedetectionandcounter.py`.

## Gereksinimler

- Python 3.x
- OpenCV kütüphanesi

OpenCV kütüphanesini yüklemek için:
```sh
pip install opencv-python
```

## Kullanım

### `handdetectionandcounter.py`

Bu dosya, HOG (Histogram of Oriented Gradients) tanımlayıcısını kullanarak insanları algılar ve kırmızı çizginin sağından geçen her insan için sayaç değerini artırır.

#### Çalıştırma

```sh
python sayac1.py
```

#### Açıklama

- Kamera açılır ve görüntü alınır.
- HOG tanımlayıcısı kullanılarak insan algılama yapılır.
- Çerçevenin ortasına kırmızı bir çizgi çizilir.
- İnsanların çizgiyi geçip geçmediği kontrol edilir ve sayaç değeri güncellenir.
- Sayaç değeri çerçevenin sol üst köşesinde gösterilir.

### `sayac2.py`

Bu dosya, Haar Cascade sınıflandırıcılarını kullanarak yüzleri algılar ve kırmızı çizginin sağından geçen her yüz için sayaç değerini artırır, solundan geçen her yüz için sayaç değerini azaltır.

#### Çalıştırma

```sh
python facedetectionandcounter.py
```

#### Açıklama

- Kamera açılır ve görüntü alınır.
- Haar Cascade sınıflandırıcıları kullanılarak yüz algılama yapılır.
- Çerçevenin ortasına kırmızı bir çizgi çizilir.
- Yüzlerin çizgiyi geçip geçmediği kontrol edilir ve sayaç değeri güncellenir.
  - Yüz çizginin sağından geçerse sayaç +1 artırılır.
  - Yüz çizginin solundan geçerse sayaç -1 azaltılır.
- Sayaç değeri çerçevenin sol üst köşesinde gösterilir.

## Kapatma

Her iki dosya da çalışırken `q` tuşuna basarak programı sonlandırabilirsiniz.


