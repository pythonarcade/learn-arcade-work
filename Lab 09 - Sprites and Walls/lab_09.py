import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5
COIN_SCALING = 0.3

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "SPRITE LOCKED IN A BOX"

# coin number / anymore, and it will crash system :(
Number_Of_Coins = 100

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 150

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.3

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # good sprite sound
        self.goodSpriteSound = arcade.load_sound(":resources:sounds/coin3.wav")

        # Sprite lists
        self.score = None
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer"
                                           "/maleAdventurer_walk0.png",
                                           scale=0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # score
        self.score = 0

        # -- Set up the walls
        # set up the outer border
        # y loops the bottom and the top of the area we want to block in
        for y in (0, 1536):
            # loop through each box across
            for x in range(0, 1600, 64):
                wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

        # create the left and right limits
        for x in (0, 1536):
            # loop each box
            for y in range(64, 1600, 64):
                wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

        # set up random inside boxes
        for x in range(200, 1536, 210):
            for y in range(200, 1450, 64):
                if random.randrange(3) > 0:
                    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # set up coins
        # make sure they aren't in the walls / boxes
        # very effective but inefficient / keeps crashing computer with to many coins due to complexity
        for i in range(Number_Of_Coins):
            # Coin instance / prob should have been less generic
            coin_placed_successfully = False
            coin = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)

            # while loop to check and see if coin is not in box / wall and keep trying until successful
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(1600)
                coin.center_y = random.randrange(1600)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin / didn't think of this on my own but super smart
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                # winner winner chicken dinner!
                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Select the (un-scrolled) camera for our GUI
        self.camera_gui.use()
        # draw the score with the un-scrolled camera
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.coin_list.update()

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        # Generate a list of all good sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,

                                                              self.coin_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        # Good sprite loop
        for coin in coins_hit_list:
            arcade.play_sound(self.goodSpriteSound)
            coin.remove_from_sprite_lists()
            self.score += 10

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
