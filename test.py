from funcs import *
#print([1, 2].index(7))


iamge = Image.fromarray(np.zeros((100, 100)))
iamge = iamge.convert('RGB').save("C:\\Github Stuffs\\ArtOfMathmateics\\iamge.png")