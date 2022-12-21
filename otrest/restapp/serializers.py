from rest_framework import serializers as core_serializers
from . models import Info

class InfoSerializer(core_serializers.ModelSerializer):
    class Meta:#သူ့ရဲ့မူရင်း class ကကောင်ကိုအလုပ်လုပ်ပေးတဲ့ကောင်
        model = Info#info class ကနေလှမ်းယူပြီးတော့ model လို့နာမည်ပေးမယ်
        fields = '__all__'#db ထဲက database ထဲကနေပြီးတော့fields တွေအကုန်လုံးစီကနေပြီးတော့ data လှမ်းယူမာ