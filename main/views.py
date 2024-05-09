# Create your views here.
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


# ModelViewSet provides typical CRUD (Create, Read, Update, Delete) operations for Django models.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
