from django.urls import path
from . import views
app_name = 'library'


urlpatterns = [
    path("",views.home,name='home'),
    path('addbook/',views.addbook,name='addbook'),
    path('savebook/',views.save_book,name='save_book'),
    path('edit_book/<int:book_id>',views.edit_book,name='edit_book'),
    path('delete_book/<int:book_id>',views.delete_book,name='delete_book'),
    path('save_edited_book',views.save_edited_book,name='save_edited_book'),
]