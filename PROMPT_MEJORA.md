# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
import boto3
from aws_lambda_powertools import Logger, Tracer, Metrics
from src.models.transaction_model import Transaction

logger = Logger()
tracer = Tracer()
metrics = Metrics()

sqs = boto3.client('sqs')

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/123456789012/transaction-queue'


// === ARCHIVO: src/main.py ===
import os
from flask import Flask, request, jsonify
from src.handlers.transaction_handler import handle_transaction

app = Flask(__name__)

@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    transaction = handle_transaction(data)
    return jsonify(transaction.__dict__), 201

if __name__ == '__main__':
    app.run()


// === ARCHIVO: src/handlers/transaction_handler.py ===
from src.models.transaction_model import Transaction
from src.config.aws_config import sqs_client

@tracer.capture_method
def handle_transaction(data):
    logger.info('Handling transaction')
    transaction = Transaction(**data)
    send_to_sqs(transaction)
    return transaction

def send_to_sqs(transaction):
    response = sqs_client.send_message(
        QueueUrl=os.getenv('SQS_QUEUE_URL'),
        MessageBody=transaction.json()
    )
    logger.info(f'Message sent to SQS: {response}')


// === ARCHIVO: src/models/transaction_model.py ===
from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    amount: float
    currency: str
    status: str

    def json(self):
        return self.json()


// === ARCHIVO: config/aws_config.yaml ===
sqs_client:
    aws_access_key_id: YOUR_ACCESS_KEY_ID
    aws_secret_access_key: YOUR_SECRET_ACCESS_KEY
    region_name: us-east-1


// === ARCHIVO: scripts/deploy.sh ===
#!/bin/bash

# Deploy script for AWS Lambda

zip -r deployment.zip src/

aws lambda create-function --function-name transaction-service \
    --zip-file fileb://deployment.zip \
    --handler main.app \
    --runtime python3.12 \
    --role arn:aws:iam::123456789012:role/lambda-execution-role


// === ARCHIVO: tests/test_transaction_handler.py ===
import pytest
from src.handlers.transaction_handler import handle_transaction
from src.models.transaction_model import Transaction

def test_handle_transaction():
    data = {'id': '1', 'amount': 100.0, 'currency': 'USD', 'status': 'pending'}
    transaction = handle_transaction(data)
    assert isinstance(transaction, Transaction)
    assert transaction.id == '1'
    assert transaction.amount == 100.0
    assert transaction.currency == 'USD'
    assert transaction.status == 'pending'


// === ARCHIVO: config/sqs_config.yaml ===
SQS_QUEUE_URL: https://sqs.us-east-1.amazonaws.com/123456789012/transaction-queue


// === ARCHIVO: config/iam_policy.json ===
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:SendMessage",
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage"
      ],
      "Resource": "arn:aws:sqs:us-east-1:123456789012:transaction-queue"
    }
  ]
}

```
