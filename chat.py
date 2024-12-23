# Chatbot básico
def chatbot():
    respuestas = {
        "hola": "¡Hola! ¿En qué puedo ayudarte?",
        "¿cómo estás?": "Estoy bien, gracias por preguntar 😊",
        "adiós": "¡Adiós! Que tengas un buen día.",
        "tu nombre": "Soy un chatbot sencillo creado con Python."
    }
    
    print("¡Hola! Soy tu chatbot. Escribe 'salir' para terminar la conversación.")
    while True:
        mensaje = input("\nTú: ").lower()
        if mensaje == "salir":
            print("Chatbot: ¡Hasta luego!")
            break
        respuesta = respuestas.get(mensaje, "No entiendo esa pregunta 😕")
        print(f"Chatbot: {respuesta}")

chatbot()
