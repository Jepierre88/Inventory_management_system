from django.shortcuts import render
from rest_framework import generics
from django.views.generic import ListView
from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
# Create your views here.

class ReadCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class UpdateCategory(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(["POST"])    
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response({"message":serializer.errors}, status=HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response({
        "message":"Category created succesfull",
        "category":serializer.data
    })
class DeleteCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ReadCategoryByID(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        # Filtrar categorías por el negocio del usuario autenticado
        business_id = self.request.GET.get('business_id')  # Supongamos que el negocio se pasa como parámetro
        return Category.objects.filter(business__owner=self.request.user, business_id=business_id)