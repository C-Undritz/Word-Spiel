/*
-----------------------------------------------------------------------------------------------------------
JS required to moves the cursor to the next box once a character has been entered.  Ignores certain keys to 
improve the navigation between boxes and therefore the user experience.
-----------------------------------------------------------------------------------------------------------
*/

document.getElementById("1").focus();

// https://stackoverflow.com/questions/40956717/how-to-addeventlistener-to-multiple-elements-in-a-single-line
const inputBoxes = document.getElementsByClassName("char-input-box");
const reservedKeys = ["Backspace", "Delete", "Tab", "Shift"];
// https: //www.codegrepper.com/code-examples/javascript/frameworks/ionic/javascript+if+statement+with+time+delay
const delay = 100; //sets delay for .1 second

for (let i = 0; i < inputBoxes.length; i++) {
  inputBoxes[i].addEventListener("keydown", function () {
    if (reservedKeys.includes(event.key)) {
      inputBoxes[i].focus();
    } else {
      setTimeout(function () {
        if (i <= 3) {
          // stops console error 'Uncaught TypeError: Cannot read properties of undefined (reading 'focus')'
          console.log(i);
          inputBoxes[i + 1].focus();
        }
      }, delay);
    }
  });
}

/*
-----------------------------------------------------------------------------------------------------------
JS required for the custom modal(https: //www.w3schools.com/howto/howto_css_modals.asp)
-----------------------------------------------------------------------------------------------------------
*/

const modal = document.getElementById("myModal");
const input = document.getElementById("char-input-form");
const btn = document.getElementById("myBtn");
const span = document.getElementsByClassName("close")[0];
const win = document.getElementById("win-bool").innerHTML;
let roundCount = document.getElementById("output-boxes").childElementCount;

/*
When five output displays are shown and now win, modal displays and input disappears so as to disable 
further guesses.
*/
if (roundCount == 5 || win == "True") {
  modal.style.display = "block";
  input.style.display = "none";
}

// Closes modal when the user clicks on <span> (x).
span.onclick = function () {
  modal.style.display = "none";
};

// Closes modal when the user clicks anywhere outside of the modal.
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
