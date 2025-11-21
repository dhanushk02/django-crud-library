from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('book/create/', views.book_create, name='book-create'),
    path('book/<int:pk>/update/', views.book_update, name='book-update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book-delete'),
]
