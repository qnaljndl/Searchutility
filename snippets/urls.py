from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.Userlist.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('usersearch', views.UserSearch.as_view()),
    path('search', views.Search.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)