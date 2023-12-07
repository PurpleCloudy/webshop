from django.http import HttpRequest
from django.db.models import QuerySet
from math import ceil
from . import models


def products_pagination(request: HttpRequest, pagination_data: QuerySet[models.Product], default_size: int):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', default_size))
    pages_number = ceil(len(pagination_data) / page_size)
    if page > pages_number:
        page = pages_number
    elif page < 1:
        page = 1
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return {
            'start_index': start_index,
            'end_index': end_index,
            'pages_number': pages_number,
            'page': page,
    }
