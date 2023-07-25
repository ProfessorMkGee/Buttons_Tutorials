input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Meh)
})
// an event is something that happens... when we press the a button something will happen!
input.onButtonPressed(Button.B, function on_button_pressed_a2() {
    basic.showIcon(IconNames.Rabbit)
})
// second event happens when you press the B button
input.onButtonPressed(Button.AB, function on_button_pressed_a3() {
    basic.showIcon(IconNames.Silly)
    basic.showIcon(IconNames.Surprised)
})
