from django.urls import path
from .views import ModelPlanCreateView

urlpatterns = [
    path('plans/create/', ModelPlanCreateView.as_view(), name='plan_create'),
    # path('plan/list/', ModelPlanListView.as_view(), name='plan_list'),
    # path('plan/upe/<int:pk>/', ModelPlanUpdateView.as_view(), name='plan_update'),
    # path('plan/delete/<int:pk>/', ModelPlanDeleteView.as_view(), name='plan_delete'),
]