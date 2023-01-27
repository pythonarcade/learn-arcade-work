import arcade
from arcade.examples.sprite_explosion_particles import PARTICLE_FADE_RATE

Screen_Width = 800
Screen_Height = 800
point_list = ((165, 495), (200, 760), (250, 700), (270, 650), (400, 670),
                  (450, 780), (490, 620), (510, 730), (525, 700), (560, 630),
                  (600, 760), (610, 690), (650, 650), (690, 730), (700, 700),
                  (724, 665), (740, 615), (770, 720), (775, 705), (180, 770))

def draw_light_from_house():
    arcade.draw_ellipse_filled(625, 320, 28, 48, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_filled(420, 320, 123, 48, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_filled(420, 450, 58, 58, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_filled(625, 450, 58, 58, arcade.color.DARK_YELLOW)

def draw_upper_windows():
    arcade.draw_rectangle_outline(420, 450, 60, 60, arcade.color.BLACK, 2)
    arcade.draw_rectangle_outline(625, 450, 60, 60, arcade.color.BLACK, 2)
    arcade.draw_line(390, 450, 450, 450, arcade.color.BLACK, 2)
    arcade.draw_line(595, 450, 655, 450, arcade.color.BLACK, 2)

def stars():
    arcade.draw_points(point_list, arcade.color.GHOST_WHITE, 2)

def moon():
    arcade.draw_circle_filled(100, 650, 50, arcade.color.GHOST_WHITE)
    arcade.draw_circle_filled(120, 650, 40, (27, 27, 27))

def main():
    arcade.open_window(Screen_Width, Screen_Height, "landscape")

    # background color
    arcade.set_background_color((27, 27, 27))

    arcade.start_render()

    # Start Drawing
    stars()

    # Ground
    arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, (26, 36, 33))

    # House
    arcade.draw_lrtb_rectangle_filled(300, 700, 500, 250, arcade.color.JET)

    # Chimney
    arcade.draw_lrtb_rectangle_filled(600, 650, 625, 500, (20, 20, 20))

    # Roof
    arcade.draw_triangle_filled(300, 500, 500, 600, 700, 500, (43, 43, 43))

    # Door
    arcade.draw_lrtb_rectangle_filled(600, 650, 350, 250, arcade.color.DARK_BROWN)

    # Door Handle
    arcade.draw_circle_filled(610, 290, 3, arcade.color.BLACK)

    # Door Window
    arcade.draw_ellipse_outline(625, 320, 30, 50, arcade.color.BLACK)

    # Window at Ground Level
    arcade.draw_rectangle_outline(420, 320, 125, 50, arcade.color.BLACK, 2)

    draw_light_from_house()
    draw_upper_windows()
    moon()

    # Finish drawing
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


# calling the main function
main()
