from django.urls import path
from django.views.generic import FormView
from django.urls import re_path

from project_management.views import *

urlpatterns = [
    path('status/ongoing', StatusViewOngoing.as_view(), name='status'),
    path('status/completed', StatusViewCompleted.as_view(), name='status-completed'),
    path('status/detail/<int:pk>/', StatusDetail.as_view(), name='status-detail'),
    path('status/create', StatusCreate.as_view(), name='status-create'),
    path('status/edit/<int:pk>/', StatusEdit.as_view(), name='status-edit'),
    path('status/delete/<int:pk>/', StatusDelete.as_view(), name='status-delete'),
]
