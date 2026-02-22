# Laboratorio de Cadena LLM con LangChain

Este repositorio contiene el código y la documentación para el tutorial básico de la cadena LLM de LangChain, parte del laboratorio "Introducción a la Creación de RAGs (Generadores Aumentados por Recuperación) con OpenAI".

## Arquitectura del Proyecto

Este proyecto simple demuestra los componentes fundamentales de LangChain:
1.  **ChatOpenAI**: Un envoltorio para un Modelo de Lenguaje Grande (LLM) que permite la interacción programática con los modelos de OpenAI (específicamente `gpt-3.5-turbo`).
2.  **ChatPromptTemplate**: Una plantilla de prompt genérica utilizada para estructurar las entradas para el LLM. Ayuda a manejar el contexto y las variables (como instrucciones específicas y entradas del usuario).
3.  **StrOutputParser**: Un analizador que extrae automáticamente el contenido de texto de los objetos de respuesta estructurados devueltos por ChatOpenAI.
4.  **LCEL (LangChain Expression Language)**: El mecanismo de tubería (`|`) para conectar prompts, modelos y analizadores en cadenas.

## Requisitos Previos
* Python 3.8+
* Una clave API de OpenAI activa.

## Instrucciones de Instalación

1.  **Abre el directorio**: Asegúrate de estar en el directorio raíz de este repositorio (donde se encuentran este `README.md` y `requirements.txt`).
2.  **Crear un entorno virtual (opcional pero recomendado)**:
    ```bash
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```
3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configurar la clave de API**:
    Crea un archivo llamado `.env` en la raíz del directorio y añade tu clave API de OpenAI de esta manera:
    ```env
    OPENAI_API_KEY="tu-clave-sk-...."
    ```

## Cómo Ejecutar

Ejecuta el script principal:
```bash
python main.py
```

## Ejemplo de Salida
```
--- Tutorial Básico de Cadena LLM con LangChain ---

[1] Inicializando ChatOpenAI...
[2] Creando Plantilla de Prompt...
[3] Creando Analizador de Salida...
[4] Construyendo la Cadena (Prompt -> Modelo -> Analizador)...

--- Invocando la Cadena ---
Entrada: '¡Hola! ¿Cómo estás hoy?' (Traduciendo de Español a Inglés)

[Resultado]:
Hello! How are you today?
```
