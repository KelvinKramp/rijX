let Buttons = {
    prevButton: document.querySelector(".previous"),
    nextButton: document.querySelector(".next"),
    submitButton: document.querySelector(".submit"),
  },
  Steps = {
    currentStep: 1,
    prevStep: 0,
    StepsContainer: document.querySelector(".steps-container"),
  },
  BodyArea = document.querySelector(".body-area");

Buttons.submitButton.addEventListener("click", (e) => {
  e.preventDefault();
});

const GetFormValues = () => {
  let InformationArray = [];
  let SelectValueArray = [];
  let AllInputs = document.querySelectorAll(
    ".step2 .floating_input_wrapper .input-wrapper-new input"
  );
  let AllSelects = document.querySelectorAll(".step_first_area select");

  AllInputs.forEach((EachInput) => {
    InformationArray.push({
      name: EachInput.name,
      value: EachInput.value,
    });
  });
  for (let i = 0; i < AllSelects.length; i++) {
  console.log(AllSelects[i]);
    }
  AllSelects.forEach((EachSelect) => {
    SelectValueArray.push({
      name: EachSelect.name,
      value: EachSelect.value,
    });
  });

  document.querySelector(".confirmation_area").innerHTML = ``;

  InformationArray.forEach((EachObject) => {
    document.querySelector(".confirmation_area").insertAdjacentHTML(
      "beforeend",
      ` <div class="box">
    <h1>${EachObject.name}</h1>
    <p>${EachObject.value}</p>
  </div>`
    );
  });
console.log(AllSelects)
  AllSelects.forEach((EachObject) => {
    document.querySelector(".confirmation_area").insertAdjacentHTML(
      "beforeend",
      ` <div class="box">
    <h1>${EachObject.name}</h1>
    <p>${EachObject[EachObject.selectedIndex].innerHTML}</p>
  </div>`
    );
  });
};

const NavigateNext = (e) => {
  e.preventDefault();

  window.scrollTo(window.pageYOffset, 0);

  if (Steps.currentStep < 3) {
    BodyArea.querySelector(`.step${Steps.currentStep}`).style.display = "none";
    Steps.currentStep++;
    BodyArea.querySelector(`.step${Steps.currentStep}`).style.display = "block";
    document.querySelector(
      `.header-form-area .mbl-step`
    ).textContent = `Step ${Steps.currentStep}`;
  }

  if (Steps.currentStep == 2) {
    Buttons.prevButton.style.display = "block";
    let FooterArea = document.querySelector(".footer-form-area");
    FooterArea.style.justifyContent = "space-between";
  }
  if (Steps.currentStep == 3) {
    Buttons.nextButton.style.display = "none";
    Buttons.submitButton.style.display = "block";

    GetFormValues();
  }

  Steps["StepsContainer"]
    .querySelector(`#step-list${Steps.currentStep}`)
    .classList.add("active");
};
const NavigateBack = (e) => {
  e.preventDefault();

  window.scrollTo(window.pageYOffset, 0);
  if (Steps.currentStep > 1) {
    Steps["StepsContainer"]
      .querySelector(`#step-list${Steps.currentStep}`)
      .classList.remove("active");

    BodyArea.querySelector(`.step${Steps.currentStep}`).style.display = "none";
    Steps.currentStep--;
    BodyArea.querySelector(`.step${Steps.currentStep}`).style.display = "block";
    document.querySelector(
      `.header-form-area .mbl-step`
    ).textContent = `Step ${Steps.currentStep}`;
  }

  if (Steps.currentStep == 2) {
    Buttons.nextButton.style.display = "block";
    Buttons.submitButton.style.display = "none";
  }
  if (Steps.currentStep == 1) {
    Buttons.prevButton.style.display = "none";
    let FooterArea = document.querySelector(".footer-form-area");
    FooterArea.style.justifyContent = "flex-end";
  }
};

function Submit () {
    const form = document.querySelector("#test")
    console.log(form)
    form.submit()

};

Buttons.nextButton.addEventListener("click", NavigateNext);
Buttons.prevButton.addEventListener("click", NavigateBack);
Buttons.submitButton.addEventListener("click", Submit);