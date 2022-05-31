/*
Moves the cursor to the next box once a character has been entered.  Ignores certain keys to improve the 
navigation between boxes and therefore the user experience.
*/

document.getElementById("1").focus();

// https://stackoverflow.com/questions/40956717/how-to-addeventlistener-to-multiple-elements-in-a-single-line
const inputBoxes = document.getElementsByClassName("char-input-box");
const reservedKeys = ["Backspace", "Delete", "Tab", "Shift"];
// https: //www.codegrepper.com/code-examples/javascript/frameworks/ionic/javascript+if+statement+with+time+delay
const delay = 100; //sets delay for .5 second

for (let i = 0; i < inputBoxes.length; i++) {
    inputBoxes[i].addEventListener("keydown", function () {
        if (reservedKeys.includes(event.key)) {
            inputBoxes[i].focus();
        } else {
            setTimeout(function () {
                inputBoxes[i + 1].focus();
            }, delay)
        }
    });
}