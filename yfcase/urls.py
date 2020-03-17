from django.urls import path
from . import views

urlpatterns = [
	path('', views.CaseListView.as_view(), name='case_list'),
	path('new/', views.CaseCreateView.as_view(), name='case_new'),
	path('<int:pk>/edit/',views.CaseUpdateView.as_view(), name='case_edit'), # new
	path('<int:pk>/',views.CaseDetailView.as_view(), name='case_detail'), # new
	path('<int:pk>/delete/',views.CaseDeleteView.as_view(), name='case_delete'), # new
]
