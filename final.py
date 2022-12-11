import re
import random
from respuestas import preguntas, respuestas

start = True;


#Definimos el mensaje que el usuario va a introducir.
def get_response(user_input):

    #Omitimos lo caracteres especiales y convertimos en minusculas las palabras.
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())

    #Revisamos todos los mensajes que va a tener y va a resivir el mensaje como entrada
    response = check_all_messages(split_message)
    return response


#Definimos la probabilidad de mensajes que va a introduccir el usuario.
def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True


    #iteramos cada palabra del mensaje y validamos si estas estan en la palabra reconocidas
    for word in recognized_words:
        if word in user_message:
            message_certainty += 1


    #Una variable que va a almacenar el mensaje que insertamos para ver si es el mas adecuado.
    percentage = float(message_certainty) / float(len(recognized_words))


    #Iteramos las palabras requeridas y validamos si las palabras no estan en el mensaje y si es asi le decimos que no cumple y terminamos el bucle.
    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break


    #De lo contrario si tiene la palabra requerida o es una respuesta simple  va a mostrar la que mayor porcentuaje tiene o si no e asi retorna 0.
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0



#Aqui creamos una funcion para revisar todos los mensajes
def check_all_messages(message):
        highest_prob = {}

        #Definimos las respuestas
        def response(list_of_words, bot_response, single_response=False, required_words=[]):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        #Aqui va a tomar las preguntas y respuestas de la otra pag
        for p, r in zip(preguntas, respuestas):
            response(p, r, single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)


#Definimos una funcion desconocido para las respuestas que sean menor que 1 y devolvemos la que mejor encaja
        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():

    #Aqui colocamos un mensaje de cuando el bot no entienda lo que el usuario le esta preguntando
    response=['Lo siento pero no tengo suficiente capacidad para poder responderte'][random.randrange(3)]
    return response



#Hacemos un bucle para que siempre este preguntando al usuario.
while start:
    response = get_response(input('Tu: '));
    print("Priscilio: " + response)
    if(response == 'Fue un placer ayudarle'):
        start = False;
        input('Presiona cualquier tecla para salir')
