from django.core.management.base import BaseCommand
from cuentaAPP.models import Cuenta

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Crear cuentas de ejemplo
        Cuenta.objects.create(
            tipo_cuenta=Cuenta.TipoCuenta.Casa,
            usario = None)
        
        Cuenta.objects.create(
            tipo_cuenta=Cuenta.TipoCuenta.Pendiente,
            usario = None)
        

        self.stdout.write(self.style.SUCCESS('Cuentas del sistema creadas exitosamente.'))