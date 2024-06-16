a = 0
b = 0

def on_button_pressed_a():
    global a
    for index in range(1):
        basic.show_icon(IconNames.CHESSBOARD)
        basic.pause(100)
        basic.show_leds("""
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            """)
    a = randint(0, 10)
    basic.show_number(a)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("º" + str(a * b))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global b
    for index2 in range(1):
        basic.show_icon(IconNames.CHESSBOARD)
        basic.pause(100)
        basic.show_leds("""
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            """)
    b = randint(0, 10)
    basic.show_number(b)
input.on_button_pressed(Button.B, on_button_pressed_b)
