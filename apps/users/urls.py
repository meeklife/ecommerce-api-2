from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    AddressView,
    ChangePasswordView,
    EmailVerification,
    ForgotPasswordView,
    OTPVerifyView,
    ProfileView,
    ResetPasswordView,
    RoleView,
    SignUpView,
    UserView,
)

router = DefaultRouter()


router.register("role", RoleView, basename="role")
router.register("address", AddressView, basename="address")
router.register("profile", ProfileView, basename="profile")
router.register("users", UserView, basename="users")


urlpatterns = [
    path("auth/signup/", SignUpView.as_view(), name="signup"),
    path("auth/verify-otp/", OTPVerifyView.as_view(), name= 'verify-otp'),
    path("auth/verify-email/", EmailVerification.as_view(), name = 'email-verify'),
    path("auth/login/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("auth/refresh-token/", TokenRefreshView.as_view(), name="token-refresh"),
    path("auth/forget-password/", ForgotPasswordView.as_view(), name="forget-password"),
    path("auth/reset-password/", ResetPasswordView.as_view(), name="reset-password"),
    path("auth/change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("", include(router.urls)),
]
