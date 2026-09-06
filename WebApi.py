from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
# IMPORTA ESTO:
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from docx import Document
import io

app = FastAPI(title="Procesador de Calidad de Energía")

# CONFIGURA ESTO:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción puedes cambiar "*" por la URL exacta de tu React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analizar-historico")
async def analizar_historico(archivo: UploadFile = File(...)):
    contenido = await archivo.read()
    df = pd.read_csv(io.BytesIO(contenido))

    voltaje_prom = df['voltaje'].mean() if 'voltaje' in df.columns else 0
    corriente_max = df['corriente'].max() if 'corriente' in df.columns else 0
    total_registros = len(df)

    doc = Document()
    doc.add_heading('Reporte Eléctrico de Calidad de Energía', level=0)
    doc.add_heading('1. Resumen de Mediciones Históricas', level=1)
    doc.add_paragraph(f"Se han analizado exitosamente un total de {total_registros} muestras.")
    doc.add_paragraph(f"Voltaje Promedio Registrado: {voltaje_prom:.2f} V")
    doc.add_paragraph(f"Corriente Máxima Registrada: {corriente_max:.2f} A")

    buffer_word = io.BytesIO()
    doc.save(buffer_word)
    buffer_word.seek(0)

    headers = {
        'Content-Disposition': f'attachment; filename="Reporte_{archivo.filename}.docx"'
    }

    return StreamingResponse(
        buffer_word,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers=headers
    )
