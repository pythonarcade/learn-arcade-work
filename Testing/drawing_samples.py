"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color((31, 218, 255))

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0

# Tree trunk
# Center of 100, 320
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(100, 320, 20, 90, (163, 99, 11))

# Tree top
arcade.draw_circle_filled(100, 350, 30, (245, 138, 61))

arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, (168, 131, 29))

# Another tree, with a trunk and ellipse for top
arcade.draw_rectangle_filled(200, 320, 20, 40, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, (156, 55, 25))
# Finish drawing
# Another tree, with a trunk and arc for top
# Arc is centered at (300, 340) with a width of 60 and height of 100.
# The starting angle is 0, and ending angle is 180.
arcade.draw_rectangle_filled(300, 320, 20, 40, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 320, 40, 200, (237, 201, 43), 0, 180)


# Another tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(400, 320, 20, 40, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 500, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 320, 20, 40, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 340)
                            ),
                           arcade.csscolor.DARK_GREEN)

arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()