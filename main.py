import gradio as gr
from model import generator

try:
    def generate_image(prompt):
        if not prompt.strip():
            return None
        
        image = generator.generate(prompt)
        return image

    demo = gr.Interface(
        fn=generate_image,
        inputs=[
            gr.Textbox(
                label="Descrivi la tua immagine (Usa l'inglese per risultati migliori)",
                placeholder="A wine glass on a wooden table...",
                lines=3
            ),
        ],
        outputs=[
            gr.Image(label="Immagine generata", type="pil")
        ],
        
        title="🎨 Generatore di immagini con Flux Schnell",
        description="Genera immagini usando Flux Schnell. Il primo utilizzo potrebbe richiedere qualche minuto per caricare il modello.",
        
        submit_btn="Genera",
        clear_btn="Cancella"
    )

    demo.launch()

except Exception as e:
    print(f"Error: {e}")

