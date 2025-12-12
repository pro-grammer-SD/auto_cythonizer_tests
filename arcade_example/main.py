import arcade
import random

WIDTH = 800
HEIGHT = 600

class Box(arcade.SpriteSolidColor):
    def __init__(self):
        super().__init__(5, 5, arcade.color.WHITE)
        self.change_x = random.uniform(-3, 3)
        self.change_y = random.uniform(-3, 3)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Choke Test")
        self.boxes = arcade.SpriteList()
        for _ in range(1000):
            b = Box()
            b.center_x = random.randint(0, WIDTH)
            b.center_y = random.randint(0, HEIGHT)
            self.boxes.append(b)
        self.fps_text = arcade.Text("", 10, 10, arcade.color.WHITE, 18)

    def on_update(self, delta_time):
        for b in self.boxes:
            b.center_x += b.change_x
            b.center_y += b.change_y
            if b.center_x < 0 or b.center_x > WIDTH:
                b.change_x *= -1
            if b.center_y < 0 or b.center_y > HEIGHT:
                b.change_y *= -1
        fps = 1 / delta_time if delta_time > 0 else 0
        self.fps_text.text = f"FPS: {int(fps)}"

    def on_draw(self):
        self.clear()
        self.boxes.draw()
        self.fps_text.draw()

Game()
arcade.run()
