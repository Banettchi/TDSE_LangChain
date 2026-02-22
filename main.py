import os
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    print("=" * 70)
    print("  TUTORIAL BÁSICO DE CADENA LLM CON LANGCHAIN Y GEMINI")
    print("=" * 70)
    
    # 1. Inicializar el LLM (Modelo de Lenguaje Grande)
    print("\n[1] Inicializando Gemini (modelo: gemini-2.5-flash)...")
    try:
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    except Exception as e:
        print(f"Error al inicializar el modelo: {e}")
        print("Asegúrate de que tu GOOGLE_API_KEY esté configurada en el archivo .env")
        return

    # 2. Crear una Plantilla de Prompt (Prompt Template)
    print("[2] Creando Plantilla de Prompt...")
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente educativo experto. Responde siempre en español de forma detallada y clara, usando formato con negritas (**texto**) y listas numeradas para organizar tu respuesta."),
        ("user", "{text}")
    ])

    # 3. Crear un Analizador de Salida (Output Parser)
    print("[3] Creando Analizador de Salida (StrOutputParser)...")
    parser = StrOutputParser()

    # 4. Encadenarlos juntos usando LCEL (LangChain Expression Language)
    print("[4] Construyendo la Cadena (Prompt -> Modelo -> Analizador)...\n")
    chain = prompt_template | model | parser

    # =====================================================
    # PRIMERA CONSULTA: Explicar qué es LangChain
    # =====================================================
    print("=" * 70)
    print("  CONSULTA 1: ¿Qué es LangChain?")
    print("=" * 70)

    try:
        respuesta1 = chain.invoke({
            "text": "Explica qué es LangChain, cuáles son sus componentes principales (LLMs, Prompts, Chains, Agents, Memory), para qué se usa y cuáles son sus ventajas. Sé detallado."
        })
        print(respuesta1)
    except Exception as e:
        print(f"Error: {e}")
        return

    # =====================================================
    # SEGUNDA CONSULTA: Traducción como ejemplo práctico
    # =====================================================
    print("\n" + "=" * 70)
    print("  CONSULTA 2: Ejemplo práctico - Traducción")
    print("=" * 70)

    prompt_traduccion = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente útil que traduce del {input_language} al {output_language}. Responde únicamente con la traducción."),
        ("user", "{text}")
    ])
    
    chain_traduccion = prompt_traduccion | model | parser

    texto_original = "La inteligencia artificial está transformando la manera en que interactuamos con la tecnología."
    print(f"\nTexto original (Español): {texto_original}\n")
    
    try:
        traduccion = chain_traduccion.invoke({
            "input_language": "Español",
            "output_language": "Inglés",
            "text": texto_original
        })
        print(f"Traducción (Inglés): {traduccion}")
    except Exception as e:
        print(f"Error: {e}")
        return

    # =====================================================
    # TERCERA CONSULTA: Resumen de conceptos clave
    # =====================================================
    print("\n" + "=" * 70)
    print("  CONSULTA 3: Conceptos clave de los Modelos de Lenguaje (LLMs)")
    print("=" * 70)

    try:
        respuesta3 = chain.invoke({
            "text": "Explica los conceptos clave de los Modelos de Lenguaje Grande (LLMs): qué son, cómo funcionan, qué es un token, qué es el temperature, y qué es un prompt. Incluye ejemplos prácticos."
        })
        print(respuesta3)
    except Exception as e:
        print(f"Error: {e}")

    print("\n" + "=" * 70)
    print("  FIN DEL TUTORIAL BÁSICO DE LANGCHAIN")
    print("=" * 70)

if __name__ == "__main__":
    main()
