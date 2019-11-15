from django.urls import path

from jobs.api.views import JobOfferListCreateView, JobOfferDetailView

urlpatterns = [
    path('jobs/', JobOfferListCreateView.as_view(), name='jobs-list'),
    path('jobs/<int:pk>', JobOfferDetailView.as_view(), name='jobs-detail'),
]
