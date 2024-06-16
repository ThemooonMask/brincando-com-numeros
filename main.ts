let a = 0
let b = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    for (let index = 0; index < 1; index++) {
        basic.showIcon(IconNames.Chessboard)
        basic.pause(100)
        basic.showLeds(`
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            `)
    }
    a = randint(0, 10)
    basic.showNumber(a)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString("º" + ("" + a * b))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    for (let index2 = 0; index2 < 1; index2++) {
        basic.showIcon(IconNames.Chessboard)
        basic.pause(100)
        basic.showLeds(`
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            `)
    }
    b = randint(0, 10)
    basic.showNumber(b)
})
