from rest_framework.viewsets import ModelViewSet
from .models import Adoption
from .serializers import AdoptionSerializer
from common.responses import response_error, response_success


class AdoptionViewSet(ModelViewSet):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return response_success('Adoptions list', serializer.data)
        except Exception as e:
            return response_error('Error', str(e))
