let Inputs = document.querySelectorAll(".floating_input_wrapper input");
let TextAreas = document.querySelectorAll(".floating_input_wrapper textarea");
const HandleBlurInput = (e) => {
  if (e.target.value != "") {
    e.target.parentNode.classList.add("active");
  } else {
    e.target.parentNode.classList.remove("active");
  }
};
const HandleFocusInput = (e) => {
  // e.target.parentNode.style.marginTop = "30px";
};

window.addEventListener("load", (e) => {
  Inputs.forEach((EachInput) => {
    if (EachInput.value != "") {
      EachInput.parentNode.classList.add("active");
    } else {
      EachInput.parentNode.classList.remove("active");
    }
  });
});
Inputs.forEach((EachInput) => {
  EachInput.addEventListener("blur", HandleBlurInput);
});
Inputs.forEach((EachInput) => {
  EachInput.addEventListener("focus", HandleFocusInput);
});
TextAreas.forEach((EachInput) => {
  EachInput.addEventListener("blur", HandleBlurInput);
});
TextAreas.forEach((EachInput) => {
  EachInput.addEventListener("focus", HandleFocusInput);
});
