from .models import Equipamento
from .serializers import DesafioSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect


class EquipamentoList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'equipamentos.html'
    def get(self, request):
        equipamentos = Equipamento.objects.all()
        return Response({'equipamentos': equipamentos})

class EquipamentoDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detalhe_equipamento.html'
    def get(self, request, pk):
        equipamento = get_object_or_404(Equipamento, pk=pk)
        serializer = DesafioSerializer(equipamento)
        return Response({'serializer': serializer, 'equipamento': equipamento})
    def post(self, request, pk):
        equipamento = get_object_or_404(Equipamento, pk=pk)
        serializer = DesafioSerializer(equipamento, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'equipamento': equipamento})
        serializer.save()
        return redirect('equipamento-list')
    
class EquipamentoCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_equipamento.html'
    def get(self, request):
        serializer = DesafioSerializer
        return Response({'serializer': serializer})
    def post(self, request):
        serializer = DesafioSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('equipamento-list')

class EquipamentoDelete(APIView):
    def post(self, request, pk):
        equipamento = get_object_or_404(Equipamento, pk=pk)
        equipamento.delete()
        return redirect('equipamento-list')
