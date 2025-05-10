from ranobes.models import Ranobe
import django_filters

class RanobeFilter(django_filters.FilterSet):
    order_by = django_filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('updated_at', 'updated'),
            ('created_at', 'added')
        )
    )

    tags = django_filters.BaseInFilter(field_name='tags__pk', lookup_expr='in')
    genres = django_filters.BaseInFilter(field_name='genres__pk', lookup_expr='in')

    class Meta:
        model = Ranobe
        fields = ('tags', 'genres', 'order_by')

def ranobe_list(*, filters=None):
    filters = filters or {}

    qs = Ranobe.objects.all()
    filter = RanobeFilter(filters, qs)

    return filter.qs

def get_ranobe(slug: str) -> Ranobe:
    return Ranobe.objects.get(slug=slug)
