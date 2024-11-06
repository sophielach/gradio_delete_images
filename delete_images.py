import os
import gradio as gr

def get_image_paths(directory):
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    return sorted([os.path.join(directory, f) for f in image_files])

def delete_image(evt: gr.SelectData, directory):
    try:
        gallery_images = get_image_paths(directory)
        index = evt.index
        
        if 0 <= index < len(gallery_images):
            file_path = gallery_images[index]
            if os.path.exists(file_path):
                os.remove(file_path)
                return {
                    status: f"Deleted: {os.path.basename(file_path)}",
                    gallery: get_image_paths(directory),
                }
            return {
                status: "Error: File not found",
                gallery: gallery_images,
            }
        return {
            status: "Error: Invalid image index",
            gallery: gallery_images,
        }
    except Exception as e:
        return {
            status: f"Error: {str(e)}",
            gallery: get_image_paths(directory),
        }

def create_interface(directory):
    custom_css = """
    #gallery_container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px;
        padding: 20px;
    }
    #gallery {
        min-height: 300px;
    }
    .gallery-item {
        object-fit: cover;
        aspect-ratio: 9 / 16;
        width: 150px;
        height: auto;
        border-radius: 8px;
        transition: transform 0.2s;
    }
    .gallery-item:hover {
        transform: scale(1.05);
        cursor: pointer;
    }
    """

    with gr.Blocks(css=custom_css) as demo:
        gr.HTML("<h2>Click on an image to delete it</h2>")
        
        with gr.Column():
            status = gr.Textbox(label="Status", interactive=False)
            
            with gr.Column(elem_id="gallery_container"):
                gallery = gr.Gallery(
                    value=get_image_paths(directory),
                    columns=4,
                    rows=None,
                    height="auto",
                    show_label=False,
                    elem_id="gallery",
                    allow_preview=False,
                    preview=False
                )

            refresh_btn = gr.Button("Refresh Gallery")

        gallery.select(
            fn=lambda evt: delete_image(evt, directory),
            inputs=None,
            outputs=[status, gallery]
        )

        refresh_btn.click(
            fn=lambda: {
                status: "Gallery refreshed",
                gallery: get_image_paths(directory)
            },
            outputs=[status, gallery]
        )

    return demo

if __name__ == "__main__":
    # Specify directory path here:
    directory_path = "example_images"
    interface = create_interface(directory_path)
    interface.launch(share=True)
