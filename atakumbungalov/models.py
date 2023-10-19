from django.db import models

class Hakkımda(models.Model):
    baslik = models.CharField(max_length=20)
    icerik = models.TextField()
    image = models.ImageField(upload_to="hakkımda")
    
    class Meta:
        verbose_name = "Hakkımda"
        verbose_name_plural = "Hakkımda"

    def __str__(self):
        return self.baslik


class Hizmetler(models.Model):
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
    is_active = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Hizmetler"
        verbose_name_plural = "Hizmetler"

    def __str__(self):
        return self.baslik


class Galeri(models.Model):
    baslik = models.CharField(max_length=50)
    image = models.ImageField(upload_to="galeri")
    anasayfa_active = models.BooleanField(default=False, verbose_name='Anasayfada Görünsün mü')
    yayıntarih = models.DateTimeField(auto_now_add=True, verbose_name='Yayın Tarihi')

    class Meta:
        verbose_name = "Galeri"
        verbose_name_plural = "Galeri"
    
    def __str__(self):
        return self.baslik

class AnasayfaHizmetler(models.Model):
    baslik = models.CharField(max_length=50, verbose_name="Başlık")
    icerik = models.TextField(verbose_name='İçerik')
    image = models.ImageField(verbose_name='Resim')

    class Meta:
        verbose_name = 'Ana Sayfa Hizmetler'
        verbose_name_plural = 'Ana Sayfa Hizmetler'

class AnasayfaOdalar(models.Model):
    baslik = models.CharField(max_length=50, verbose_name="Oda İsmi")
    ozellik1 = models.CharField(max_length=50, verbose_name="1. Özellik")
    ozellik2 = models.CharField(max_length=50,verbose_name="2. Özellik")
    ozellik3 = models.CharField(max_length=50,verbose_name="3. Özellik")
    ozellik4 = models.CharField(max_length=50,verbose_name="4. Özellik")
    buyukresim = models.ImageField(upload_to="oda")
    kucukresim = models.ImageField(upload_to="oda")

    class Meta:
        verbose_name = "Oda Bilgi"
        verbose_name_plural = "Oda Bilgi"

    def __str__(self):
        return self.baslik


