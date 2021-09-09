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
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0

# Tree trunk
# Center of 100, 320
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(100, 320, 20, 90, arcade.csscolor.SIENNA)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Another tree, with a trunk and ellipse for top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)
# Finish drawing

arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()