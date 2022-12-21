from rest_framework import viewsets
from . import models 
from . import serializers

class InfoViewSet(viewsets.ModelViewSet):
    queryset = models.Info.objects.all()
     #api အလုပ်လုပ်ပြီဆိုရင်ကျွန်တော်တို့api က queryset ဆိုတဲ့ကောင်ကို လာရှာမယ် 
    #ကျွန်တော်တို့ api တွေကိုတခြားနေရာကနေပြီးတော့ လှမ်းပြီးတော့ပဲယူယူ /တခြားသော application ကနေပြီးတော့
    #လှမ်းပြီးတော့ပဲတောင်းတောင်းဒီကောင်ကိုပဲသုံးပြီးတော program တစ်ပုဒ်လုံး data ထုတ်တာသွင်းတာ လုပ်သွားမယ်
    serializer_class = serializers.InfoSerializer