import arcade

arcade.open_window(800, 600, "Car")

arcade.set_background_color(
    arcade.color.SKY_BLUE
)

arcade.start_render()

leaves_h= 200
leaves_w = 20
trunk_h = 80
trunk_w = 20
x, y = 200, 180
arcade.draw_rectangle_filled(
    x, y, trunk_w, trunk_h,
    arcade.color.BROWN
)
arcade.draw_triangle_filled(
    x - leaves_w, y, 
    x + leaves_w, y,
    x, y + leaves_h, 
    arcade.color.FOREST_GREEN,
)

#The Road
arcade.draw_rectangle_filled(
    0, 50, 1600, 200,
    arcade.color.GRAY
)
#THE CAR
#The car tires
arcade.draw_circle_filled(
    350, 150, 30,
    arcade.color.BLACK
)
arcade.draw_circle_filled(
    600, 150, 30,
    arcade.color.BLACK
)
#The wheels
arcade.draw_circle_filled(
    350, 150, 25,
    arcade.color.WHITE
)
arcade.draw_circle_filled(
    600, 150, 25,
    arcade.color.WHITE
)
arcade.draw_circle_filled(
    350, 150, 20,
    arcade.color.BLACK
)
arcade.draw_circle_filled(
    600, 150, 20,
    arcade.color.BLACK
)
#rear and front fender
x = 350
y = 150
width = 40
height = 40
start_angle = 5
end_angle = 178
arcade.draw_arc_outline(x, y, width, height, arcade.color.RED,
                        start_angle, end_angle, 10)
arcade.draw_arc_outline(600, 150, 40, 40, arcade.color.RED,
                        5, 178, 10)
#Body
arcade.draw_lrtb_rectangle_filled(
    390, 560, 250, 152,
    arcade.color.RED
)
arcade.draw_line(555, 249, 640, 160, arcade.color.RED, 4)
arcade.draw_line(390, 249, 308, 160, arcade.color.RED, 4)
#The Sun
arcade.draw_circle_filled(
    750, 600, 110, 
    arcade.color.ORANGE_PEEL
)
arcade.draw_circle_filled(
    750, 600, 100, 
    arcade.color.YELLOW_ORANGE
)
#The Clouds
arcade.draw_ellipse_filled(
    200, 500, 275, 75,
    arcade.color.WHITE_SMOKE
)


arcade.finish_render()
arcade.run()