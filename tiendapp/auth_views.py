from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from tiendapp.models import Customer

def v_sign_up(request):
    return render(request, "tiendapp/sign_up.html")


def v_sign_up_create(request):
    if request.method == "POST":
        data = request.POST.copy()
        print(">>>>>>>>>>>>>>>", data)

        print("Creando un cliente: ")
        nuevo_user = User.objects.filter(username = data["email"]).first()
        if nuevo_user is not None:
            # Incluir mensaje "Cuenta ya existe"
            return redirect("/sign_up")
        
        if nuevo_user is None:
            # Inicio de la creación de un usuario
            nuevo_user.first_name = data["first_name"]
            nuevo_user.last_name = data["last_name"]
            nuevo_user.username = data["email"]
            nuevo_user.is_active = True

            nuevo_user.set_password("123456")  # Define una contraseña
            nuevo_user.save() # Almacena en base de datos al usuario
            # Fin de la creación de un usuario

        print("Enlazar el user al customer: ")
        nuevo_customer = Customer.objects.filter(user=nuevo_user).first()
        if nuevo_customer is None:
            nuevo_customer = Customer()
            nuevo_customer.user = nuevo_user  # Enlace
            nuevo_customer.billing_address = data["billing_address"]
            nuevo_customer.shipping_address = "Av. liertad 12412. Concepción"
            nuevo_customer.phone = data["phone"]
            nuevo_customer.save()
            
            return redirect("/sign_in")

    return redirect("/")

def v_sign_in(request):
    from django.contrib.auth import authenticate, login
    
    if request.method == "POST":
        data = request.POST.copy()
        username = data["userame"]
        password = data["password"]
        
        usuario_valido = authenticate(request, username = username, password = password)
        if usuario_valido is not None:
            login(request, usuario_valido)
            return redirect("/")
        else:
            pass

    return render(request, "tiendapp/sign_in.html")