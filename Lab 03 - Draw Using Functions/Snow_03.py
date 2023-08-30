import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.GREEN)

def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(300 + x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 340 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315 + x, 350 + y, 5, arcade.color.BLACK)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)
on_draw.snow_person1_x = 150

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    arcade.schedule(on_draw, 1/60)
    arcade.run()
    
    #  Finish and run
    arcade.finish_render()
    arcade.run()






main() 