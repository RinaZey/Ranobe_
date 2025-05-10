from django.urls import path, include

from .apis.tag import (
    TagAPI,
    TagDetailAPI
)

from .apis.genre import (
    GenreAPI,
    GenreDetailAPI
)

genre_patterns = [
    path('', GenreAPI.as_view(), name='list-or-create-genre'),
    path('<int:pk>/', GenreDetailAPI.as_view(),
         name='get-delete-update-genre')
]

tag_patterns = [
    path('', TagAPI.as_view(), name='list-or-create-tag'),
    path('<int:pk>/', TagDetailAPI.as_view(),
         name='get-delete-update-tag')
]

urlpatterns = [
    path('tags/', include((tag_patterns, 'tags'))),
    path('genres/', include((genre_patterns, 'genres'))),
]
