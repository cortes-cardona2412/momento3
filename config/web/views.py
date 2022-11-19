from django.shortcuts import render
from web.formularios.formularioplatos import FormularioRegistroPlatos
from web.formularios.formularioemplados import FormularioRegistroEmpleados
from web.models import Platos,Empleados

# Create your views here.

# Cada vista es una funcion de python

def Home(request):
    return render(request,'index.html')

def PlatosVista(request):

    #Cargar el formulario de registro de platos
    formulario=FormularioRegistroPlatos()

    #creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatos={
        'formulario':formulario
    }
    
    #Recibiendo datos del formulario
    #PETICION DE TIPO POST

    if request.method=='POST':
        datosFormulario=FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            platoNuevo=Platos(
                nombre=datosLimpios["nombrePlato"],
                descripcion=datosLimpios["descripcionPlato"],
                imagen=datosLimpios["fotoPlato"],
                precio=datosLimpios["precioPlato"],
                tipo=datosLimpios["tipoPlato"]
            )
            platoNuevo.save()

    return render(request,'platos.html',diccionarioEnvioDatos)  

def EmpleadosVista(request):
    formulario=FormularioRegistroEmpleados()

    #creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatos={
        'formulario':formulario
    }
    #Recibiendo datos del formulario
    #PETICION DE TIPO POST

    if request.method=='POST':
        datosFormulario=FormularioRegistroEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            #enviando datos a mi base de datos
            empleadoNuevo=Empleados(
                nombre=datosLimpios["nombreempleado"],
                apellido=datosLimpios["apellidoempleado"],
                telefono=datosLimpios["telefonoempleado"],
                direccion=datosLimpios["direccionempleado"],
                cedula=datosLimpios["cedulaempleado"]
            )
            empleadoNuevo.save()
            
            
    return render (request, 'empleados.html',diccionarioEnvioDatos)      