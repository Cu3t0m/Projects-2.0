const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const search_element = 5;

array.forEach((element) => {
  if (element === search_element) {
    console.log(`element found at index ${element}`);
    process.exit();
  } else {
    console.log("Element not found");
  }
});
