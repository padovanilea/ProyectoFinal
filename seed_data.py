from ejemplo.models import Familiar

Familiar(nombre="Pablo", direccion="Alsina 4040", numero_pasaporte=111223344).save()
Familiar(nombre="Ivone", direccion="Alsina 4040", numero_pasaporte=22334455).save()
Familiar(nombre="Lucas", direccion="Alsina 4040", numero_pasaporte=33445566).save()
Familiar(nombre="Kiara", direccion="Alsina 4040", numero_pasaporte=44556677).save()

print("Se cargo con éxito los usuarios de pruebas")