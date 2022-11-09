# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()


arcade.draw_ellipse_outline(450, 50, 470, 700, arcade.csscolor.DIM_GREY, 3)
arcade.draw_ellipse_filled(450, 50, 465, 695, arcade.csscolor.DARK_GREEN)
arcade.draw_ellipse_outline(800, 300, 700, 400, arcade.csscolor.DIM_GREY, 3)
arcade.draw_ellipse_filled(800, 300, 695, 395, arcade.csscolor.DARK_GREEN)
arcade.draw_ellipse_outline(250, 200, 600, 270, arcade.csscolor.DIM_GREY, 3)
arcade.draw_ellipse_filled(250, 200, 595, 265, arcade.csscolor.DARK_GREEN)
arcade.draw_ellipse_outline(1, 250, 700, 400, arcade.csscolor.DIM_GREY, 3)
arcade.draw_ellipse_filled(1, 250, 695, 395, arcade.csscolor.DARK_GREEN)

arcade.draw_lrtb_rectangle_filled(0, 800, 180, 0, arcade.color.MINT_GREEN)


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()