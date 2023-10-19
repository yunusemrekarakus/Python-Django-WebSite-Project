from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['adsoyad','tarih']
    list_display_links = ['adsoyad','tarih']
    list_filter = ['tarih']
    search_fields = ['adsoyad','content']
    class Meta:
        model = Contact
admin.site.register(Contact,ContactAdmin)