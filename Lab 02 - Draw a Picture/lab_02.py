import arcade

arcade.open_window(650, 650, "Drawing Example")

arcade.set_background_color(arcade.color.LIGHT_PINK)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 650, 325, 0, arcade.color.ELECTRIC_BLUE)

arcade.draw_triangle_filled(175, 325, 300, 325, 225, 350, arcade.color.HOT_PINK)
arcade.draw_triangle_filled(0, 325, 225, 325, 100, 400, arcade.color.HOT_PINK)

arcade.draw_triangle_filled(475, 325, 350, 325, 425, 350, arcade.color.HOT_PINK)
arcade.draw_triangle_filled(650, 325, 425, 325, 550, 400, arcade.color.HOT_PINK)

arcade.draw_circle_filled(325, 500, 90, arcade.color.LIGHT_CORAL)
arcade.draw_lines(((0, 420),(650, 420)),
                    arcade.color.LIGHT_PINK, 
                    8)
arcade.draw_lines(((0, 440),(650, 440)),
                    arcade.color.LIGHT_PINK,
                    7)
arcade.draw_lines(((0, 460),(650, 460)),
                    arcade.color.LIGHT_PINK,
                    6)
arcade.draw_lines(((0, 475),(650, 475)),
                    arcade.color.LIGHT_PINK,
                    5)
arcade.draw_lines(((0, 487.5),(650, 487.5)),
                    arcade.color.LIGHT_PINK,
                    4)

arcade.draw_polygon_filled(((300, 326), (350, 326), (475, 0), (175, 0)), arcade.color.LIGHT_SKY_BLUE)


arcade.finish_render()

arcade.run()