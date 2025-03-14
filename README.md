# XML Translator

XML Translator, XML dosyalarındaki metinleri farklı dillere çevirmeye yönelik bir Python aracıdır. Google Translate API'si kullanarak, kullanıcıların XML dosyalarındaki metinleri belirli bir kaynaktan hedef dile çevirmesini sağlar. Ayrıca, kullanıcıların özel çeviri sözlükleri eklemesine de olanak tanır.

## Özellikler

- XML dosyalarındaki metinleri otomatik olarak çevirebilme.
- Özel çeviri sözlükleri (örneğin, oyun terimleri gibi) kullanarak belirli terimleri çevirebilme.
- İlerleme çubuğu ile işlem takibi.
- Hedef ve kaynak dil seçimleri.
- Çoklu dosya çevirisi ve paralel işlem desteği.
- Çevirilen dosyaların istatistiklerini görme.

## Başlarken

Bu rehber, XML Translator'ı bilgisayarınıza kurup çalıştırabilmeniz için gerekli adımları içerir.

### Gereksinimler

Proje şu Python kütüphanelerine ihtiyaç duyar:
- `deep-translator`: Google Translate API entegrasyonu için.
- `tqdm`: İlerleme çubuğu için.

### Kurulum

Projeyi çalıştırmadan önce, gerekli bağımlılıkları yüklemeniz gerekir. Bunun için `requirements.txt` dosyasını kullanabilirsiniz.

1. Projeyi yerel makinenize indirin veya klonlayın:

   git clone https://github.com/licaster0/xml-translator.git
   cd xml-translator

2. Bağımlılıkları yükleyin:

   python install_requirements.py

   Veya doğrudan `requirements.txt` ile yüklemek için:

   pip install -r requirements.txt

### Kullanım

XML dosyalarını çevirmek için aşağıdaki adımları takip edebilirsiniz.

1. **Kaynak ve Hedef Dili Seçin**:
   Çeviri yapmak istediğiniz kaynak dil ve hedef dil kodlarını girmeniz istenecektir. Örneğin, İngilizce'den Türkçe'ye çevirmek için:
   
   - Kaynak Dil: `en`
   - Hedef Dil: `tr`

2. **XML Dosyalarını Seçin**:
   Çevrilecek XML dosyalarının bulunduğu dizin yolunu belirtin.

3. **Özel Çeviri Sözlüğü (Opsiyonel)**:
   Çeviri sırasında kullanılacak özel terimler için bir çeviri sözlüğü eklemek isteyip istemediğiniz sorulacaktır.

4. **Çeviriye Başla**:
   Çeviriyi başlattıktan sonra, ilerleme çubuğu ile işlemi takip edebilirsiniz. Çeviri tamamlandığında, başarıyla çevrilen dosyalar ve kelimeler hakkında istatistikler görüntülenir.

### Örnek Çalıştırma

Proje klasörüne girdikten sonra, aşağıdaki komutu çalıştırabilirsiniz:

   python translate.py

Bu komut, XML dosyalarını çevirmek için size gerekli tüm yönlendirmeleri verecektir.

### Katkı Sağlama

Katkı sağlamak isteyenler için şu adımları takip edebilirsiniz:

1. Projeyi forklayın.
2. Yeni bir özellik ekleyin veya hata düzeltmesi yapın.
3. Pull request (PR) gönderin.

Her katkı için testlerin çalıştığından emin olun.

### Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

### İletişim

Projeye dair sorularınız veya önerileriniz için iletişime geçebilirsiniz:

- Instagram: [licaster0](https://www.instagram.com/licaster0/)
