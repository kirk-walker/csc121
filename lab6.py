import arcade


def draw_section_outlines():
    color = arcade.color.BLACK

    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, color)
    arcade.draw_rectangle_outline(450, 150, 300, 300, color)
    arcade.draw_rectangle_outline(750, 150, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, color)
 
    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, color)
    arcade.draw_rectangle_outline(450, 450, 300, 300, color)
    arcade.draw_rectangle_outline(750, 450, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, color)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            # Instead of zero, calculate the proper x location using
            # column
            x = (column * 10) + 5
 
            # Instead of zero, calculate the proper y location using row
            y = (row * 10) + 5
 
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_2():
    for row in range(30):
        for column in range(30):

            x = (column * 10) + 305

            y = (row * 10) + 5
            if column % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:   
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
 
 
def draw_section_3():
    for row in range(30):
        for column in range(30):

            x = (column * 10) + 605

            y = (row * 10) + 5
            if row % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:   
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
 
 
def draw_section_4():
    for row in range(30):
        for column in range(30):

            x = (column * 10) + 905

            y = (row * 10) + 5
            if row % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            elif column % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)    
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
 
def draw_section_5():
    for column in range(30):
        for row in range(column + 1):

            x = (column * 10) + 5
 
            y = (row * 10) + 305

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
   
 
def draw_section_6():
    for row in range(30):
        for column in range(row):
            print(" ", end=" ")
        for column in range(30 - row):
            print(column, end=" ")

            x = (column * 10) + 305
 
            y = (row * 10) + 305

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    print()
 
def draw_section_7():
    for row in range(30):
        for column in range(row + 1):
            print(column, end=" ")
            x = (column * 10) + 605

            y = (row * 10) + 305

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    print()
 
def draw_section_8():
    for row in range(30):
        for column in range((29 - row), 30):
            print(column, end=" ")
            x = (column * 10) + 905

            y = (row * 10) + 305

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    print()
 
 
def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
 
    arcade.start_render()
 
    # Draw the outlines for the sections
    draw_section_outlines()
 
    #draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()

if __name__ =='__main__':
    main()