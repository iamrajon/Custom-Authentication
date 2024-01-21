from django.urls import path
from authapp import views

from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm, MySetPasswordForm, MyPasswordChangeForm



# List of urls
urlpatterns = [
    path("signup/", views.signup_view, name="sign-up"),
    path('verify_otp/<str:name>/', views.verify_otp_view, name="verify-otp"),
    path("login/", views.login_view, name="log-in"),
    path("logout/", views.logout_view, name="log-out"),
    path('', views.home_view, name="home"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password-reset.html", form_class=MyPasswordResetForm), name="password-reset"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password-reset-confirm.html", form_class=MySetPasswordForm), name="password_reset_confirm"),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name="password-reset-done.html"), name="password_reset_done"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-complete.html"), name="password_reset_complete"),

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name="password-change.html", form_class=MyPasswordChangeForm), name="password_change"),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name="password-change-done.html"), name="password_change_done"),
]
