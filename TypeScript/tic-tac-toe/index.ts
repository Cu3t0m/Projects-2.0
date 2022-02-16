import { spawn } from 'child_process';
import { exit } from 'process';
const clear = spawn('clear');
const prompt = require('prompt-sync')();

                  /*  1   2   3  |  4    5    6  |  7   8   9 */
let board: any[] = [[" "," "," "],[" ", " ", " "],[" "," "," "]]

class CPoint {
    x:number | any;
    y:number | any;
}

function print_board() {
    console.log(board[2][0] + '|' + board[2][1] + '|' + board[2][2]);
    console.log('-+-+-');
    console.log(board[1][0] + '|' + board[1][1] + '|' + board[1][2]);
    console.log('-+-+-');
    console.log(board[0][0] + '|' + board[0][1] + '|' + board[0][2]);
}

function clean_board(board: any[]) {
    for (let entry in board) {
        board[entry] = " "
    }
}

function restart() {
    let input = prompt("Do you want to restart? (y/n)")
    if (input == 'y' || 'Y') {
        clean_board(board);
        clear.stdout.on('data', (data: string) => {
            console.log(`stdout: ${data}`);
        });
        main()
    }  else if (input == 'n' || 'N') {
        console.log("Thanks for playing!")
        clear.stdout.on('data', (data: string) => {
            console.log(`stdout: ${data}`);
        });
        exit()
    }
}

function main() {
    let current_turn = "x";
    let turn_count = 0;

    for (let i = 0; i <= 10; i++) {
        print_board()
        console.log(`Hey ${current_turn}, it's your go!`)
        let cpt = new CPoint
        cpt.x = prompt('Enter x coordinate')
        cpt.y = prompt('Enter y coordinate')
    }
}

main()