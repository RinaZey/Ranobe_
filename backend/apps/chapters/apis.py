from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.core.utils import get_response_data

from chapters.types import ChapterObject

from backend.apps.chapters.schemas import (
    ChapterSerializer,
    ChapterUpdateSerializer,
    ChapterCreateSerializer
)

from chapters.services import (
    create_chapter,
    update_chapter
)

from backend.apps.chapters.selectors import (
    get_chapter_by_id,
    get_chapters_list
)

class ChapterDetailAPI(APIView):
    """API для получения, обновления и удаления экземпляра главы"""

    def get(self, pk: int) -> Response:
        chapter = get_chapter_by_id(pk=pk)

        data = ChapterSerializer(chapter).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data)

    def delete(self, request, pk: int) -> Response:
        chapter = get_chapter_by_id(pk)
        self.check_object_permissions(request, chapter)

        data = ChapterSerializer(chapter).data

        chapter.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Успешно удалено')

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, pk: int) -> Response:
        chapter = get_chapter_by_id(pk)
        self.check_object_permissions(request, chapter)

        serializer = ChapterUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        chapter = update_chapter(chapter, ChapterObject(
            **serializer.validated_data))

        data = ChapterSerializer(chapter).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data, status=status.HTTP_200_OK)


class ChapterAPI(APIView):
    """API для получения списка глав или создания экземпляров"""

    def get(self, slug: str) -> Response:
        queryset = get_chapters_list(novel_slug=slug)

        data = ChapterSerializer(queryset, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, slug: str) -> Response:
        serializer = ChapterCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        chapter_object = ChapterObject(**serializer.data, novel=slug)

        chapter = create_chapter(chapter_object)

        data = ChapterSerializer(chapter).data
        data = get_response_data(status.HTTP_201_CREATED, data)

        return Response(data=data, status=status.HTTP_201_CREATED)
