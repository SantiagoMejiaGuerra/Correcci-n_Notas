from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel
from groq import Groq
import logging

#Inicializamos el cliente con Groq
"""
Aqui te dejo un video explicativo de como adquirir tu API KEY en GROQ

https://www.youtube.com/watch?v=J8JkqTrNDjA&t=435s
"""
client= Groq(api_key="Aqui_va_tu_API_KEY")

# Creamos la app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes, ajusta si es necesario
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Modelo de entrada y salida
class NoteRequest(BaseModel):
    text: str

class NoteResponse(BaseModel):
    corrected_text: str
    original_text: str

def get_ai_response(messages):
    try:
        completion =client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
            stream=False,
        )
        
        if completion.choices and hasattr(completion.choices[0], "message"):
            response = completion.choices[0].message.content.strip()
            
            # # Busca el texto entre comillas dobles
            # match = re.search(r'"(.*?)"', response) # Busca el contenido entre comillas
            # return match.group(1) #Devuelve el texto corregido
            if response:
                return response
            else:
                raise ValueError("Respuesta vacía o no válida.")
            
        else:
            raise ValueError("No se encontró 'message.content' en la respuesta de la API.")
        
    except Exception as e:
        raise ValueError(f"Error procesando la respuesta de la API: {str(e)}")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("API_Connection")

# Endpoint para analizar y corregir las notas
@app.post ("/analyze-note", response_model=NoteResponse)
async def analyze_note(request: NoteRequest):
    try:
        #Mensajes iniciales
        messages = [
            {"role": "system", "content": (
                "Eres un experto en corrección de notas médicas. Corrige ortografía, gramática y asegura que las palabras médicas sean precisas. "
                "Además, indica la lateralidad del cuerpo humano con MAYUSCULA  (por ejemplo: brazo IZQUIERDO o pierna DERECHA) cuando sea necesario. Si no se especifica el género del paciente en el texto, "
                "indícalo con una nota en MAYUSCULA: [ESPECIFICAR GÉNERO: MASCULINO/FEMENINO]. Dame la respuesta siempre en español"
            )},
            {"role": "user", "content": request.text},
        ]
        
        logger.info("Enviando solicitud a la API con mensajes: %s", messages)
        #obtener respuesta de la IA
        corrected_text= get_ai_response(messages)
        
        
        # Devuelve la respuesta corregida
        return NoteResponse(
            original_text=request.text,
            corrected_text=corrected_text
        )
    except HTTPException as http_err:
        logger.error("Error HTTP: %s", str(http_err))
        raise http_err
    except Exception as e:
        logger.error(f"Error interno: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error procesando la nota:{str(e)}")