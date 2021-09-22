from django.urls import path
from .views import urliew, ShortenedUrlView, works

urlpatterns = [
    path('', ShortenedUrlView.as_view(), name="main"),
    path('<uuid:id>', urliew, name="yeah"),
    path('works', works, name="works"),
]