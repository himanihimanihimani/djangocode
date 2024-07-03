from django.urls import path
from base import views
urlpatterns = [
    path("create/", views.create_todo, name="create"),
    path("login/", views.logiinpage, name="login"),
    path("register/", views.registerpage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path('update/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
]