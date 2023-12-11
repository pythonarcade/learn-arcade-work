""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_BAD_OBJ = 0.3
SPRITE_SCALING_GOOD_OBJ = 0.2
COIN_COUNT = 50
ROCK_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Good Sprite class
class GoodSprite(arcade.Sprite):
    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

        self.angle += 1

        # If we rotate past 360, reset it back a turn.
        if self.angle > 359:
            self.angle -= 360


# Bad Sprite class
class BadSprite(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # good sprite sound
        self.goodSpriteSound = arcade.load_sound(":resources:sounds/coin3.wav")

        # bad sprite sound
        self.badSpriteSound = arcade.load_sound(":resources:sounds/gameover5.wav")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bad_sprite_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_jump.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins // good sprites
        for i in range(COIN_COUNT):
            # Create the coin instance
            coin = GoodSprite(":resources:images/items/coinGold.png", SPRITE_SCALING_GOOD_OBJ)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Create the rocks // Bad sprites
        for i in range(ROCK_COUNT):
            # Create the rock instance
            rock = BadSprite(":resources:images/space_shooter/meteorGrey_med1.png", SPRITE_SCALING_BAD_OBJ)

            # Position the rock
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            rock.change_x = random.randrange(-3, 4)
            rock.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.bad_sprite_list.append(rock)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.bad_sprite_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.coin_list) == 0:
            # Draw Game Over
            arcade.draw_text("GAME OVER", 325, 350, arcade.color.WHITE, 20)
            # End Game Sound

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

        # Freeze Player
        if len(self.coin_list) == 0:
            self.player_sprite.center_x = 400
            self.player_sprite.center_y = 300

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.bad_sprite_list.update()

        # Generate a list of all good sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Generate a list of all bad sprites that collided with the player.
        bad_sprite_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                   self.bad_sprite_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        # Good sprite loop
        for coin in coins_hit_list:
            arcade.play_sound(self.goodSpriteSound)
            coin.remove_from_sprite_lists()
            self.score += 10

        # Bad sprite loop
        for rock in bad_sprite_hit_list:
            arcade.play_sound(self.badSpriteSound)
            rock.remove_from_sprite_lists()
            self.score -= 25

        if len(self.coin_list) == 0:
            for rock in self.bad_sprite_list:
                rock.remove_from_sprite_lists()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
