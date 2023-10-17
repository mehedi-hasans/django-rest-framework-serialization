from django.urls import path
from snippets import views

urlpatterns = [
    path('api/', views.SnippetList.as_view()),
    path('api/<int:pk>/', views.SnippetDetail.as_view()),
]