from django.contrib import admin
from posts.views import PostViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
