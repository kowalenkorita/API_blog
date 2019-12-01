from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response

__all__ = (
    'PageNumberPagination',
)


class PageNumberPagination(pagination.PageNumberPagination):
    """
    Пагинация по умолчанию - номер страницы + размер страницы.
    """

    page_size_query_param = 'size'

    query_params = '?{}={}&{}={}'

    def get_current_page_size(self):
        return self.page.paginator.per_page

    def get_next_page_query(self):
        if not self.page.has_next():
            return None

        return self.query_params.format(self.page_query_param,
                                        self.page.next_page_number(),
                                        self.page_size_query_param,
                                        self.get_current_page_size())

    def get_previous_page_query(self):
        if not self.page.has_previous():
            return None

        return self.query_params.format(self.page_query_param,
                                        self.page.previous_page_number(),
                                        self.page_size_query_param,
                                        self.get_current_page_size())

    def get_paginated_response(self, data):
        # links содержит только query-параметры,
        # т.к. валидный URL для обращения устанавливает фронтенд-сервер.
        links = OrderedDict()

        previous_query = self.get_previous_page_query()
        next_query = self.get_next_page_query()

        if previous_query:
            links['previous'] = previous_query

        if next_query:
            links['next'] = next_query

        return Response(OrderedDict(
            page=self.page.number,
            size=self.get_current_page_size(),
            total=self.page.paginator.count,
            total_pages=self.page.paginator.num_pages,
            items=data,
            links=links
        ))
