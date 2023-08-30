"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

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

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# Barn cement base
arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BISQUE)

# draw the wall
arcade.draw_lrtb_rectangle_filled(30, 350, 400, 190, arcade.color.BROWN)


arcade.draw_polygon_filled([[10, 400],
                            [75, 540],
                            [300, 540],
                            [380, 400]],
                            arcade.color.BROWN)
'''# Draw the top
arcade.draw_triangle_filled(15, 400, 65, 400, 65, 500,  arcade.color.BROWN)
arcade.draw_triangle_filled(300, 400, 365, 400, 300, 500,  arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(65, 300, 500, 400, arcade.color.LAVA)

arcade.draw_triangle_filled(65, 500, 300, 500, 180, 550,  arcade.color.BROWN)
'''
#window top
arcade.draw_lrtb_rectangle_filled(65, 125, 480, 415, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(230, 300, 480, 420, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(70, 120, 475, 420, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(235, 295, 475, 425, arcade.color.WHITE)

#window left
arcade.draw_lrtb_rectangle_filled(65, 125, 300, 250, arcade.color.BLACK )
arcade.draw_lrtb_rectangle_filled(70, 120, 295, 255, arcade.color.WHITE )

#window right
arcade.draw_lrtb_rectangle_filled(230, 300, 300, 250, arcade.color.BLACK )
arcade.draw_lrtb_rectangle_filled(235, 295, 295, 255, arcade.color.WHITE )

#door
arcade.draw_lrtb_rectangle_filled(150, 200, 300, 190, arcade.color.ASH_GREY )


#machine body
arcade.draw_lrtb_rectangle_filled(480, 690, 210, 120, arcade.color.ASH_GREY )
arcade.draw_lrtb_rectangle_filled(510, 650, 150, 120, arcade.color.BLACK )
arcade.draw_lrtb_rectangle_filled(600, 610, 250, 210, arcade.color.BLACK )

#back wheel
arcade.draw_circle_filled(450, 150, 55, arcade.color.BLACK)
arcade.draw_circle_filled(450, 150, 50, arcade.color.PAYNE_GREY)
arcade.draw_circle_filled(450, 150, 35, arcade.color.WHITE)
arcade.draw_circle_filled(450, 150, 15, arcade.color.RED)

#front wheel
arcade.draw_circle_filled(650, 130, 35, arcade.color.BLACK)
arcade.draw_circle_filled(650, 130, 30, arcade.color.PAYNE_GREY)
arcade.draw_circle_filled(650, 130, 25, arcade.color.WHITE)
arcade.draw_circle_filled(650, 130, 5, arcade.color.RED)





# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()