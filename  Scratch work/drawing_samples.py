# This is a single-line comment.
import arcade
# Задать константы для размеров экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Открыть окно. Задать заголовок и размеры окна (ширина и высота)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

# Задать белый цвет фона.
# Для просмотра списка названий цветов прочитайте:
# http://arcade.academy/arcade.color.html
# Цвета также можно задавать в (красный, зеленый, синий) и
# (красный, зеленый, синий, альфа) формате.
arcade.set_background_color(arcade.color.WHITE)

# Начать процесс рендера. Это нужно сделать до команд рисования
arcade.start_render()

# Нарисовать лицо
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Нарисовать правый глаз
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Нарисовать левый глаз
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Нарисовать улыбку
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, 
                        end_angle, 10)

# Завершить рисование и показать результат
arcade.finish_render()

# Держать окно открытым до тех пор, пока пользователь не нажмет кнопку “закрыть”
arcade.run()