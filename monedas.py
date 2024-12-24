
tasas_cambio = {
    "usd_to_eur": 0.92,
    "usd_to_mxn": 17.5,
    "eur_to_usd": 1.09,
    "eur_to_mxn": 19.0,
    "mxn_to_usd": 0.057,
    "mxn_to_eur": 0.052
}

def convertir_moneda():
    print("\nConversor de Monedas")
    print("Opciones disponibles: USD, EUR, MXN")
    origen = input("Moneda de origen: ").upper()
    destino = input("Moneda de destino: ").upper()
    try:
        monto = float(input(f"Monto en {origen}: "))
        clave = f"{origen.lower()}_to_{destino.lower()}"
        if clave in tasas_cambio:
            convertido = monto * tasas_cambio[clave]
            print(f"{monto} {origen} equivale a {convertido:.2f} {destino}.")
        else:
            print("Conversión no disponible.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

convertir_moneda()
