from rest_framework.serializers import ModelSerializer
from .models import Adoption


class AdoptionSerializer(ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'
