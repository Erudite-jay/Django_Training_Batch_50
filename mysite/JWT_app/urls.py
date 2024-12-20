from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView
)

urlpatterns = [
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]