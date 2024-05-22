# Depo Takip Sistemi
 
Bu uygulama, Türkiye'deki belirli depoların ürün giriş ve çıkışlarını takip etmek için geliştirilmiştir. Uygulama, kullanıcı veritabanıyla entegre çalışır. Programı çalıştırdığınızda, çalışma dizininde otomatik olarak bir SQL dosyası ve "loglar.txt" adında bir giriş takip dosyası oluşturulur. Bu dosyada "username", "password" ve "mail" sütunları bulunur. Şifreler, "password" sütununda şifreleme algoritmasıyla kodlanarak saklanır. Uygulama başlatıldığında kullanıcıya bir menü sunulur. Kullanıcı, yapmak istediği işlemi seçerek ilgili işlemi gerçekleştirir.

"Kayıt ol" kısmında her zaman bir "admin" isimli kullanıcı kayıt olmak zorundadır. Farklı bir isimde kayıt olan kullanıcılar belirli özelliklere erişemezler. Eğer kullanıcı "şifre değiştir" seçeneğini tercih ederse, kullanıcı adını girerek kayıt olurken girdiği mail adresine bir "doğrulama maili" alabilir. Maildeki "doğrulama kodu" ile yeni şifresini belirleyebilir. "Kullanıcı sil" kısmında sadece "admin" adlı kullanıcı silinemez.

Başarılı bir girişin ardından kullanıcıya başka bir menü sunulur. Bu menülerde sırasıyla şu seçenekler yer alır:

1-Ürün Ekle

2-Ürün Bilgilerini Göster

3-Ürün Bilgilerini veya Logları Mail Gönder

4-Maili Hızlı Erişimlere Ekle

5-Ürün Sil

6-Ürün Transfer Et

7-Arka Plan Müziğini Oynat

8-Arka Plan Müziğini Durdur

9-Çıkış Yap

Ürün Ekle: "Kayıtlar.xlsx" adında bir dosya oluşturur (eğer yoksa). Ardından ilgili deponun yer aldığı il seçilerek ürünün "barkod numarası", "ürün adı", "ürün miktarı" gibi özellikleri girilir ve kaydedilir. 

Ürün Bilgilerini Göster: Kullanıcıya "barkod numarasına göre göster" veya "tüm sayfayı göster" gibi seçenekler sunulur. 

Ürün Bilgilerini veya Logları Mail Gönder: "Kayıtlar.xlsx", "loglar.txt" veya her ikisini de mail olarak gönderebilirsiniz. Mail göndermek için Google'ın SMTP sunucusu kullanılır. Mail göndermek için ya 4. seçenekteki "hızlı erişimlere ekle" kısmında daha önce eklediğiniz bir maili seçebilir yada elle farklı bir mail girebilirsiniz.

Ürün Sil: Bu seçenek, depodan bir ürünü silmenizi sağlar. Silinecek ürünü seçtikten sonra silme işlemi gerçekleştirilir.

Ürün Transfer Et: Bu seçenek, bir depodan diğerine ürün transferi yapmanıza olanak tanır. Transfer edilecek ürünler ve miktarları belirlenerek transfer işlemi gerçekleştirilir.

Arka Plan Müziğini Oynat: Bu seçenek, uygulama içinde arka planda müzik çalmasını sağlar. Müzik çalma seçeneği aktif hale getirilir ve seçenekten çıkıldığında müzik durdurulur.

Arka Plan Müziğini Durdur: Bu seçenek, arka planda çalan müziği durdurur. Müzik durdurulduktan sonra tekrar oynatmak için "Arka Plan Müziğini Oynat" seçeneği kullanılabilir.

Çıkış Yap: Bu seçenek, uygulamadan çıkış yapmanızı sağlar. Uygulama kapandığında kullanıcıya bir çıkış mesajı gösterilir ve uygulama sonlandırılır.

Admin olmayan kullanıcılar sadece 2, 3, 4, 7, 8 ve 9. seçeneklere erişebilirler. Eğer programın çalıştığı sırada kullanıcı beklenmedik bir hata alırsa, kullanıcıya hatayı bir dosyaya kaydedip kaydetmeyeceği sorulur. Kullanıcı kaydetmeyi seçerse, programın bulunduğu klasöre "hatalar.txt" adında bir dosya oluşturulur.