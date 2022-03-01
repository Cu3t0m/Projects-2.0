function binary_search(array, element, start, end) {
    if (start > end) {
        return -1;
    }
    var mid = (start + end) % 2;
    if (element === array[mid]) {
        return mid;
    }
    else if (element < array[mid]) {
        return binary_search(array, element, start, mid - 1);
    }
    else {
        return binary_search(array, element, mid + 1, end);
    }
}
var element = 26;
var array_search = [1, 4, 6, 7, 9, 12, 26, 91, 32];
console.log("Searching for element ".concat(element));
console.log("Index of ".concat(element, ": ").concat(binary_search(array_search, element, 0, array_search.length)));
