from django.urls import path
from . import views


urlpatterns = [
    path('', views.anasayfa),
    path("anasayfa", views.anasayfa, name='anasayfa'),
    path('hakkımızda', views.hakkımızda, name='hakkimda'),
    path('galeri', views.galeri, name='galeri'),
    path('hizmetlerimiz', views.hizmetlerimiz, name='hizmetler'),
    # path('iletisim', views.iletisim1, name='iletisim'),
]
