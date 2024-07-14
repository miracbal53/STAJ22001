import os

# Klasörün tanımlanması
imgv2_dir = '/content/drive/MyDrive/mamografai/InBreast/INbreast Release 1.0/imgv2'

# .png uzantılı dosyaların listelenmesi ve isimlerinin ilk 8 hanesinin okunması
def read_first_8_characters(directory):
    png_files = [f for f in os.listdir(directory) if f.endswith('.png')]

    for filename in png_files:
        first_8_characters = filename[:8]
        print(f"Dosya adı: {filename}, İlk 8 hane: {first_8_characters}")

# İşlevin çağrılması
read_first_8_characters(imgv2_dir)
