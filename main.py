import gradio as gr

def greet():
    return f"Default"

demo = gr.Interface(
    fn= greet,
    inputs=[
        gr.Textbox(label="Descrivi la tua immagine(Usa l'inglese per risultati migliori)",
                   placeholder="Un calice di vino..."
                   ),
        ],
    outputs=[
        gr.Textbox(label="Questo è solo un test... ancora non genero immagini",
                   placeholder="Work in progress..."
            )
        ],
    
    title="Generatore di immagini",
    description="Generatore d'immagine ancora in lavorazione...",
    
    submit_btn="Genera",
    clear_btn="Cancella"
    )

demo.launch()