from django.shortcuts import render
from mandados.models import Mandado


def dashboard_view(request):
    mandados = Mandado.objects.all().order_by('-fecha')
    usuario_id = request.session.get('usuario_id')
    usuario_nombre = request.session.get('usuario_nombre')
    return render(request, 'dashboard/dashboard.html', {
        'mandados': mandados,
        'usuario_id': usuario_id,
        'usuario_nombre': usuario_nombre
    })