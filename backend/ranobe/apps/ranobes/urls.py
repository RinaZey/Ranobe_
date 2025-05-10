from django.urls import path, include

from ranobes.apis import (
    RanobeAPI,
    RanobeDetailAPI
)

from apps.chapters.apis import (
    ChapterAPI,
    ChapterDetailAPI
)

chapter_patterns = [
    path('', ChapterAPI.as_view(), name='chapter'),
    path('<int:pk>/', ChapterDetailAPI.as_view(),
         name='detail-chapter'),
]

ranobe_detail_patterns = [
    path('', RanobeDetailAPI.as_view(), name='detail'),
    path('chapters/', include((chapter_patterns, 'chapters'))),
]

ranobe_patterns = [
    path('', RanobeAPI.as_view(), name='list-or-create-ranobe'),
    path('<slug:slug>/', include((ranobe_detail_patterns, 'ranobe-detail')))
]

urlpatterns = [
    path('', include((ranobe_patterns, 'ranobes'))),
]
