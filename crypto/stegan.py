from PIL import Image

# Encode text into an image with start and end markers
def encode(input_image_path, output_image_path, secret_text):
    start_marker = "#START#"
    end_marker = "#END#"
    secret_text = start_marker + secret_text + end_marker  # Add markers to the secret text

    image = Image.open(input_image_path)
    encoded_image = image.copy()

    # Convert secret_text to binary representation
    binary_secret_text = ''.join(format(ord(char), '08b') for char in secret_text)

    data_index = 0
    data_length = len(binary_secret_text)

    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))

            for color_channel_index in range(3):  # R, G, B channels
                if data_index < data_length:
                    pixel[color_channel_index] = pixel[color_channel_index] & ~1 | int(binary_secret_text[data_index])
                    data_index += 1

            encoded_image.putpixel((x, y), tuple(pixel))

    encoded_image.save(output_image_path)

# Decode and print the secret text using text markers
def decode(encoded_image_path):
    encoded_image = Image.open(encoded_image_path)
    binary_secret_text = ""

    for x in range(encoded_image.width):
        for y in range(encoded_image.height):
            pixel = list(encoded_image.getpixel((x, y)))

            for color_channel_index in range(3):  # R, G, B channels
                binary_secret_text += str(pixel[color_channel_index] & 1)

    binary_secret_text = ''.join([chr(int(binary_secret_text[i:i + 8], 2)) for i in range(0, len(binary_secret_text), 8)])

    start_marker = "#START#"
    end_marker = "#END#"

    start_index = binary_secret_text.find(start_marker)
    end_index = binary_secret_text.find(end_marker)

    if start_index != -1 and end_index != -1:
        secret_text = binary_secret_text[start_index + len(start_marker):end_index]
        return secret_text
    else:
        return "No secret text found in the image"

