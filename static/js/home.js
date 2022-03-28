const BurgerIcon = document.querySelector(".burger-menu");
const HandleSideBar = (e) => {
  document.querySelector(".nav_side").classList.toggle("active");
};

BurgerIcon.addEventListener("click", HandleSideBar);
