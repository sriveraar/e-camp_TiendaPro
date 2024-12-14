from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tiendapp.models import Customer, Order, OrderDetail
from tiendapp.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("tienda tests")
        print("Comprando el MackBook Pro: ")
        mackbook = Product.objects.get(id = 2)
        print(">", mackbook.name)
        
        print("Creando un cliente: ")
        nuevo_user = User.objects.filter(username = "hanslam@gmail.com").first()
        if nuevo_user is None:
            nuevo_user.first_name = "Hans"
            nuevo_user.last_name = "Lambda"
            nuevo_user.username = "hanslam@gmail.com"
            nuevo_user.is_active = True
            nuevo_user.save() # Almacena en base de datos al usuario
            
            nuevo_user.set_password("123456") # Define una contraseña
            nuevo_user.save()
            ## Fin de la creación de un usuario
            
        print("Enlazar el user al customer: ")
        nuevo_customer = Customer.objects.filter(user = nuevo_user).first()
        if nuevo_customer is None:
            nuevo_customer = Customer()
            nuevo_customer.user = nuevo_user # Enlace
            nuevo_customer.billing_address = "Las flores 3434. Concepción"
            nuevo_customer.shipping_address = "Av. liertad 12412. Concepción"
            nuevo_customer.phone = "325252112"
            nuevo_customer.save()
            
        print("Creando una orden para el customer: ")    
        nueva_order = Order.objects.filter(customer = nuevo_customer).first()
        if nueva_order is None:
            nueva_order = Order()
            nueva_order.customer = nuevo_customer
            nueva_order.shipping_address = nuevo_customer.shipping_address
            nueva_order.status = "PENDIENTE"
            nueva_order.save()