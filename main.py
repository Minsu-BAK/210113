let 몫 = 0
let 이진수_결과 = 0
let 리스트 = 0
let 입력값 = 0
function binary (num: number) {
    몫 = num
    while (몫 != 0) {
        let 결과 = 0
        이진수_결과 = 몫 % 2
        몫 = Math.floor(몫 / 2)
        basic.showNumber(결과)
        basic.pause(500)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `)
        리스트.push(이진수_결과)
    }
}
input.onButtonPressed(Button.A, function () {
    입력값 = 19
    basic.showNumber(입력값)
    binary(입력값)
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(리스트)
})
