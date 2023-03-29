from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {
    "white": (255,255,255),
    "black": (0,0,0)
}
canvas_color = input("Enter canvas color(white or black): ")

canvas = Canvas(canvas_height, canvas_width, canvas_color)

while True:
    # Ask user for the shape
    shape_type = input("What do you like to draw (rectangle or square)? Enter quit to quit. ")

    # Ask for rectangle data and create rectangle
    if shape_type.lower() == "rectangle":
        rect_x = int(input("Enter x of the rectangle: "))
        rect_y = int(input("Enter y of the rectangle: "))
        rect_width = int(input("Enter width of the rectangle: "))
        rect_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have? (0-255) "))
        green = int(input("How much green should the rectangle have? (0-255)"))
        blue = int(input("How much blue should the rectangle have? (0-255)"))

        # Creat the rectangle
        r1 = Rectangle(rect_x, rect_y, rect_height, rect_width, (red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        sq_x = int(input("Enter x of square: "))
        sq_y = int(input("Enter y of square: "))
        sq_side = int(input("Enter side of square: "))
        red = int(input("How much red should the square have? (0-255) "))
        green = int(input("How much green should the square have? (0-255)"))
        blue = int(input("How much blue should the square have? (0-255)"))


        # Create the square
        s1 = Square(sq_x, sq_y, sq_side, (red, green, blue))
        s1.draw(canvas)

    #Break the loop with quit
    if shape_type.lower() == "quit":
        break

canvas.make("canvas.png")


# canvas = Canvas(20, 30, (255, 255, 255))
# #canvas.make("canvas.png")
# r1 = Rectangle(1,6,10,7,(100,200,125))
# r1.draw(canvas)
# # canvas.make("canvas.png")
# s1 = Square(1,3,3,(0,100,222))
# s1.draw(canvas)
# canvas.make("canvas.png")