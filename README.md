# Cadena LLM Básica con LangChain y Google Gemini

## Introducción
Este proyecto lo desarrollé para entender de forma práctica cómo funciona una **LLM Chain** en LangChain conectada a un modelo real. La idea no era construir algo complejo, sino comprender bien el flujo básico:

- Cómo se inicializa un modelo de lenguaje (LLM).
- Cómo se estructura y envía un prompt usando plantillas.
- Cómo se recibe y procesa la respuesta del modelo.

Integré **Google Gemini (gemini-2.5-flash)** como proveedor del modelo, lo que me permitió ejecutar el proyecto sin costos gracias a su API gratuita. Me enfoqué en que el código fuera claro, bien comentado y que demostrara los conceptos fundamentales de LangChain: `ChatPromptTemplate`, `ChatGoogleGenerativeAI`, y `StrOutputParser`, encadenados con **LCEL (LangChain Expression Language)**.

## Arquitectura del Proyecto
El flujo del proyecto es el siguiente:

```
Usuario (prompt)
  → LangChain (ChatPromptTemplate)
    → Google Gemini (gemini-2.5-flash)
      → Generación de texto
        → StrOutputParser
          → Respuesta impresa en consola
```

Más detallado:

1. Se carga la API key de Google desde un archivo `.env`.
2. Se inicializa el modelo con `ChatGoogleGenerativeAI`.
3. Se crea una plantilla de prompt con instrucciones del sistema y la consulta del usuario.
4. Se construye la cadena usando el operador `|` de LCEL.
5. El modelo genera respuestas basadas en el input.
6. Se imprime el contenido generado en consola.

Este patrón es la base sobre la cual luego se pueden construir:
- Chains más complejas
- Agentes
- Sistemas RAG
- Pipelines con memoria

## Archivo Principal

**main.py**

```python
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente educativo experto..."),
        ("user", "{text}")
    ])

    parser = StrOutputParser()
    chain = prompt_template | model | parser

    respuesta = chain.invoke({
        "text": "Explica qué es LangChain y sus componentes principales."
    })
    print(respuesta)

if __name__ == "__main__":
    main()
```

## Requisitos
- Python 3.x
- `langchain`
- `langchain-google-genai`
- `python-dotenv`

Instalación:
```bash
pip install -r requirements.txt
```

## Variables de Entorno
Archivo `.env`:
```env
GOOGLE_API_KEY=tu-clave-de-google
```

## Cómo lo corrí en mi máquina (Windows)
1. Creé un entorno virtual:
   ```bash
   python -m venv .venv
   ```
2. Activé el entorno:
   ```bash
   .venv\Scripts\Activate.ps1
   ```
3. Instalé dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuté:
   ```bash
   py main.py
   ```
La respuesta se imprime directamente en consola.


## Conceptos Demostrados
- Inicialización de un LLM externo (Google Gemini) en LangChain.
- Uso de variables de entorno para credenciales.
- Creación de plantillas de prompt con `ChatPromptTemplate`.
- Flujo básico de invocación (`invoke`).
- Encadenamiento de componentes con **LCEL** (operador `|`).
- Uso de `StrOutputParser` para procesar la respuesta del modelo.
- Integración entre framework (LangChain) y proveedor externo (Google Gemini).

## Conclusión
- **Arquitectura**: Aunque es un ejemplo simple, muestra claramente la separación entre aplicación, framework y modelo.
- **Integración**: LangChain abstrae la complejidad del proveedor; cambiar de modelo solo requiere modificar parámetros.
- **Base para RAG**: Este flujo es exactamente el que luego se amplía al agregar un componente de recuperación (retriever + vector store).
- **Simplicidad**: Mantener el código pequeño permitió entender cada parte sin ocultar lógica detrás de librerías complejas.
- **Sin costos**: Usar Google Gemini permite ejecutar el proyecto sin necesidad de una suscripción de pago.
