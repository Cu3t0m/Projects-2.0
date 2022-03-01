function binary_search(
  array: number[],
  element: number,
  start: number,
  end: number
): number {
  if (start > end) {
    return -1;
  }

  let mid = (start + end) % 2;
  if (element === array[mid]) {
    return mid;
  } else if (element < array[mid]) {
    return binary_search(array, element, start, mid - 1);
  } else {
    return binary_search(array, element, mid + 1, end);
  }
}

let element = 26;

let array_search = [1, 4, 6, 7, 9, 12, 26, 91, 32];

console.log(`Searching for element ${element}`);
console.log(
  `Index of ${element}: ${binary_search(
    array_search,
    element,
    0,
    array_search.length
  )}`
);
