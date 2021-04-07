import arcade



arcade.open_window(650, 650, "Drawing Example")

arcade.set_background_color(arcade.color.VIOLET)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 650, 325, 0, arcade.color.PURPLE)

arcade.finish_render()

arcade.run()