from rest_framework import viewsets
from rest_framework.response import Response

from .models import User, News, Tag
from .serializers import UserSerialiser, NewsSerialiser, TagSerialiser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerialiser

    def list(self, request, *args, **kwargs):
        if bool(request.query_params):
            queryset = News.objects.filter(author_id=request.query_params['author'])
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerialiser
