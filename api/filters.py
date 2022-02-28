from django_filters import *
from .models import *


class CategoryFilter(FilterSet):
    created_at_max = DateTimeFilter(field_name="created_at", lookup_expr="lte")
    created_at_min = DateTimeFilter(field_name="created_at", lookup_expr="gte")

    class Meta:
        model = Category
        fields = ['name']


class ProductFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
    )
    min_price = NumberFilter(field_name="price", lookup_expr="lte")
    max_price = NumberFilter(field_name="price", lookup_expr='gte')

    class Meta:
        model = Product
        fields = ['name', 'size']
