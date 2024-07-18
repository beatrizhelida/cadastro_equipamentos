from django.urls import path
from app_desafio.views import EquipamentoList, EquipamentoDetail, EquipamentoCreate, EquipamentoDelete


urlpatterns =[

    path('api/equipamentos/', EquipamentoList.as_view(), name='equipamento-list'),
    path('api/equipamentos/<int:pk>/', EquipamentoDetail.as_view(), name='equipamento-detail'),
    path('api/equipamentos/add/', EquipamentoCreate.as_view(), name='equipamento-add'),
    path('equipamentos/delete/<int:pk>/', EquipamentoDelete.as_view(), name='equipamento-delete'),
]