import os
from dotenv import load_dotenv

# Proporciona una clave API localmente si no usas .env, de lo contrario usa dotenv
# import getpass
# os.environ["OPENAI_API_KEY"] = getpass.getpass("Ingresa tu clave de API de OpenAI: ")
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    print("--- Tutorial Básico de Cadena LLM con LangChain ---")
    
    # 1. Inicializar el LLM (Modelo de Lenguaje Grande)
    # Usa gpt-3.5-turbo por defecto. Requiere OPENAI_API_KEY en el entorno.
    print("\n[1] Inicializando ChatOpenAI...")
    try:
        model = ChatOpenAI(model="gpt-3.5-turbo")
    except Exception as e:
         print(f"Error al inicializar el modelo: {e}")
         print("Por favor, asegúrate de que tu OPENAI_API_KEY esté configurada en un archivo .env o variable de entorno.")
         return

    # 2. Crear una Plantilla de Prompt (Prompt Template)
    # Esto ayuda a formatear la entrada del usuario en un formato que el modelo espera.
    print("[2] Creando Plantilla de Prompt...")
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente útil que traduce del {input_language} al {output_language}."),
        ("user", "{text}")
    ])

    # 3. Crear un Analizador de Salida (Output Parser)
    # Esto analiza la compleja respuesta del modelo en una cadena de texto estándar.
    print("[3] Creando Analizador de Salida...")
    parser = StrOutputParser()

    # 4. Encadenarlos juntos usando LCEL (LangChain Expression Language)
    print("[4] Construyendo la Cadena (Prompt -> Modelo -> Analizador)...")
    chain = prompt_template | model | parser

    # 5. Invocar la cadena
    input_text = "¡Hola! ¿Cómo estás hoy?"
    input_lang = "Español"
    output_lang = "Inglés"
    
    print(f"\n--- Invocando la Cadena ---")
    print(f"Entrada: '{input_text}' (Traduciendo de {input_lang} a {output_lang})")
    
    try:
        # Pasamos un diccionario que contiene las variables esperadas por la plantilla
        response = chain.invoke({
            "input_language": input_lang,
            "output_language": output_lang,
            "text": input_text
        })
        print("\n[Resultado]:")
        print(response)
    except Exception as e:
        print(f"\nOcurrió un error durante la invocación de la cadena: {e}")
        print("Por favor verifica tu clave de API de OpenAI y tu conexión a internet.")

if __name__ == "__main__":
    main()
