from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewset

# urlpatterns = [
#     path("books/", views.BookListCreate.as_view(), name="book-list"), 
#     path("books/<int:pk>/", views.BookDetail.as_view(), name="book-detail"),
# ]

router = DefaultRouter()
router.register(r"books", BookViewset, basename="book")
router.register(r"books/<int:pk>", BookViewset, basename="book-detail")

urlpatterns = router.urls
