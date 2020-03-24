from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from araf_sport import views as user_view

urlpatterns = [
    path('', user_view.index, name='index'),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(template_name='araf_sport/logout.html'), name='logout'),
    path('workouts/', user_view.workouts, name='workouts'),
    path('pics', user_view.pics, name='pics'),

]
