import os
import gradio as gr

# get a list of image file paths
def get_image_paths(directory):
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    return sorted([os.path.join(directory, f) for f in image_files])

# handle image deletion
def delete_image(evt: gr.SelectData, directory):
    try:
        index = evt.index
        gallery_images = get_image_paths(directory)
        file_path = gallery_images[index]
        
        if os.path.exists(file_path):
            os.remove(file_path)
            new_images = get_image_paths(directory)
            return f"Deleted: {os.path.basename(file_path)}", new_images
        return "Error: Image not found!", gallery_images
    except Exception as e:
        return f"Error: {str(e)}", gallery_images

# create the Gradio interface
def create_interface(directory):
    # Custom CSS for styling the gallery images
    custom_css = """
    #gallery_container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px;
        padding: 20px;
    }
    #gallery img {
        object-fit: cover;
        aspect-ratio: 9 / 16;
        width: 150px;
        height: auto;
        border-radius: 8px;
        transition: transform 0.2s;
    }
    #gallery img:hover {
        transform: scale(1.05);
    }
    """
    
    with gr.Blocks(css=custom_css) as demo:
        gr.HTML("<h2>Click an image to delete it</h2>")
        
        # Status message
        status = gr.Textbox(label="Status", interactive=False)
        
        # Create a gallery for displaying images
        with gr.Column(elem_id="gallery_container"):
            gallery = gr.Gallery(
                value=get_image_paths(directory),
                columns=4,
                rows=2,
                height="auto",
                show_label=False,
                elem_id="gallery"
            )
        
        # Handle selection event
        gallery.select(
            lambda evt: delete_image(evt, directory),
            outputs=[status, gallery]
        )
        
        # Refresh button to reload the gallery
        refresh_btn = gr.Button("Refresh Gallery")
        refresh_btn.click(
            lambda: (None, get_image_paths(directory)),
            outputs=[status, gallery]
        )
    
    return demo

if __name__ == "__main__":
    # Specify directory path here:
    directory_path = "/content/my_folder_name"
    interface = create_interface(directory_path)
    interface.launch(share=True)