from django.urls import path
from .views import AboutPageView, HomePageView, SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('snacks/', SnackListView.as_view(), name='snack_list'),
    path('snacks/<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
        path('snacks/create/', SnackCreateView.as_view(), name='snack_create'),
    path('snacks/<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'), 
    path('snacks/<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete'), 
]
