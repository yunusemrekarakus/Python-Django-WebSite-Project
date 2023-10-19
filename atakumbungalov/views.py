from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Hakkımda,Hizmetler,Galeri,AnasayfaHizmetler,AnasayfaOdalar


def anasayfa(request):
    fotograf = Galeri.objects.filter(anasayfa_active=True)
    oda = AnasayfaOdalar.objects.all()
    hizmetler = AnasayfaHizmetler.objects.all()
    data = {
            "photo": fotograf,
            "hizmetler": hizmetler,
            "oda": oda,
        }

    return render(request,"index.html",data)

def hakkımızda(request):
    data = Hakkımda.objects.all()

    context = {
        "hakkimda": data
    }

    return render(request,"hakkımızda.html", context)

def galeri(request):
    fotograf = Galeri.objects.all()
    data = {
        "fotograf1": fotograf
    }

    return render(request, "galeri.html", data)

def hizmetlerimiz(request):
    hizmet = Hizmetler.objects.filter(is_active=True)
    #wifi = Hizmetler.objects.filter(id=1)
    #netflix = Hizmetler.objects.filter(id=2)
    #mangal = Hizmetler.objects.filter(id=3)
    #havuz = Hizmetler.objects.filter(id=4)
    #serpmekahvalti = Hizmetler.objects.filter(id=5)

    context = {
        "hizmet" : hizmet,
        #"wifi1": wifi,
        #"netflix1": netflix,
        #"mangal1": mangal,
        #"havuz1": havuz,
        #"serpmekahvalti1": serpmekahvalti,
    }

    return render(request, "hizmetlerimiz.html" , context)


