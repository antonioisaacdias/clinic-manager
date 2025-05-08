from django.urls import path
from .views import ModelPlanCreateView, ModelPlanListView, ModelPlanDetailView, change_plan_activity_view, ModelPlanDeleteView, ModelPlanUpdateView

urlpatterns = [
    path('plans/create/', ModelPlanCreateView.as_view(), name='plan_create'),
    path('plan/list/', ModelPlanListView.as_view(), name='plan_list'),
    path('plan/<uuid:pk>/', ModelPlanDetailView.as_view(), name='plan_detail'),
    path('plan/<uuid:pk>/active/', change_plan_activity_view, name='plan_active'),
    path('plan/<uuid:pk>/update/', ModelPlanUpdateView.as_view(), name='plan_update'),
    path('plan/<uuid:pk>/delete/', ModelPlanDeleteView.as_view(), name='plan_delete'),
]
