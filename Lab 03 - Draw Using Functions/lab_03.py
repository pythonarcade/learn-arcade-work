import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snow_person():
    arcade.draw_circle_filled(300, 200, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 280, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 340, 40, arcade.color.WHITE)

    arcade.draw_circle_filled(285, 350, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315, 350, 5, arcade.color.BLACK)

def main():
    arcade.open_window(SCREEN_HEIGHT, SCREEN_WIDTH, "Drwaing with Functions")
    arcade.set_background_color(arcade.color.NAVY_BLUE)
    arcade.start_render()

    draw_grass()
    draw_snow_person()

    arcade.finish_render()
    arcade.run()

main()