from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('verification/', include('verify_email.urls')),
    path("", include("quiz.urls")),

]
