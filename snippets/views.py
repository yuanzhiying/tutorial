from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
# Create your views here.


class SnippetList(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
