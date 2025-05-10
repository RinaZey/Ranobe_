from django.urls import path

from chapters.apis import (
    ChapterDetailAPI,
    ChapterAPI
)

urlpatterns = [
    path('', ChapterAPI.as_view(), name='list-or-create-chapter'),
    path('<int:pk>/', ChapterDetailAPI.as_view(),
         name='get-delete-update-chpater')
]
