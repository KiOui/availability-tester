import rainbowhat as rainbow


class RainbowWrapper:
    """Wrapper for Rainbowhat."""

    def __init__(self, rotation, brightness):
        rainbow.set_layout(rainbow.PHAT)
        rainbow.rotation(rotation)
        rainbow.brightness(brightness)
        self.width, self.height = rainbow.get_shape()

    def set_pixel(self, width, height, r, g, b):
        height, width = self.convert(height, width)
        rainbow.set_pixel(width, height, r, g, b)

    def show(self):

        rainbow.show()

    def getshape(self):
        return rainbow.get_shape()

    def convert(self, height, width):
        if width < 0 or width > 7 or height < 0 or height > 3:
            raise Exception("Width or height not in range!")

        if width % 2 == 0:
            actualheight = width / 2
            return actualheight, height
        else:
            actualheight = (width - 1) / 2
            if height == 3:
                return actualheight, 4
            elif height == 2:
                return actualheight, 5
            elif height == 1:
                return actualheight, 6
            else:
                return actualheight, 7
