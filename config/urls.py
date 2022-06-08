
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from apps.product.views import ReviewViewSet

router = SimpleRouter()
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/category/', include('apps.category.urls')),
    path('api/v1/product/', include('apps.product.urls')),
    path('', include(router.urls)),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
