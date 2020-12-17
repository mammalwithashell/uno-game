import arcade

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
SCREEN_TITLE = "Uno"


class Card(arcade.Sprite):
    def __init__(self, role: str, color: str, scale=1):
        """Initialize variables that belong to the class Card
        """
        self.role = role  # Save the type of card
        self.color = color  # Save the color of card

        self.face_file = f"Uno_Sprites/{self.role}_{self.color}.png"
        self.is_face_up = False
        self.back_file = "Uno_Sprites/face_down.png"
        self.scale = scale
        super().__init__(self.back_file, scale)

    def flip(self):
        """Function to flip the card
        """
        if self.is_face_up:
            arcade.load_texture(self.back_file)
            self.is_face_up = False
        else:
            arcade.load_texture(self.face_file)
            self.is_face_up = True


class Deck(arcade.SpriteList):
    pass


class Uno(arcade.Window):
    def __init__(self):
        """Constructor for Uno Window class
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_count: int = None
        self.player_hand_0: arcade.SpriteList = None
        self.player_hand_1: arcade.SpriteList = None
        self.deck: arcade.SpriteList = None
        self.pile: arcade.SpriteList = None

    def setup(self):

        pass

    def on_draw(self):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_release(self, x, y, button):
        pass


def main():
    """Main Function
    """
    window = Uno()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
