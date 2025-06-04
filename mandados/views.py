from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login_registro.models import Usuario
from django.urls import reverse
from .models import Mandado
from django.shortcuts import render, redirect, get_object_or_404

@csrf_exempt
def crear_mandado(request):
    if request.method == 'POST':
        usuario_id = request.session.get('usuario_id')
        if not usuario_id:
            return JsonResponse({'success': False, 'mensaje': 'Usuario no autenticado.'})

        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        costo = request.POST.get('costo')
        numContacto = request.POST.get('numContacto')

        if not all([titulo, descripcion, costo, numContacto]):
            return JsonResponse({'success': False, 'mensaje': 'Todos los campos son obligatorios.'})

        try:
            usuario = Usuario.objects.get(id=usuario_id)
            Mandado.objects.create(
                idUsuario=usuario,
                titulo=titulo,
                descripcion=descripcion,
                costo=costo,
                numContacto=numContacto
            )
            return JsonResponse({'success': True, 'mensaje': 'Mandado creado exitosamente.'})
        except Exception as e:
            return JsonResponse({'success': False, 'mensaje': f'Error al crear mandado: {str(e)}'})

    return JsonResponse({'success': False, 'mensaje': 'Método no permitido.'})

def listar_mandados(request):
    mandados = Mandado.objects.all().order_by('-fecha')  # muestra los más recientes primero
    return render(request, 'dashboard/dashboard.html', {'mandados': mandados, 'usuario_id': request.session.get('usuario_id')})

def aceptar_mandado(request, mandado_id):
    mandado = get_object_or_404(Mandado, pk=mandado_id)

    # Solo asignar repartidor si no hay uno ya
    if mandado.repartidor is None:
        usuario_id = request.session.get('usuario_id')
        if usuario_id:
            repartidor = Usuario.objects.get(pk=usuario_id)
            mandado.repartidor = repartidor
            mandado.save()

            # Redirige a la vista seguimiento con mandado.id, cliente_id, repartidor_id y rol 'repartidor'
            url = reverse('seguimiento', args=[mandado.id, mandado.idUsuario.id, mandado.repartidor.id, 'cliente'])
            return redirect(url)

    # Si ya tiene repartidor, redirige a listado u otra vista (ajusta según tu lógica)
    return redirect('mandados_list')  # O la ruta que uses para listar mandados