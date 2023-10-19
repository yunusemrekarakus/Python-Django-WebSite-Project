from django.db import models

class Contact(models.Model):
    adsoyad = models.CharField(max_length=50, verbose_name="AD SOYAD")
    email = models.EmailField(max_length=30, verbose_name="EMAİL")
    phone = models.CharField(max_length=15, verbose_name="TEL NO")
    message = models.TextField(verbose_name="MESAJ")
    tarih = models.DateTimeField(auto_now_add=True, verbose_name="TARİH")

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"

    def __str__(self):
        return self.adsoyad
