var binarySearch = function (nums, key) {
    var low = 0;
    var high = nums.length - 1;
    while (low <= high) {
        var mid = Math.floor((low + high) / 2);
        mid;
        if (nums[mid] === key) {
            return mid + 1;
        }
        if (key > nums[mid]) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    return -1;
};
var array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var sKey = 6;
console.log("Searching for ".concat(sKey));
console.log("Index of ".concat(sKey, " : ").concat(binarySearch(array, sKey)));
