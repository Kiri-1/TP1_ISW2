
# Escriba un programa en lenguaje Python que basándose en el esqueleto previamente proporcionado acepte una consulta del usuario, verifique si la misma tiene texto, imprima su contenido, invoque el API de chatGPT con esa consulta e imprima en pantalla el resultado que se obtenga como respuesta. El contenido de la consulta debe agregársele “You:” antes de imprimirlo y de enviarlo. La respuesta de chatGPT deberá agregársele “chatGPT: “antes de imprimirse.

# https://platform.openai.com/docs/api-reference //documentacion. 

import openai
import argparse

# Configuración de argumentos de la línea de comando.
parser = argparse.ArgumentParser(description='Programa de chat con GPT-3')
parser.add_argument('--convers', action='store_true', help='Habilita el modo de conversación')
args = parser.parse_args()

openai.api_key = "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"

# Parámetros de la API.
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"

# Buffer para almacenar las consultas y respuestas anteriores.
conver_buffer = []

# Función para imprimir el contenido de la consulta o la respuesta.
def print_message(message, is_user_message=True):
    prefix = "You: " if is_user_message else "chatGPT: "
    print(prefix + message)

print("Bienvenido a chatGPT")
# Bucle principal para el modo de conversación.
while args.convers:
    user_input = input("Ingrese su consulta a chatGPT: ")
    
    # Si la consulta es nula, se ignora y se vuelve a pedir.
    if not user_input:
        continue
    
    # Salir del modo conversación al ingresar "salir".
    if user_input == "salir":
        break
    
    # Agregar la consulta al buffer de conversación.
    conver_buffer.append("You: " + user_input)
    
    # Combinar las consultas anteriores con la última para enviar a la API.
    prompt = "\n".join(conver_buffer)
    
    try:
        # Invocar la API de chatGPT con la consulta actual y el buffer completo.
        completion = openai.Completion.create(
            engine=MODEL_ENGINE,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            n=NMAX,
            top_p=TOP_P,
            frequency_penalty=FREQ_PENALTY,
            presence_penalty=PRES_PENALTY,
            temperature=TEMPERATURE,
            stop=["You:", "chatGPT:"] # Indicar la cadena de STOP para el modo de conversación.
        )
        
        # Agregar la respuesta al buffer de conversación.
        response = completion.choices[0].text.strip()
        conver_buffer.append("chatGPT: " + response)
        
        # Imprimir la respuesta de chatGPT.
        print_message(response, False)

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