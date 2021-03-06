from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import forms, views as auth_views
from django.urls import conf, path, include
from users import views as user_views


EwooralsaysChangePasswordViews = user_views.PasswordsChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('account/', user_views.account, name='account'),
    path('account/<int:id>/delete/', user_views.remove_mt_account, name='account_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('pages.urls')),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='users/change_password.html')),
    path('password/', EwooralsaysChangePasswordViews.as_view(template_name='users/change_password.html')),
    path('password_success/', user_views.password_success, name='password_success'),
    #     forgot password functionality
    path('password-reset/', auth_views.PasswordResetView.as_view(
                      template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
      template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
      template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
      template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]

# We are just adding this when we're in debug mode, so don't get it twisted... smile
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
