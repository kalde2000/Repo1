from rest_framework import viewsets
from rest_framework.viewsets import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from .models import User, Category, Item
from .serializers import UserSerializer, CategorySerializer, ItemSerializer
from .utils import CustomGenericFilter


class Users(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = User.objects.create_user(**serializer.data)
        user.save()

class Categories(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemsList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [CustomGenericFilter]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ItemsDetail(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.count_views += 1
        obj.save()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
