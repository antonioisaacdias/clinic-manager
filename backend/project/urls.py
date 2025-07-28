from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenBlacklistView
from apps.user.views import EmailTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.user.urls')),
    path('api/v1/', include('apps.professional.urls')),
    path('api/v1/', include('apps.patient.urls')),
    path('api/v1/administration/', include('apps.administration.urls')),

    # JWT Authentication
    path('api/v1/auth/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/auth/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
