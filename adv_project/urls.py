from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

router = routers.DefaultRouter()
router.register("rooms", RoomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
]
