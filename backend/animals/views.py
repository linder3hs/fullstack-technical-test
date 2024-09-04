from rest_framework.viewsets import ModelViewSet
from .models import Animal
from .serializers import AnimalSerializer
from common.responses import response_error, response_success

class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return response_success('Animals list', serializer.data)
        except Exception as e:
            return response_error("Error", str(e))
