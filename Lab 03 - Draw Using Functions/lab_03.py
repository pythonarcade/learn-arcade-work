import arcade
import random
from arcade.examples.sprite_explosion_particles import PARTICLE_FADE_RATE

Screen_Width = 1000
Screen_Height = 800
star_coordinate_list = []

def draw_light_from_house():
    arcade.draw_ellipse_filled(625, 320, 28, 48, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_filled(420, 320, 123, 48, arcade.color.DARK_YELLOW)

def draw_upper_windows(x, y):
    arcade.draw_rectangle_filled(x, y, 58, 58, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_outline(x, y, 60, 60, arcade.color.BLACK, 2)
    arcade.draw_line(x - 30, y, x + 30, y, arcade.color.BLACK, 2)
    arcade.draw_line(x, y - 30, x, y + 30, arcade.color.BLACK, 2)

def draw_house():
    arcade.draw_lrtb_rectangle_filled(300, 700, 500, 250, arcade.color.JET)
    arcade.draw_lrtb_rectangle_filled(600, 650, 625, 500, (20, 20, 20))
    arcade.draw_triangle_filled(300, 500, 500, 600, 700, 500, (43, 43, 43))
    arcade.draw_lrtb_rectangle_filled(600, 650, 350, 250, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(610, 290, 3, arcade.color.BLACK)
    arcade.draw_ellipse_outline(625, 320, 30, 50, arcade.color.BLACK)
    arcade.draw_rectangle_outline(420, 320, 125, 50, arcade.color.BLACK, 2)

def stars(point_list):
    arcade.draw_points(point_list, arcade.color.GHOST_WHITE, 2)

def moon():
    arcade.draw_circle_filled(100, 650, 50, arcade.color.GHOST_WHITE)
    arcade.draw_circle_filled(120, 650, 40, (27, 27, 27))

def ground():
    arcade.draw_lrtb_rectangle_filled(0, 999, 300, 0, (26, 36, 33))

def tree(x, y):
    arcade.draw_rectangle_filled(x, y, 30, 60, (69, 41, 19))
    arcade.draw_triangle_filled(x - 30, y + 30, x, y + 70, x + 30, y + 30, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(x - 30, y + 60, x, y + 100, x + 30, y + 60, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(x - 30, y + 90, x, y + 130, x + 30, y + 90, arcade.color.DARK_GREEN)

def main():
    arcade.open_window(Screen_Width, Screen_Height, "landscape")

    # background color
    arcade.set_background_color((27, 27, 27))

    arcade.start_render()

    # Start Drawing
    ground()

    for x in range(0, 100):
        x_stars = random.randint(0, 1000)
        y_stars = random.randint(400, 800)
        x_and_y_object = (x_stars, y_stars)
        star_coordinate_list.append(x_and_y_object)

    stars(star_coordinate_list)

    # House
    draw_house()

    draw_light_from_house()
    draw_upper_windows(390, 450)
    draw_upper_windows(505, 450)
    draw_upper_windows(620, 450)
    moon()

    tree(50, 290)
    tree(120, 290)
    tree(850, 290)
    tree(920, 290)

    # Finish drawing
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()

# calling the main function
main()
