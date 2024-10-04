from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.salida.models import Salida
from apps.salida.api.serializers import SalidaSerializer

class SalidaApiView(ViewSet):

    def list(self,request):
        serializer = SalidaSerializer(Salida.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self, request, pk=int):
        serializer = SalidaSerializer(Salida.objects.get(pk=pk))
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    
    def create(self,request):
        serializer = SalidaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def update(self, request, pk):
        try:
            serializer = Salida.objects.get(pk=pk)
            serializer = SalidaSerializer(Salida, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Salida.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"No se encontró registro"})
            
    def partial_update (self, request, pk):
        try:
            serializer = Salida.objects.get(pk=pk)
            serializer = SalidaSerializer(serializer, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Salida.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"No se encontró registro"})

    def destroy(self, request, pk):
        serializer = Salida.objects.get(pk=pk)
        serializer.delete()
        return Response(status=status.HTTP_200_OK)