from django.urls import path
from snippets import views

urlpatterns = [
    path('api/', views.SnippetList.as_view()),
    # path('apid/<int:pk>/', views.snippet_detail),
]