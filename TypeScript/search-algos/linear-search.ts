import { exit } from "process";
import { log, clear } from "console";


const main = () => {
  let searchList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  let numberToSearch = 7;
  let complete = false;

  for (let i = 0; i < searchList.length; i++) {
    if (numberToSearch === searchList[i]) {
      log(`Number found at index ${i}`);
      exit();
    } else {
      log("Item not found");
    }
  }
};

clear();
main();
