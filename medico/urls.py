from django.urls import path
from .views import (EspecialidadeListView, EspecialidadeCreateView, EspecialidadeUpdateView, EspecialidadeDeleteView, MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView)

urlpatterns = [
    path('especialidade/', EspecialidadeListView.as_view(), name='especialidade_list'),
    path('especialidade/create/', EspecialidadeCreateView.as_view(), name='especialidade_create'),
    path('especialidade/<int:pk>/update/', EspecialidadeUpdateView.as_view(), name='especialidade_edit'),
    path('especialidade/<int:pk>/delete/', EspecialidadeDeleteView.as_view(), name='especialidade_delete'),
    path('medico/', MedicoListView.as_view(), name='medico_list'),
    path('medico/create/', MedicoCreateView.as_view(), name='medico_create'),
    path('medico/<int:pk>/update/', MedicoUpdateView.as_view(), name='medico_edit'),
    path('medico/<int:p>/delete/', MedicoDeleteView.as_view(), name='medico_delete'),
]

