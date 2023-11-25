"""Utility methods relating to image conversion."""
import base64
import io
import PIL
from PIL.Image import Image


def pil_to_ascii(image: Image) -> str:
    """Serialize PIL Image to ascii.

    Example::

          import PIL
          from curator.utils import pil_to_ascii, ascii_to_pil

          image = PIL.Image.open('tests/resources/hopper.png')
          ascii_image = pil_to_ascii(image)
          decoded_image = ascii_to_pil(ascii_image)
    """
    imageio = io.BytesIO()
    image.save(imageio, 'png')
    bytes_image = base64.b64encode(imageio.getvalue())
    ascii_image = bytes_image.decode('ascii')
    return ascii_image


def ascii_to_pil(ascii_image: str) -> Image:
    """Convert ascii image to PIL Image.

    Example::

          import PIL
          from curator.utils import pil_to_ascii, ascii_to_pil

          image = PIL.Image.open('tests/resources/hopper.png')
          ascii_image = pil_to_ascii(image)
          decoded_image = ascii_to_pil(ascii_image)
    """
    return PIL.Image.open(io.BytesIO(base64.b64decode(ascii_image)))


def pil_to_bytes(image: Image) -> bytes:
    """Serialize PIL Image into io.BytesIO stream.

    Example::

          import PIL
          from curator.utils import pil_to_bytes, bytes_to_pil

          image = PIL.Image.open('tests/resources/hopper.png')
          bytes_image = pil_to_bytes(image)
          decoded_image = bytes_to_pil(ascii_image)
    """
    imageio = io.BytesIO()
    image.save(imageio, 'png')
    image_stream = imageio.getvalue()
    return image_stream


def bytes_to_pil(bytes_image: bytes) -> Image:
    """Convert io.BytesIO stream to PIL Image.

    Example::

          import PIL
          from curator.utils import pil_to_bytes, bytes_to_pil

          image = PIL.Image.open('tests/resources/hopper.png')
          bytes_image = pil_to_bytes(image)
          decoded_image = bytes_to_pil(ascii_image)
    """
    return PIL.Image.open(io.BytesIO(bytes_image))
