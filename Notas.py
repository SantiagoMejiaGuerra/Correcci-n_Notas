from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel
from groq import Groq
import re

#Inicializamos el cliente con Groq
"""
Aqui te dejo un video explicativo de como adquirir tu API KEY en GROQ

https://www.youtube.com/watch?v=J8JkqTrNDjA&t=435s
"""
client= Groq(api_key="aqui_va_tu_API_Key_de_groq")

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
    completion =client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        temperature=0.9,
        max_tokens=1024,
        stream=False,
    )
    
    try:
        if completion.choices and hasattr(completion.choices[0], "message"):
            response = completion.choices[0].message.content.strip()
            
            # Busca el texto entre comillas dobles
            match = re.search(r'"(.*?)"', response) # Busca el contenido entre comillas
            if match:
                return match.group(1) #Devuelve el texto corregido
            else:
                raise ValueError("No se encontró texto corregido en el formato esperado.")
            
        else:
            raise ValueError("No se encontró 'message.content' en la respuesta de la API.")
    except Exception as e:
        raise ValueError(f"Error procesando la respuesta de la API: {str(e)}")

# Endpoint para analizar y corregir las notas
@app.post ("/analyze-note", response_model=NoteResponse)
async def analyze_note(request: NoteRequest):
    try:
        #Mensajes iniciales
        messages = [
            {"role": "system", "content":"Eres un asistente que corrige gramatica y ortografia de las notas médicas."},
            {"role": "user", "content": request.text},
        ]
        
        #obtener respuesta de la IA
        corrected_text= get_ai_response(messages)
        
        # Devuelve la respuesta corregida
        return NoteResponse(
            original_text=request.text,
            corrected_text=corrected_text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando la nota:{str(e)}")