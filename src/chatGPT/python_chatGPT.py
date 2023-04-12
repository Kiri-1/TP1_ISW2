
# Escriba un programa en lenguaje Python que basándose en el esqueleto previamente proporcionado acepte una consulta del usuario, verifique si la misma tiene texto, imprima su contenido, invoque el API de chatGPT con esa consulta e imprima en pantalla el resultado que se obtenga como respuesta. El contenido de la consulta debe agregársele “You:” antes de imprimirlo y de enviarlo. La respuesta de chatGPT deberá agregársele “chatGPT: “antes de imprimirse.

# https://platform.openai.com/docs/api-reference //documentacion 

import openai

openai.api_key = "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"

while True:
    try:
        # Se llama prompt al carácter o conjunto de caracteres que se muestran en una línea de comandos para indicar que está a la espera de órdenes.
        print ('Ingrese una pregunta a chatGPT -- exit para finalizar')
        prompt = input("\nYou: ") # El sistema operativo trae a travez del imput permitir la funcionalidad de "cursor Up".

        if prompt == "":
            continue
        # Se detiene el programa cuando ingresa un exit al prompt.
        # .lower() Convierte una cadena de caracteres a minúsculas.
        if prompt.lower() == "exit" :
            print("Hasta pronto!")
            break

        # Agregamos "You:" al inicio de la consulta.
        prompt = "You: " + prompt

        TOP_P=1
        FREQ_PENALTY=0
        PRES_PENALTY=0
        STOP=None
        MAX_TOKENS=1024
        TEMPERATURE=0.75
        NMAX=1
        MODEL_ENGINE = "text-davinci-003"

        completion = openai.Completion.create(engine=MODEL_ENGINE,
                                          prompt=prompt,
                                          max_tokens=MAX_TOKENS,
                                          n=NMAX,
                                          top_p=TOP_P,
                                          frequency_penalty=FREQ_PENALTY,
                                          presence_penalty=PRES_PENALTY,
                                          temperature=TEMPERATURE,
                                          stop=STOP)
    
        # Agregamos "chatGPT: " al inicio de la respuesta.
        response = "chatGPT: " + completion.choices[0].text
        print(response) # Imprime la respuesta.

    # Agregue al programa anterior estructuras Try:/Except: para gestionar problemas en la ejecución, coloque un nido para la aceptación de consulta desde el usuario, otro para su tratamiento y un tercero para la invocación.
    
    # Excepciones para manejar errores relacionados con la autenticación.
    except openai.error.AuthenticationError:
        print("Ha ocurrido un error de autenticación. Por favor, revisa tu API key.")
        break

    # En la llamada a la API y otros errores genéricos.    
    except openai.error.APIError as e:
        print(f"Ha ocurrido un error al llamar a la API: {e}")
        break

    # Condición para ignorar las consultas vacías.
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        break