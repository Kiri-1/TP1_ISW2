#Escriba un programa en lenguaje Python que basándose en el esqueleto
#previamente proporcionado acepte una consulta del usuario, verifique si
#la misma tiene texto, imprima su contenido, invoque el API de chatGPT
#con esa consulta e imprima en pantalla el resultado que se obtenga
#Ingeniería de Software II
#como respuesta. El contenido de la consulta debe agregársele “You:”
#antes de imprimirlo y de enviarlo. La respuesta de chatGPT deberá
#agregársele “chatGPT: “antes de imprimirse.
import openai

openai.api_key = "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"

while True:
    #Se llama prompt al carácter o conjunto de caracteres que se muestran en una línea de comandos para indicar que está a la espera de órdenes.
    prompt = input("\nIntroduce una pregunta: ")
    TOP_P=1
    FREQ_PENALTY=0
    PRES_PENALTY=0
    STOP=None
    MAX_TOKENS=1024
    TEMPERATURE=0.75
    NMAX=1
    MODEL_ENGINE = "text-davinci-003"

    #se detiene el programa cuando ingresa un exit al prompt
    if prompt == "exit" :
        break

    completion = openai.Completion.create(engine=MODEL_ENGINE,
                                          prompt=prompt,
                                          max_tokens=MAX_TOKENS,
                                          n=NMAX,
                                          top_p=TOP_P,
                                          frequency_penalty=FREQ_PENALTY,
                                          presence_penalty=PRES_PENALTY,
                                          temperature=TEMPERATURE,
                                          stop=STOP)
    print(completion.choices[0].text)