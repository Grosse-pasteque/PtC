from PIL import Image
import numpy

image = 'image.png'
rgb = {
    'red': {
        51: '.',
        102: '-',
        153: ':',
        204: '+',
        255: '%'
    },
    'green': {
        51: '.',
        102: '-',
        153: ':',
        204: '+',
        255: '%'
    },
    'blue': {
        51: '.',
        102: '-',
        153: ':',
        204: '+',
        255: '%'
    },
    'equals-special': {
        51: '.',
        102: '-',
        153: ':',
        204: '+',
        255: '%'
    }
}

def convert(image):
    image = Image.open(image)
    return numpy.array(image, dtype=numpy.uint8)

def transform(image_list, rgb):
    image_new = []
    for l, line in enumerate(image_list):
        image_new.append([])
        for pixels in line:
            if pixels[1] < pixels[0] > pixels[2]:
                diff = lambda l: abs(l-pixels[0])
                closest = min(list(rgb['red'].keys()), key=diff)
                image_new[l].append(rgb['red'][closest]*2)
            elif pixels[0] < pixels[1] > pixels[2]:
                diff = lambda l: abs(l-pixels[1])
                closest = min(list(rgb['green'].keys()), key=diff)
                image_new[l].append(rgb['green'][closest]*2)
            elif pixels[0] < pixels[2] > pixels[1]:
                diff = lambda l: abs(l-pixels[2])
                closest = min(list(rgb['blue'].keys()), key=diff)
                image_new[l].append(rgb['blue'][closest]*2)
            
            else:  # all equals
                diff = lambda l: abs(l-pixels[0])
                closest = min(list(rgb['equals-special'].keys()), key=diff)
                image_new[l].append(rgb['equals-special'][closest]*2)
    return image_new

def show(l):
    nl = ""
    for ligne in l:
        for pixel in ligne:
            nl += pixel
        nl += '\n'
    return nl

def write_file(image, file):
    with open(file, 'w') as f:
        f.write(image)
        f.close()

image = convert(image)
image = transform(image, rgb)
image = show(image)
write_file(image, 'image.txt')