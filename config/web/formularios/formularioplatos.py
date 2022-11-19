from django import forms

class FormularioRegistroPlatos(forms.Form):

    platos=(
        (1,'Entrada'),
        (2,'Plato Fuerte'),
        (3,'Postre'),
        (4,'Bebidas')
    )
    
    nombrePlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Nombre"
    )
    descripcionPlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label="Descripcion"
    )
    fotoPlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True,
        label="Foto"
    )
    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label="Precio"
    )
    tipoPlato=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        choices=platos
    )
