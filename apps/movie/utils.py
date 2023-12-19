from rest_framework.pagination import PageNumberPagination


class TestPagination(PageNumberPagination):
    page_size = 10
