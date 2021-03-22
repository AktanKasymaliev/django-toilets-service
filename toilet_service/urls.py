from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from user.views import TokenObtainPairView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api_side.urls')),
    path('', include('map.urls'), name='map'),
    path('user/', include('user.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/captcha/', include('rest_captcha.urls')),
    path('auth/', include('account_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
