from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.views import APIView
from rest_framework import status

from apps.core.utils import get_response_data

from apps.ranobes.services import (
    create_ranobe,
    update_ranobe,
)
from apps.ranobes.selectors import (
    ranobe_list,
    get_ranobe
)

from apps.core.pagination import (
    get_paginated_response
)
from apps.ranobes.types import RanobeObject
from backend.apps.ranobes.schemas import (
    RanobeSerializer,
    RanobeCreateSerializer,
    RanobeUpdateSerializer,
    RanobeFilterSerializer,
    RanobeListSerializer
)

class RanobeAPI(APIView):
    """API для получения списка ranobe или создания экземпляра ranobe"""
    parser_classes = (MultiPartParser, JSONParser)

    def post(self, request) -> Response:
        serializer = RanobeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ranobe = create_ranobe(RanobeObject(**serializer.validated_data))

        data = RanobeSerializer(ranobe).data
        data = get_response_data(status.HTTP_201_CREATED, data)

        return Response(data=data,
                        status=status.HTTP_201_CREATED)

    def get(self, request) -> Response:
        filter_serializer = RanobeFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        ranobes = ranobe_list(filters=filter_serializer.validated_data)

        return get_paginated_response(
            serializer_class=RanobeListSerializer,
            queryset=ranobes,
            view=self,
            request=request
        )

class RanobeDetailAPI(APIView):
    """API для получения, удаления и обновления экземпляра ranobe"""

    def get(self, slug: str) -> Response:
        ranobe = get_ranobe(slug=slug)

        data = RanobeSerializer(ranobe).data

        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data)

    def delete(self, request, slug: str) -> Response:
        ranobe = get_ranobe(slug)
        self.check_object_permissions(request, ranobe)

        data = RanobeSerializer(ranobe).data

        ranobe.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Успешно удалено!')

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, slug: str) -> Response:
        ranobe = get_ranobe(slug)
        self.check_object_permissions(request, ranobe)

        serializer = RanobeUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        ranobe = update_ranobe(ranobe, RanobeObject(**serializer.validated_data))

        data = RanobeSerializer(ranobe).data

        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)
