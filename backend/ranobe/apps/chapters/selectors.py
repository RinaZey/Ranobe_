from chapters.models import Chapter
from django.db.models import QuerySet, ObjectDoesNotExist
import django_filters


class ChapterFilter(django_filters.FilterSet):
    ranobe = django_filters.NumberFilter(field_name='ranobe')
    order_by = django_filters.OrderingFilter(
        fields=(
            ('updated_at', 'updated'),
            ('created_at', 'added')
        )
    )

    class Meta:
        model = Chapter
        fields = ('ranobe', )


def get_chapters_list(*, ranobe_slug) -> QuerySet[Chapter]:
    result = Chapter.objects.filter(ranobe__slug=ranobe_slug)

    if result.exists():
        return result

    raise ObjectDoesNotExist(f'Ranobe с тегом - {ranobe_slug} не найдено')


def get_chapter_by_id(pk: int) -> Chapter:
    return Chapter.objects.get(pk=pk)


def get_chapter_list_by_slice(slice: tuple[int], ranobe_slug: str) -> QuerySet[Chapter]:
    chapters = get_chapters_list(ranobe_slug=ranobe_slug)

    return chapters[slice[0]:slice[1]]
