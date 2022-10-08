/*
https://jasonwatmore.com/post/2021/10/02/vanilla-js-create-an-array-with-a-range-of-numbers-in-a-javascript
(function() {
    // 0 to 100 step 10
    const start = 0;
    const end = 100;
    const step = 10;
    const arrayLength = Math.floor(((end - start) / step)) + 1;
    const range = [...Array(arrayLength).keys()].map(x => (x * step) + start);
    document.getElementById('rangeFour').innerHTML = JSON.stringify(range);
})();
*/
