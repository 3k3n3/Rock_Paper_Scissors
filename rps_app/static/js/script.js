// Submit the form on click of the radio buttons without submit button
const radioButtons = document.querySelectorAll('input[type="radio"]');
radioButtons.forEach(button => {
    // 'change' event handler user instead of 'click' to
    // ensure compatibility across different browsers
    button.addEventListener('change', function () {
        game.submit();
    });
});

// Delay scoreboard display by a sec
setTimeout(function () {
    document.getElementById("scoreRow").style.display = "table-row";
}, 1000); // 1000 milliseconds = 1 second
setTimeout(function () {
    document.getElementById("scoreHead").style.display = "contents";
}, 1100);