def generate_qr(URL:str,fill_color:tuple,back_color:tuple,box_size:int,border:int,filename:str):
    import qrcode
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
    qr.add_data(URL)
    qr.make(fit=True)
    # (fill_color="black) , (back_color="white")
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img