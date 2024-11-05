# Delete Images

A simple Gradio-based interface for viewing and deleting images from a specified directory.
Designed for jupyter notebooks.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
import delete_images
```

In a jupyter notebook, specify the directory containing your images and create the Gradio interface:

```python
# Specify your image directory
directory_path = "/path/to/your/image_folder"

# Create and launch the interface
interface = delete_images.create_interface(directory_path)
interface.launch()
```

### How It Works

1. **Image Gallery**: The interface displays images in a gallery format. You can view and scroll through your images, which are organized in a grid.
2. **Delete Images**: Click on an image to delete it from the directory. A status message will confirm whether the image was successfully deleted.
3. **Refresh Gallery**: Use the "Refresh Gallery" button to reload the images and reflect any changes.


## Customization

- You can modify the `directory_path` to point to your desired folder containing images.
- The gallery is styled using custom CSS for 9:16 photos, when openedin a separate window.