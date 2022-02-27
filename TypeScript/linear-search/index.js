"use strict";
exports.__esModule = true;
var process_1 = require("process");
var console_1 = require("console");
var random_1 = require("random");
var main = function () {
    var searchList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    var numberToSearch = random_1["default"].int((min = 0), (max = searchList.length));
    var complete = false;
    for (var i = 0; i < searchList.length; i++) {
        if (numberToSearch === searchList[i]) {
            (0, console_1.log)("Number found at index ".concat(i));
            (0, process_1.exit)();
        }
        else {
            (0, console_1.log)("Item not found");
        }
    }
};
(0, console_1.clear)();
main();
