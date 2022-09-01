from reportlab.pdfgen import canvas
from config import *
from superheroe import Superheroe
import os
from utils import download_image
from reportlab.lib.units import cm # type: ignore

# Declare type of cm
cm: float = cm

# Canvas configuration
A4_HEIGHT = 29.7 * cm
TOP_MARGIN = 0.5 * cm
LEFT_MARGIN = 1 * cm
IMAGE_HEIGHT = 1.75 * cm
TEXT_HEIGHT = 11
FIELD_LEFT_PADDING = 0.1 * cm
FONT_NAME = 'Helvetica'
FONT_SIZE = 12
LINE_WIDTH = .3

class MyCanvas(canvas.Canvas):
    def __init__(self, filename: str):
        super().__init__(filename=filename) # type: ignore

        # This cursor will be moved every time something is ploted in the canvas
        self.y_cursor = A4_HEIGHT - TOP_MARGIN
    
    def set_default_font_and_font_size(self):
        self.setLineWidth(LINE_WIDTH)       # type: ignore
        self.setFont(FONT_NAME, FONT_SIZE)  # type: ignore
    
    def plot_occupation_title(self, title: str):
        # Capitalize title
        title = title.capitalize()

        # Draw title
        self.y_cursor -= TEXT_HEIGHT * 2
        self.drawString(x=LEFT_MARGIN, y=self.y_cursor, text=title) # type: ignore
        self.y_cursor -= TEXT_HEIGHT
    
    def plot_superheroe(self, superheroe: Superheroe):
        # Create directory if does not exist
        os.makedirs('./cache', exist_ok=True)

        # Define image path of current superheroe image
        image_path = f'./cache/{superheroe.id}.{IMAGE_EXTENSION}'

        # Download file if it does not exist
        if not os.path.exists(image_path):
            # Download superhero image
            download_image(superheroe.image_url, image_path)

        # Assert
        assert os.path.exists(image_path)

        # Draw the superhero image
        self.y_cursor -= IMAGE_HEIGHT
        self.drawImage(image_path, LEFT_MARGIN, y=self.y_cursor, width=IMAGE_HEIGHT, height=IMAGE_HEIGHT) # type: ignore
        
        # Remove image from local
        if not CACHE_IMAGES:
            os.remove(image_path)

        # Draw every field
        sub_y_cursor = self.y_cursor + IMAGE_HEIGHT
        for field in [
            superheroe.full_name,
            superheroe.alter_egos,
            ', '.join(superheroe.aliases),
            superheroe.place_of_birth,
        ]:
            sub_y_cursor -= TEXT_HEIGHT
            self.drawString(x=LEFT_MARGIN + IMAGE_HEIGHT + FIELD_LEFT_PADDING, y=sub_y_cursor, text=field) # type: ignore

    def show_page_and_save(self):
        self.showPage() # type: ignore
        self.save()     # type: ignore
