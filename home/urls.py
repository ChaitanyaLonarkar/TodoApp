
from django.contrib import admin
from django.urls import path,include
from . import views
# from home import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('tasks/', views.tasks,name='tasks'),
    path('tasks/update<str:pk>/', views.update,name='update'),
    path('tasks/delete<str:pk>/', views.delete,name='delete'),
    path('login/', views.login_page,name='login'),
    path('register/', views.register_page,name='register'),
    path('logout/', views.logout_page,name='logout'),

]
