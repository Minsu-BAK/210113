몫 = 0
리스트: List[number] = []
입력값 = 0
def binary(num: number):
    global 몫, 리스트
    몫 = num
    리스트 = []
    while 몫 != 0:
        리스트.append(몫 % 2)
        몫 = Math.floor(몫 / 2)

def on_button_pressed_a():
    global 입력값
    입력값 = 19
    basic.show_number(입력값)
    binary(입력값)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    index = 0
    while index <= len(리스트):
        basic.show_number(리스트[index - 1])
        basic.pause(500)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        index += 1
input.on_button_pressed(Button.B, on_button_pressed_b)
