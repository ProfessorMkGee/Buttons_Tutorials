def on_button_pressed_a():
    basic.show_icon(IconNames.MEH)
input.on_button_pressed(Button.A, on_button_pressed_a)
#an event is something that happens... when we press the a button something will happen!

def on_button_pressed_a2():
    basic.show_icon(IconNames.RABBIT)
input.on_button_pressed(Button.B, on_button_pressed_a2)
#second event happens when you press the B button

def on_button_pressed_a3():
    basic.show_icon(IconNames.SILLY)
    basic.show_icon(IconNames.SURPRISED)
input.on_button_pressed(Button.AB, on_button_pressed_a3)
#third event is a secret animation mode