from django.urls import path

from .views import home, book_detail


urlpatterns = [
    path('', home, name='home'),
    path('books/<int:book_id>/', book_detail, name='detail'),
]