# this will be the greatest slice of pizza know to humankind

import arcade

arcade.open_window(1000, 800, "Drawing Example")

arcade.set_background_color((84, 72, 3))

arcade.start_render()

# code for plate, had to put it first or else it would overlap
arcade.draw_circle_filled(500, 400, 400, arcade.csscolor.WHITE)

# Pizza triangle foundation, pretty straightforward.
arcade.draw_triangle_filled(100, 400, 800, 550, 800, 250, (247, 222, 129))

# Crust for pizza
arcade.draw_rectangle_filled(800, 400, 50, 300, (224, 180, 99))

# First peperoni
arcade.draw_circle_filled(400, 395, 37, arcade.csscolor.RED)

# Second peperoni
arcade.draw_circle_filled(600, 430, 40, arcade.csscolor.RED)

# Mushroom slice, cosists of an arc and a rectangle, much like the code for one of the trees
arcade.draw_arc_filled(700, 330, 80, 120, (133, 122, 81), 0, 180)
arcade.draw_rectangle_filled(700, 320, 20, 40, (133, 122, 81))

# Fun text :P
arcade.draw_text("Pizza plate for only pizza", 400, 700, arcade.csscolor.BLACK)

arcade.finish_render()

arcade.run()