import openai

# Clave de API de OpenAI para usar GPT-4 con visión
import os
openai.api_key = os.environ["OPENAI_API_KEY"]


# Función que genera el contenido emocional para redes sociales
def generar_contenido_emocional():
    response = openai.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in emotional and viral content for a gift shop called Pasha Love."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Look at the image and create a short emotional or funny caption in English. Then provide a Spanish translation. Add relevant hashtags in both languages."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://cdn.shopify.com/s/files/1/0661/9630/7113/files/llavero-bubble-azul-pashalove.jpg"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )

    # Mostrar en consola el resultado generado por la IA
    print("\n✅ Resultado generado por la IA:\n")
    print(response.choices[0].message.content)

# Ejecutar la función
generar_contenido_emocional()


