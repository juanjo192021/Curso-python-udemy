nombre = input("Ingrese su nombre: ")
ventaTotal = float(input("Ingrese el monto de sus ventas totales en el mes: "))

comision = ventaTotal * 0.13

print(f"El empleado {nombre} debería recibir {comision} de comisión")