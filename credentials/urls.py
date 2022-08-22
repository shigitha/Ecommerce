from django.urls import path

from credentials import views

app_name="credentials"

urlpatterns = [
    path('/register',views.register,name='register'),

    ]