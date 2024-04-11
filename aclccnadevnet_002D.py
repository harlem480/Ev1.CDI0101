# Sección: CCNA DEVNET_002D
aclNum = int(input("Ingrese el número de ACL IPv4 para saber si es estandar o extendida: "))

# Verificar el tipo de ACL IPv4
if 1 <= aclNum <= 99:
    print("Esta ACL es  IPv4 estándar.")
elif 100 <= aclNum <= 199:
    print("Esta ACL es  IPv4 extendida.")
else:
    print("El número de ACL IPv4 no corresponde a ninguna categoría estándar o extendida.")
