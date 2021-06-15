from django.urls import path
from account.api.views import registration_view



urlpatterns = [
	path('register', registration_view, name="register"),
	]