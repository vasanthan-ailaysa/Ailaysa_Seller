from django.urls import path
from .views import BookCreate , BookDetail ,LanguageCreate ,LanguageDetail ,GenreCreate ,GenreDetail ,FormatCreate ,FormatDetail


urlpatterns =[

    path ('books/',BookCreate.as_view() , name ='book-create'),
    path('books/<int:pk>/',BookDetail.as_view(),name='book-detail'),
    
    path ('languages/',LanguageCreate.as_view() , name ='language-create'),
    path('languages/<int:pk>/',LanguageDetail.as_view(),name='language-detail'),
    
    path ('genres/',GenreCreate.as_view() , name ='genre-create'),
    path('genres/<int:pk>/',GenreDetail.as_view(),name='genre-detail'),
    
    path ('formats/',FormatCreate.as_view() , name ='format-create'),
    path('formats/<int:pk>/',FormatDetail.as_view(),name='format-detail')
    
]










