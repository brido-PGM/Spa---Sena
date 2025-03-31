from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.db.utils import IntegrityError
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .utils import *

# Create your views here.

def login(request):
    if request.method == "POST":
        error = False
        usu = None
        con = None
        try:
            usu = request.POST.get("usuario")
            con = request.POST.get("contrasena")
            if usu == "Admin" and con == '12345':
                error = False
        except:
            error: True

        contexto = {
            "usu" : usu,
            "error" : error
        }
        return render(request, "login_listo.html", contexto)
    else:
        return render(request, "login.html")

def cambiar_clave(request):
    if request.method == "POST":
        clave_actual=clave_actual.POST.get("clave_actual")
        nueva=nueva.POST.get("nueva")
        repite_nueva=repite_nueva.POST.get("repite_nueva")
        logueado = request.session.get("auth", False)
        q = Usuario.objects.get(pk=logueado["id"])
        if clave_actual == q.password:
            if nueva == repite_nueva:
                q.password = hash_password(nueva)
                q.save()
                messages.success(request, "Contraseña cambiada con exito!!")
            else:
                messages.info(request, "Contraseñas no coinciden")
        else:
            messages.warning(request, "Contraseña no concuerda")
            return redirect("cambiar_clave")
        return render(request, "usuarios/cambiar_clave.html")
    else:
        return render(request, "usuarios/cambiar_clave.html")


def inicio(request):
    print("Hola mundo...!")
    """return HttpResponse(""Hola <strong style='color:blue;'>mundo</strong>...!
                        <br>
                        <a href='../login/'>Login</a>"")
    """
    return render(request, "inicio.html")

def saludar(request, nombre, apellido):
    """
    return HttpResponse(f"Hola <b style='color:green;'>{nombre} {apellido}</b>")
    """

    contexto = {
        "nombre" : nombre,
        "apellido" : apellido
    }
    return render(request, "saludar.html", contexto)

def calculadora(request, n1, n2, operador):
    """Calculadora de dos numero dados por URL"""
    if operador == "s" or operador == "S":
        result = n1 + n2
    elif operador == "r" or operador == "R":
        result = n1 - n2
    elif operador == "m" or operador == "M":
        result = n1 * n2
    elif operador == "d" or operador == "D":
        result = n1 / n2
    else:
        result="NO se pude procesar"

    """return HttpResponse(f"Resultado: {result}")"""

    contexto = {
        "result" : result
    }
    return render(request, "calculadora.html", contexto)

def cuadrado_formulario(request):
    """Calcular el cuadrado  de un numero dado por formulario: POST"""
    # ejemplo: num = 5       resultado = 5 * 5 = 25

    if request.method == "POST":
        error = False
        num_capturado = None
        resultado = None
        try:
            num_capturado = int(request.POST.get("num1"))
            resultado = num_capturado * num_capturado
        except:
            error = True

        contexto = {
            "num1" : num_capturado,
            "resultado" : resultado,
            "error" : error
        }
        return render(request, "cuadrado_resultado.html", contexto)
    else:
        return render(request, "cuadrado.html")
    
def calc(request):
    if request.method == 'POST':
        error = False
        n1 = None
        n2 = None
        operador = None
        res = None

        try:
            n1 = int(request.POST.get('n1'))
            n2 = int(request.POST.get('n2'))
            operador = str(request.POST.get('operador'))
            if operador == '+':
                res = n1 + n2
            elif operador == '-':
                res = n1 - n2
            elif operador == '*':
                res = n1 * n2
            elif operador == '/':
                res = n1 / n2
        except:
            error = True

        contexto = {
            'n1' : n1,
            'n2' : n2,
            'res' : res,
            'error' : error
        }
        return render(request, 'calc_res.html', contexto)
    else:
        return render(request, 'calc.html')

# CRUD de servicios del SPA
def servicios(request):
    #   all() -> todos       filter() -> algunos      get() -> uno
    q = Servicio.objects.all()
    contexto = {
        'data' : q,
    }
    return render(request, "servicios/listar_servicios.html", contexto)

def usuarios(request):
    q = Usuario.objects.all()
    contexto = {
        'data' : q
    }

    return render(request, 'usuarios/listar_usuarios.html', contexto)

def eliminar_servicio(request, id_servicio):
    # obtener la instancia
    try:
        ds = Servicio.objects.get(pk=id_servicio)
        ds.delete()
        messages.success(request, 'Servicio eliminado correctamente!')
    except IntegrityError:
        messages.warning(request, 'No se pude borrar. Servicio en otra tabla')
        messages.success(request, 'ok')
        messages.error(request, 'mal')
    except Exception as e:
        messages.error(request, f'Error {e}')
        
    return redirect('servicios')

# correo electronicos
def correos1(request):
    try:
        send_mail(
            "Spa Sena - Pruebas",
            "Mensaje de prueba... desde Django",
            settings.EMAIL_HOST_USER,                  #   Correo del settings
            ["brianbedoya93@gmail.com"],            #   Correo a donde se envia
            fail_silently=False,
        )
        return HttpResponse(f"Correo enviado!!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def correos2(request):
    try:
        html_message = """
            Hola mundo <strong>Django</strong>desde mi app...
            <br>
            Bienvenido!!        
        """
        send_mail(
            "Spa Sena - Pruebas con HTML",
            "",
            settings.EMAIL_HOST_USER,
            ["brianbedoya93@gmail.com"],
            fail_silently=False,
            html_message=html_message,
        )
        return HttpResponse(f"Correo enviado!!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

# def correos3(request):
#     try:
#         u = Usuario.objects.all()
        
#         html_message = f"""
#         <table class="table table-striped table-hover">
#             <thead>
#                 <tr>
#                     <th>Nombre</th>
#                     <th>Apellido</th>
#                     <th>Correo</th>
#                     <th>Foto</th>
#                     <th>Rol</th>
#                 </tr>
#             </thead>
#             <tbody>
#                 {for u in data}
#                 <tr>
#                     <td>{{ u.nombre }}</td>
#                     <td>{{ u.apellido }}</td>
#                     <td>{{ u.correo }}</td>
#                     <td>{{ u.foto }}</td>
#                     <td>{{ u.get_rol_display }}</td>
#                     <td>
#                         <button type="button" class="btn btn-secondary">Eliminar</button>
#                         <button type="button" class="btn btn-info">Editar</button>
#                     </td>
#                 </tr>
#                 {% endfor %}
#             </tbody>
#             <tfoot></tfoot>
#         </table>
#         {% else %}
#             <p>No hay servicios aun...</p>
#         {% endif %}
#         """
#         send_mail(
#             "Spa Sena - Pruebas con HTML",
#             "",
#             settings.EMAIL_HOST_USER,
#             ["brianbedoya93@gmail.com"],
#             fail_silently=False,
#             html_message=html_message,
#         )
#         return HttpResponse(f"Correo enviado!!")
#     except Exception as e:
#         return HttpResponse(f"Error: {e}")