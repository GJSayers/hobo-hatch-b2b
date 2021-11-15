from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('collections/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('profile/', include('profiles.urls')),
    path('checkout/', include('checkout.urls')),
    path('about/', include('about.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
