from PIL import Image


qr = Image.open('qr.png').convert("RGB")
original = Image.open('original.png').convert("RGBA")

for x in range(qr.height):
	for y in range(qr.width):
		a = qr.getpixel((x, y))
		
		if a == (0, 0, 0):
			b = list(original.getpixel((x, y)))
			b[3] = 250 # alpha

			original.putpixel((x, y), tuple(b))

original.save('babanov.png')