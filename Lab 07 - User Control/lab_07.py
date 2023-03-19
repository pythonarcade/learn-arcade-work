""" Lab 7 - User Control """
import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 2


# draw light for the windows function
def draw_light_from_house():
    arcade.draw_ellipse_filled(625, 320, 28, 48, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_filled(420, 320, 123, 48, arcade.color.DARK_YELLOW)


# draw upper windows function
def draw_upper_windows(x, y):
    arcade.draw_rectangle_filled(x, y, 58, 58, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_outline(x, y, 60, 60, arcade.color.BLACK, 2)
    arcade.draw_line(x - 30, y, x + 30, y, arcade.color.BLACK, 2)
    arcade.draw_line(x, y - 30, x, y + 30, arcade.color.BLACK, 2)


# draw house function
def draw_house():
    arcade.draw_lrtb_rectangle_filled(300, 700, 500, 250, arcade.color.JET)
    arcade.draw_lrtb_rectangle_filled(600, 650, 625, 500, (20, 20, 20))
    arcade.draw_triangle_filled(300, 500, 500, 600, 700, 500, (43, 43, 43))
    arcade.draw_lrtb_rectangle_filled(600, 650, 350, 250, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(610, 290, 3, arcade.color.BLACK)
    arcade.draw_ellipse_outline(625, 320, 30, 50, arcade.color.BLACK)
    arcade.draw_rectangle_outline(420, 320, 125, 50, arcade.color.BLACK, 2)


# draw moon function
def moon(x, y):
    arcade.draw_circle_filled(x, y, 50, arcade.color.GHOST_WHITE)
    arcade.draw_circle_filled(x + 20, y, 40, (27, 27, 27))


# draw ground function
def ground():
    arcade.draw_lrtb_rectangle_filled(0, 999, 300, 0, (26, 36, 33))


# draw trees function
def tree(x, y):
    arcade.draw_rectangle_filled(x, y, 30, 60, (69, 41, 19))
    arcade.draw_triangle_filled(x - 30, y + 30, x, y + 70, x + 30, y + 30, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(x - 30, y + 60, x, y + 100, x + 30, y + 60, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(x - 30, y + 90, x, y + 130, x + 30, y + 90, arcade.color.DARK_GREEN)


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        # edge sound
        self.edge_sound = arcade.load_sound(":resources:")
        self.edge_sound_player = None

        if self.position_x < 8:
            self.position_x = 8
            if not self.edge_sound_player or not self.edge_sound_player.playing:
                self.edge_sound_player = arcade.play_sound(self.edge_sound)
                arcade.play_sound(self.edge_sound)

        if self.position_y < 0:
            self.position_y = 0
            if not self.edge_sound_player or not self.edge_sound_player.playing:
                self.edge_sound_player = arcade.play_sound(self.edge_sound)
                arcade.play_sound(self.edge_sound)

        if self.position_x > SCREEN_WIDTH - 25:
            self.position_x = SCREEN_WIDTH - 25
            if not self.edge_sound_player or not self.edge_sound_player.playing:
                self.edge_sound_player = arcade.play_sound(self.edge_sound)
                arcade.play_sound(self.edge_sound)

        if self.position_y > SCREEN_HEIGHT - 50:
            self.position_y = SCREEN_HEIGHT - 50
            if not self.edge_sound_player or not self.edge_sound_player.playing:
                self.edge_sound_player = arcade.play_sound(self.edge_sound)
                arcade.play_sound(self.edge_sound)

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.WHITE)

        arcade.set_background_color((27, 27, 27))

        # sounds
        self.click_sound1 = arcade.load_sound(":resources:")
        self.click_sound2 = arcade.load_sound(":resources:")

    def on_draw(self):
        arcade.start_render()

        # Start Drawing
        # draw ground
        ground()

        # draw House
        draw_house()

        # draw light
        draw_light_from_house()

        # draw windows
        draw_upper_windows(390, 450)
        draw_upper_windows(505, 450)
        draw_upper_windows(620, 450)

        # draw moon
        moon(100, 650)

        # draw trees
        tree(50, 290)
        tree(120, 290)
        tree(850, 290)
        tree(920, 290)


        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0



def main():
    window = MyGame()
    arcade.run()


main()
