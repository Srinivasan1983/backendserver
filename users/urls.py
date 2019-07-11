from django.urls import include, path 

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),

    path('genres/', views.GenreListCreate.as_view(), name=views.GenreListCreate.name),
    path('genres/<int:pk>/', views.GenreRetrieveUpdate.as_view(), name=views.GenreRetrieveUpdate.name),

    path('movies/', views.MovieListCreate.as_view(), name=views.MovieListCreate.name),
    path('movies/<int:pk>)/', views.MovieRetrieveUpdate.as_view(), name=views.MovieRetrieveUpdate.name),

    path('comments/', views.CommentListCreate.as_view()),
    path('comments/<int:pk>)/', views.CommentRetrieveUpdate.as_view()),
]
