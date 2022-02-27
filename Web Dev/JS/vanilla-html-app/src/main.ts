import "./style.css";

const app = document.querySelector<HTMLDivElement>("#app")!;

app.innerHTML = `
  <h1>Hello Vite!</h1>
  <a href="https://vitejs.dev/guide/features.html" target="_blank">Documentation</a>
`;

let btn = document.querySelector('button');
let count = 0;
btn.onclick = () => count += 1;

const btnModule = document.querySelector<HTMLDivElement>("#button-module");
btnModule.innerHTML = `
  <p> Count is ${count} </p>
`;