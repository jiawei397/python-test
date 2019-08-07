import imageio

img_paths = ["../resources/ciyun.png", "../resources/test.png"]

def compose_gif(img_paths):
    gif_images = []
    for path in img_paths:
        gif_images.append(imageio.imread(path))
    imageio.mimsave("test.gif", gif_images, fps=1)

if __name__ == '__main__':
    compose_gif(img_paths)
