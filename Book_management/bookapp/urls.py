from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('reading-lists/', views.ReadingListView.as_view(), name='reading-list'),
    path('reading-lists/<int:pk>/', views.ReadingListDetailView.as_view(), name='reading-list-detail'),
    path('reading-lists/<int:reading_list_id>/books/<int:book_id>/', views.ReadingListBookView.as_view(), name='reading-list-book'),
    
]