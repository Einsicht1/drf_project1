from django.urls import path
from quote.api.views import QuoteDetailAPIView, QuoteListCreateAPIView

urlpatterns = [
    path("quotes/", QuoteListCreateAPIView.as_view(), name="quote-list"),
    path("quotes/", QuoteDetailAPIView.as_view(), name="quote-detail"),

]
