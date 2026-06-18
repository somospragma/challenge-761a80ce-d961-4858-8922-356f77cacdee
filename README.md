# Implementación de un microservicio serverless

El equipo de desarrollo de una empresa de fintech necesita implementar un microservicio serverless para procesar transacciones financieras. El sistema debe manejar la recepción de solicitudes, el procesamiento de las mismas y el envío de respuestas. Además, debe integrarse con un sistema de colas de mensajes para garantizar la fiabilidad y el orden de las transacciones. Este microservicio será expuesto a través de una API y deberá ser escalable y resistente a fallos.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Fundamentos de servicios cloud |
| **Nivel** | junior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 3-4 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del microservicio

**Objetivo:** Definir las funcionalidades y los requisitos del microservicio.

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Identifica las operaciones que el microservicio debe soportar.
- Define los requisitos de entrada y salida para cada operación.
- Considera los posibles estados y transiciones del microservicio.

**Entregable:** Documento de requerimientos del microservicio.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en términos de operaciones que el microservicio debe realizar.
- Considera cómo el microservicio interactuará con otros sistemas.

</details>

### Fase 2: Diseño del flujo de mensajes

**Objetivo:** Diseñar el flujo de mensajes entre el microservicio y el sistema de colas.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Define cómo se enviarán los mensajes al sistema de colas.
- Establece las reglas para el procesamiento de los mensajes en la cola.
- Considera los posibles fallos y cómo manejarlos.

**Entregable:** Diagrama del flujo de mensajes y reglas de procesamiento.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo garantizar la fiabilidad y el orden de los mensajes.
- Considera cómo manejar los fallos en el sistema de colas.

</details>

### Fase 3: Implementación y pruebas

**Objetivo:** Implementar el microservicio y realizar pruebas unitarias y de integración.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Implementa las operaciones definidas en la fase 1.
- Integra el microservicio con el sistema de colas.
- Realiza pruebas unitarias y de integración para validar el funcionamiento del microservicio.

**Entregable:** Código del microservicio y reporte de pruebas.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza un enfoque de prueba temprana para identificar problemas rápidamente.
- Considera diferentes escenarios de prueba para cubrir todos los casos de uso.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un microservicio serverless y por qué se utiliza en este caso?
- **paraQueSirve**: ¿Para qué sirve integrar el microservicio con un sistema de colas de mensajes?
- **comoSeUsa**: ¿Cómo se diseña el flujo de mensajes entre el microservicio y el sistema de colas?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar un microservicio serverless y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica la implementación de un microservicio serverless y cómo afectan al diseño del sistema?

## Criterios de Evaluacion

- Definición clara de las funcionalidades y requisitos del microservicio.
- Diseño del flujo de mensajes y reglas de procesamiento.
- Implementación y pruebas del microservicio.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
