from PIL import ImageFilter, Image, ImageEnhance

with Image.open("original.jpg") as photo:
    print(photo.size)
    print(photo.format)
    print(photo.mode)
    #photo.show()
    photo_left_90 = photo.transpose(Image.ROTATE_90)
    photo_left_90.save("original_left_90.jpg")
    photo_left_270 = photo.transpose(Image.ROTATE_270)
    photo_left_270.save("original_left_270.jpg")
    photo_left_flip = photo.transpose(Image.FLIP_LEFT_RIGHT)
    photo_left_flip.save("original_left_flip.jpg")
    photo_blur = photo.filter(ImageFilter.BLUR)
    photo_blur.save("original_blur.jpg")
    photo_blur_box = photo.filter(ImageFilter.BoxBlur(10))
    photo_blur_box.save("original_box_blur.jpg")
    photo_blur_gaus = photo.filter(ImageFilter.GaussianBlur(10))
    photo_blur_gaus.save("original_blur_gaus.jpg")
    photo_BW = photo.convert("L")
    photo_BW.save("original_BW.jpg")
    photo_crop = photo.crop((0,0,500,500))
    photo_crop.save("original_crop.jpg")
    photo_rotate = photo.rotate(60)
    photo_rotate.save("original_rotate.jpg")
    photo_size = photo.resize((4800,3200))
    photo_size.save("original_size.jpg")



