from django.urls import path
from . import views

urlpatterns = [
# Dashboard  
path('', views.dashboard, name='dashboard'),  

# Users  
path('users/', views.users, name='users'),  
path('add-user/', views.add_user, name='add_user'),  
path('edit-user/<int:id>/', views.edit_user, name='edit_user'),  
path('delete-user/<int:id>/', views.delete_user, name='delete_user'),  

# Books  
path('books/', views.books, name='books'),  
path('add-book/', views.add_book, name='add_book'),  
path('edit-book/<int:id>/', views.edit_book, name='edit_book'),  
path('delete-book/<int:id>/', views.delete_book, name='delete_book'),  

# Records  
path('borrow-book/', views.borrow_book, name='borrow_book'),  
path('return-book/<int:id>/', views.return_book, name='return_book'),  
path('open_records/', views.open_records, name='open_records'),  
path('closed-records/', views.closed_records, name='closed_records'),  

#Details  
path('user/<int:id>/', views.user_detail, name='user_detail'),  
path('book/<int:id>/', views.book_detail, name='book_detail'),  
path('record/<int:id>/', views.record_detail, name='record_detail'),  

]