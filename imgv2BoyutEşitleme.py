from PIL import Image
import os

# Klasörlerin tanımlanması
imgv2_dir = '/content/drive/MyDrive/mamografai/InBreast/INbreast Release 1.0/imgv2'
outputmask8_dir = '/content/drive/MyDrive/mamografai/InBreast/boyut1'
output_dir = '/content/drive/MyDrive/mamografai/InBreast/INbreast Release 1.0/boyut2'

# .png uzantılı dosyaların listelenmesi
imgv2_files = [f for f in os.listdir(imgv2_dir) if f.endswith('.png')]
outputmask8_files = [f for f in os.listdir(outputmask8_dir) if f.endswith('.png')]

# Ortak dosya isimlerinin bulunması
common_files = set(imgv2_files).intersection(outputmask8_files)

# Output klasörünün oluşturulması
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Her ortak dosya için boyutların eşitlenip kaydedilmesi
for filename in common_files:
    img_path = os.path.join(imgv2_dir, filename)
    mask_path = os.path.join(outputmask8_dir, filename)

    # Resimlerin açılması
    img = Image.open(img_path)
    mask = Image.open(mask_path)

    # Maskenin boyutlarına göre görüntünün boyutlandırılması
    img_resized = img.resize(mask.size, Image.ANTIALIAS)

    # Yeni dosya yolunun oluşturulması ve kaydedilmesi
    output_path_img = os.path.join(output_dir, filename)
    img_resized.save(output_path_img)

    print(f"Eşitlenen ve kaydedilen dosya: {output_path_img}")

print("İşlem tamamlandı.")
