# Delete Images From a Folder via Gradio

A simple Gradio-based interface for viewing and deleting images from a specified directory.

Designed for jupyter notebooks.


![Alt text](delete_images/example_images/demo_screenshot.png)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Import the module

```python
import delete_images
```

Specify the directory containing your images

```python
interface = delete_images.create_interface("/path/to/image_folder")
```

Launch the Gradio interface

```python
interface.launch()
```

### How It Works

1. **Image Gallery**: The interface displays images in a gallery format. You can view and scroll through your images, which are organized in a grid.
2. **Delete Images**: Click on an image to delete it from the directory. A status message will confirm whether the image was successfully deleted.
3. **Refresh Gallery**: Use the "Refresh Gallery" button to reload the images and reflect any changes.


## Customization

- You can modify the `/path/to/image_folder` to point to your desired folder containing images.
- The gallery is styled using custom CSS for 9:16 photos, when it is opened in a separate window.