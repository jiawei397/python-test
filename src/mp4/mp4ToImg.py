import pylab
import imageio

filename = 'C:\\Users\\jw397\\Videos\\Captures\\a.mp4'
vid = imageio.get_reader(filename,  'ffmpeg')
nums = [12, 233]
for num in nums:
    image = vid.get_data(num)
    fig = pylab.figure()
    fig.suptitle('image #{}'.format(num), fontsize=20)
    pylab.imshow(image)
pylab.show()
