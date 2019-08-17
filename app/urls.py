from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import Users, Categories, ItemsList, ItemsDetail


urlpatterns = [
    path('users/',
         Users.as_view(),
         name='users'),
    path('categories/',
         Categories.as_view({'get': 'list'}),
         name='categories_list'),
    path('categories/<int:pk>/',
         Categories.as_view({'get': 'retrieve'}),
         name='categories_retrieve'),
    path('items/',
         ItemsList.as_view(),
         name='items_list'),
    path('items/<int:pk>/',
         ItemsDetail.as_view(),
         name='items_detail'),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
