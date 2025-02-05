from PIL import Image

img= "coffee\img\imgfundo.jpeg"

def zoom_image(image_path, output_path, zoom_factor):
    img = Image.open(image_path)

    # Calcular nova largura e altura
    width, height = img.size
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)

    # Centralizar o zoom
    left = (width - new_width) // 2
    top = (height - new_height) // 2

    img = img.crop((left, top, left + new_width, top + new_height)).resize((width, height), Image.LANCZOS)
    
    img.save(output_path)

#zoom_image(img, "coffee\img\imgEdit2.jpg", 1)



def resize_image(image_path, output_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height), Image.LANCZOS)
    
    img.save(output_path)

resize_image(img, "coffee\img\imgEdit4.jpg", 785, 1311)

