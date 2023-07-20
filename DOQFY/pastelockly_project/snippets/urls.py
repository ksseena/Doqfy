from django.urls import path
from snippets import views

urlpatterns = [
    path('', views.create_snippet, name='create_snippet'),
    path('view<str:snippet_id>/', views.view_snippet, name='view_snippet'),
]
