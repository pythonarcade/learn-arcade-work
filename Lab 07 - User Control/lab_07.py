""" Lab 7 - User Control """
import arcade

# --- Constants ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
# faster gives cool ghost like graphics behind the models
MOVEMENT_SPEED = 4


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


class PacMan:
    def __init__(self, position_x, position_y, change_x, change_y, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self):
        # Draw the pacman.
        arcade.draw_circle_filled(self.position_x, self.position_y, 25, self.color)
        arcade.draw_triangle_filled(self.position_x, self.position_y, self.position_x + 20, self.position_y + 18,
                                    self.position_x + 20, self.position_y - 18, arcade.color.BLACK)
        arcade.draw_triangle_filled(self.position_x + 27, self.position_y, self.position_x + 20, self.position_y + 18,
                                    self.position_x + 20, self.position_y - 18, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x + 5, self.position_y + 17, 3, arcade.color.BLACK)

    def update(self):
        # Move the pacman
        self.position_y += self.change_y
        self.position_x += self.change_x


class Ghost:
    def __init__(self, position_x, position_y, change_x, change_y, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

        # edge sound
        self.edge_sound = arcade.load_sound(":resources:sounds/hit4.wav")

    def draw(self):
        # Draw the Ghost.
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 30, 30, self.color)
        arcade.draw_circle_filled(self.position_x + 5, self.position_y + 5, 2, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x - 5, self.position_y + 5, 2, arcade.color.BLACK)

    def update(self):
        # Move the Ghost
        self.position_y += self.change_y
        self.position_x += self.change_x

        # edge control, so we don't fly off the screen as well as edge sounds... the more the merrier.
        if self.position_x < 15:
            arcade.play_sound(self.edge_sound)
            self.position_x = 15

        if self.position_x > SCREEN_WIDTH - 15:
            arcade.play_sound(self.edge_sound)
            self.position_x = SCREEN_WIDTH - 15

        if self.position_y < 15:
            arcade.play_sound(self.edge_sound)
            self.position_y = 15

        if self.position_y > SCREEN_HEIGHT - 15:
            arcade.play_sound(self.edge_sound)
            self.position_y = SCREEN_HEIGHT - 15


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control - Ghost")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Create our Ghosts
        self.ghost1 = Ghost(200, 200, 0, 0, arcade.color.LIGHT_BLUE)
        self.pacman = PacMan(400, 200, 0, 0, arcade.color.YELLOW)

        # click sound for the mouse
        self.click_sound = arcade.load_sound(":resources:sounds/laser5.wav")

        # background color for the program
        arcade.set_background_color((27, 27, 27))

    # draw all the stuff!
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

        # draw the mobile characters
        self.ghost1.draw()
        self.pacman.draw()

    # update the characters
    def update(self, delta_time):
        self.ghost1.update()
        self.pacman.update()

    # on keypress move the ghost
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ghost1.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ghost1.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ghost1.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ghost1.change_y = -MOVEMENT_SPEED

    # on key release stop moving the ghost
    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ghost1.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ghost1.change_y = 0

    # mouse controls for the pacman
    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.pacman.position_x = x
        self.pacman.position_y = y

    # mouse click controls to enact sound effects
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.click_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.click_sound)


# throw everything into main to get called to start the program
def main():
    MyGame()
    arcade.run()


# start the program
main()
