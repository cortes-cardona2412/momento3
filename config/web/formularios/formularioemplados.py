from django import forms

class FormularioRegistroEmpleados(forms.Form):

    
    nombreempleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Nombre"
    )
    apellidoempleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Apellido"
    )

    telefonoempleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label="Telefono"
    )
    direccionempleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True,
        label="Direccion"
    )
    cedulaempleado=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label="Cedula"
    )
   
