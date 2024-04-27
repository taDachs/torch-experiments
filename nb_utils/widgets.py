import ipywidgets as widgets
from PIL import Image
import time
import io

class ArrayRenderWidget(widgets.Image):
    def render(self, frame):
        img = Image.fromarray(frame, 'RGB')
        with io.BytesIO() as buf:
            img.save(buf, format='PNG')
            image_data = buf.getvalue()
        self.value = image_data
image_widget = ArrayRenderWidget(
    format='png',
    width=600,
    height=400,
)