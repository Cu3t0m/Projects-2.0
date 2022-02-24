import chalk from "chalk";
import inquirer from "inquirer";
import chalkAnimation from "chalk-animation";
import { urlToHttpOptions } from "url";

const pkgname = "todo-cli";

const { log, clear } = console;

const sleep = (ms = 2000) => new Promise((r) => setTimeout(r, ms));

async function welcome() {
  const rainbowTitle = chalkAnimation.rainbow("Yo!");

  await sleep();
  rainbowTitle.stop();

  log(`Welcome to ${pkgname}!`);
}

async function userName() {
  const answers = await inquirer.prompt({
    name: "user_name",
    type: "input",
    message: "What's your name?",
    default() {
      return "Player";
    },
  });

  userName = answers.user_name;
}

async function Options() {
    const options.
}

clear();
await userName();
await Options()