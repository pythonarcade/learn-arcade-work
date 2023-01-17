import arcade

arcade.open_window(800, 800, "landscape")

#background color
arcade.set_background_color((27, 27, 27))

arcade.start_render()



#Ground
arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, (26, 36, 33))

#House
arcade.draw_lrtb_rectangle_filled(300, 700, 500, 250, arcade.color.JET)

#Chimney
arcade.draw_lrtb_rectangle_filled(600, 650, 625, 500, (20, 20, 20))

#Roof
arcade.draw_triangle_filled(300, 500, 500, 600, 700, 500, (43, 43, 43))

#Door
arcade.draw_lrtb_rectangle_filled(600, 650, 350, 250, arcade.color.DARK_BROWN)
#Door Handle
arcade.draw_circle_filled(100, 650, 50, arcade.color.GHOST_WHITE)
#Door Window

#arcade.draw_lrtb_rectangle_filled(300, 700, 500, 250, arcade.color.YELLOW)

#Window at Ground Level
arcade.draw_rectangle_outline(420, 320, 125, 50, arcade.color.BLACK)
#Upper Windows
arcade.draw_rectangle_outline(420, 450, 60, 60, arcade.color.BLACK)
arcade.draw_rectangle_outline(625, 450, 60, 60, arcade.color.BLACK)

#Light From House
#arcade.draw_lrtb_rectangle_filled(300, 700, 500, 250, arcade.color.YELLOW)

#moon
arcade.draw_circle_filled(100, 650, 50, arcade.color.GHOST_WHITE)
arcade.draw_circle_filled(120, 650, 40, (27, 27, 27))

#Shooting Star

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()