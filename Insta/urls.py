
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Home,name='home'),
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('like/<int:id>/',views.Like,name='like'),
    path('profile/',views.Profile,name='profile'),
    path('add_profile/',views.EditProfile,name='add-profile')

]
