from django.shortcuts import render
from mandados.models import Mandado

def dashboard_view(request):
    usuario_id = request.session.get('usuario_id')
    usuario_nombre = request.session.get('usuario_nombre')
    vista_actual = request.GET.get('vista', '')  # Puede ser: '', 'publicar', 'disponibles'

    mandados = Mandado.objects.none()
    mandados_disponibles = Mandado.objects.none()
    mandado_actual = None

    if usuario_id:
        if vista_actual == 'publicar':
            # Solo los mandados publicados por el usuario actual
            mandados = Mandado.objects.filter(idUsuario__id=usuario_id).order_by('-fecha')

        elif vista_actual == 'disponibles':
            # Mandados sin repartidor y que no fueron publicados por el usuario actual
            mandados = Mandado.objects.filter(
                repartidor__isnull=True
            ).exclude(idUsuario__id=usuario_id).order_by('-fecha')

            # Mandado que el usuario ha aceptado (1 solo activo)
            mandado_actual = Mandado.objects.filter(
                repartidor__id=usuario_id
            ).order_by('-fecha').first()

    context = {
        'mandados': mandados,
        'mandado_actual': mandado_actual,
        'usuario_id': usuario_id,
        'usuario_nombre': usuario_nombre,
        'vista_actual': vista_actual,
    }

    return render(request, 'dashboard/dashboard.html', context)
