"use strict";
exports.__esModule = true;
var child_process_1 = require("child_process");
var process_1 = require("process");
var clear = (0, child_process_1.spawn)("clear");
var prompt = require("prompt-sync")();
var board = [
    // 0 0  0 1  0 2
    [" ", " ", " "],
    // 1 0  1 1  1 2
    [" ", " ", " "],
    // 2 0  2 1  2 2
    [" ", " ", " "],
];
var CPoint = /** @class */ (function () {
    function CPoint() {
        this.x = 0;
        this.y = 0;
    }
    return CPoint;
}());
function print_board() {
    console.log(board[2][0] + "|" + board[2][1] + "|" + board[2][2]);
    console.log("-+-+-");
    console.log(board[1][0] + "|" + board[1][1] + "|" + board[1][2]);
    console.log("-+-+-");
    console.log(board[0][0] + "|" + board[0][1] + "|" + board[0][2]);
}
function clean_board(board) {
    for (var entry in board) {
        board[entry] = " ";
    }
}
function restart() {
    var input = prompt("Do you want to restart? (y/n)");
    if (input == "y" || "Y") {
        clean_board(board);
        clear.stdout.on("data", function (data) {
            console.log("stdout: ".concat(data));
        });
        main();
    }
    else if (input == "n" || "N") {
        console.log("Thanks for playing!");
        clear.stdout.on("data", function (data) {
            console.log("stdout: ".concat(data));
        });
        (0, process_1.exit)();
    }
}
function main() {
    var current_turn = "x";
    var turn_count = 0;
    for (var i = 0; i <= 10; i++) {
        print_board();
        console.log("Hey ".concat(current_turn, ", it's your go!"));
        var cpt = new CPoint();
        cpt.x = prompt("Enter x coordinate");
        cpt.y = prompt("Enter y coordinate");
        board[cpt.x][cpt.y] = current_turn;
        if (turn_count >= 5) {
            if ((board[0][0] === board[0][1]) === board[0][2]) {
                console.log("Game over. ".concat(current_turn, " wins!"));
            }
            else if ((board[1][0] === board[1][1]) === board[1][2]) {
                console.log("Game over. ".concat(current_turn, " wins!"));
            }
            else if ((board[2][0] === board[2][1]) === board[2][2]) {
                console.log("Game over. ".concat(current_turn, " wins!"));
            }
            else if ((board[0][0] === board[1][1]) === board[2][2]) {
                console.log("Game over. ".concat(current_turn, " wins!"));
            }
            else if ((board[2][0] === board[1][1]) === board[0][2]) {
                console.log("Game over. ".concat(current_turn, " wins!"));
            }
        }
        if (current_turn === "x") {
            current_turn = "o";
        }
        else {
            current_turn = "x";
        }
        if (turn_count === 9) {
            console.log("Game over. It's a draw!");
        }
    }
}
main();
