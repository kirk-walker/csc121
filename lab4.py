import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_tree():

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
def draw_road():
#The Road
    arcade.draw_rectangle_filled(
        0, 50, 1600, 200,
        arcade.color.GRAY
    )
def draw_sun():
#The Sun
    arcade.draw_circle_filled(
        750, 600, 110, 
        arcade.color.ORANGE_PEEL
    )
    arcade.draw_circle_filled(
        750, 600, 100, 
        arcade.color.YELLOW_ORANGE
    )
def draw_clouds():
#The Clouds
    arcade.draw_ellipse_filled(
        200, 500, 275, 75,
        arcade.color.WHITE_SMOKE
    )
    arcade.draw_ellipse_filled(
        150, 450, 275, 75,
        arcade.color.WHITE_SMOKE
    )
#THE CAR
#The car tires
def draw_car(x, y):

    arcade.draw_circle_filled(
        x, 150 + y, 30,
        arcade.color.BLACK
    )
    arcade.draw_circle_filled(
        x + 250, 150 + y, 30,
        arcade.color.BLACK
    )
    #The wheels
    arcade.draw_circle_filled(
        x, 150+y, 25,
        arcade.color.WHITE
    )
    arcade.draw_circle_filled(
        x + 250, 150+y, 25,
        arcade.color.WHITE
    )
    arcade.draw_circle_filled(
        x, 150+y, 20,
        arcade.color.BLACK
    )
    arcade.draw_circle_filled(
        x + 250, 150+y, 20,
        arcade.color.BLACK
    )
    #rear and front fender
    arcade.draw_arc_outline(x, 150+y, 40, 40, arcade.color.RED,
                            5, 178, 10)
    arcade.draw_arc_outline(x + 250, 150+y, 40, 40, arcade.color.RED,
                            5, 178, 10)
    #Body
    arcade.draw_lrtb_rectangle_filled(
        40+x, 210+x, 250, 152,
        arcade.color.RED
    )
    #555,249,640,160
    arcade.draw_line(205 + x, 249 + y, 290 + x, 160 + y, arcade.color.RED, 4)
    arcade.draw_line(40+x, 249+y, -42+x, 160+y, arcade.color.RED, 4)

positions = {
    "X": 100,
    "Y": 0
}

def on_draw(delta_time):
    arcade.start_render()
    draw_road()
    draw_tree()
    draw_sun()
    draw_clouds

    draw_car(positions["X"], positions["Y"])

    speed = 1

    positions["X"] += speed

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Driving car")
    arcade.set_background_color(arcade.color.SKY_BLUE)

    arcade.schedule(on_draw, 1/60)
    
    arcade.run()

if __name__ == "__main__":
    main()

