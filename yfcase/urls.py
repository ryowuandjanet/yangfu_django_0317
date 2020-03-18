from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
	path('', views.CaseListView.as_view(), name='case_list'),
	# path('new/', views.CaseCreateView.as_view(), name='case_new'),
	path('add/', views.CaseFamilyCreateView.as_view(), name='case_add'),
	# path('<int:pk>/edit/',views.CaseUpdateView.as_view(), name='case_edit'), # new
	path('<int:pk>/edit/',views.CaseFamilyUpdateView.as_view(), name='case_edit'), # new
	path('<int:pk>/',views.CaseDetailView.as_view(), name='case_detail'), # new
	path('<int:pk>/delete/',views.CaseDeleteView.as_view(), name='case_delete'), # new
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
