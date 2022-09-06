from funcs import *

escapePoint = complex(100000000000000000, 100000000000000000)

def mandelbrot(num, seed):
    if np.abs(num) > 18446744073709551615: return escapePoint
    if num == escapePoint: return escapePoint
    return num**2 + seed

width_resolution = 4000
height_resolution = 4000
width_offset = -1.1
height_offset = -1.1
width_span = 1
height_span = 1

max_iter = 255
    
inputNumbers = makeInputCanvas(width_resolution, height_resolution, width_offset, height_offset, width_span, height_span, complex)
outputImageBits = makeOutputCanvas(width_resolution, height_resolution, 'greyscale', complex)

for width_coord in range(width_resolution):
    for height_coord in range(height_resolution):
        inputNum = inputNumbers[width_coord, height_coord]
        results = checkEscape(inputNum, mandelbrot, max_iter, inputNum)
        if np.abs(results["finalNumber"]) < np.abs(escapePoint):
            outputImageBits[width_coord, height_coord] = 0
        else:
            try:
                outputImageBits[width_coord, height_coord] = 255 / max_iter * results["history"].index(escapePoint)
            except:
                outputImageBits[width_coord, height_coord] = 255
outputImageBits = outputImageBits.astype(int)

pil_image = Image.fromarray(outputImageBits)
pil_image = pil_image.convert('RGB').save("C:\\Github Stuffs\\ArtOfMathmateics\\mandelbrot.png")
#pil_image.show()