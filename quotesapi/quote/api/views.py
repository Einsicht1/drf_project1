from rest_framework import generics
from quote.api.permissions import IsAdminUserOrReadOnly
from quote.api.serializers import QuoteSerializer
from quote.models import Quote


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset           = Quote.objects.all().order_by("-id")
    serializer_class   = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
