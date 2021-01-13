let 몫: number = []
let 리스트: number[] = []
let 입력값: number = []
function binary (num: number) {
    몫 = num
    리스트 = []
    while (몫 != 0) {
        let 결과: number[] = []
        결과.push(몫 % 2)
        몫 = Math.floor(몫 / 2)
        basic.pause(500)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `)
    }
}
input.onButtonPressed(Button.A, function () {
    입력값 = 19
    basic.showNumber(입력값)
    binary(입력값)
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index <= 리스트.length; index++) {
        basic.showNumber(리스트[index])
    }
})
