import qrcode
from io import BytesIO
import qrcode.image.svg
def qr_generator_image(URL):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

    # Add data to the QRCode
    qr.add_data(URL)
    qr.make(fit=True)

    # Create an image object
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to bytes
    img_byte_array = BytesIO()
    img.save(img_byte_array, format="PNG")
    img_bytes = img_byte_array.getvalue()
    return img_bytes
def qr_generator_vector(URL):
    factory = qrcode.image.svg.SvgPathImage
    svg_img = qrcode.make(URL, image_factory=factory)
    return svg_img

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def generate_qr(URL:str, fill_color:tuple, back_color:tuple, box_size:int, border:int, filename:str):
    import qrcode
    import io
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Convert the image to bytes
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format="PNG")
    img_bytes = img_byte_array.getvalue()
    
    return img_bytes
