const searchSection = document.querySelector(".search");
const popupShow_button = searchSection.querySelector(".button-form-show");
const searchPopup = searchSection.querySelector(".modal");
const searchForm = searchPopup.querySelector(".search-form");
const searchForm_interactive = searchForm.querySelectorAll("[name]")
const dateIn = searchForm.querySelector("[name=date-in]");
const dateOut = searchForm.querySelector("[name=date-out]");
const adults = searchForm.querySelector("[name=adults]");
const kids = searchForm.querySelector("[name=kids]");
const adultsMinus_button = searchForm.querySelector(".button-adults-minus");
const adultsPlus_button = searchForm.querySelector(".button-adults-plus");
const kidsMinus_button = searchForm.querySelector(".button-kids-minus");
const kidsPlus_button = searchForm.querySelector(".button-kids-plus");
let isStorageSupport = true;
let storageAdults_count = "";
let storageKids_count = "";

searchPopup.classList.add("modal-close")

try {
  storageAdults_count = localStorage.getItem("adults");
  storageKids_count = localStorage.getItem("kids");
} catch (err) {
  isStorageSupport = false;
}

if (storageAdults_count) {
  adults.value = storageAdults_count;
}
if (storageKids_count) {
  kids.value = storageKids_count;
}

popupShow_button.addEventListener("click", function(evt) {
  evt.preventDefault();
  if (searchPopup.classList.contains("modal-error")) {
    searchPopup.classList.remove("modal-error");
  }

  searchPopup.classList.toggle("modal-open");
  searchPopup.classList.toggle("modal-close");

  if (searchPopup.classList.contains("modal-open")) {
    for (var i = 0; i < searchForm_interactive.length; i++) {
      let searchForm_interactive_item = searchForm_interactive[i];
      searchForm_interactive_item.setAttribute("tabindex", 0);
    }
    dateIn.focus();
  }

  if (searchPopup.classList.contains("modal-close")) {
    for (var i = 0; i < searchForm_interactive.length; i++) {
      let searchForm_interactive_item = searchForm_interactive[i];
      searchForm_interactive_item.setAttribute("tabindex", -1);
    }
  }
});

searchForm.addEventListener("submit", function(evt) {
  if (!dateIn.value || !dateOut.value || !adults.value || !kids.value) {
    evt.preventDefault();
    searchPopup.classList.remove("modal-error");
    searchPopup.offsetWidth = searchPopup.offsetWidth;
    searchPopup.classList.add("modal-error");
  }else{
    if (isStorageSupport) {
    localStorage.setItem("adults", adults.value);
    localStorage.setItem("kids", kids.value);
  }
}
});

adultsMinus_button.addEventListener("click", function(evt) {
  evt.preventDefault();
  if (!adults.value) {
    adults.value = 0;
  }
  let result = parseInt(adults.value, 10)-1;
  if (result>=0) {
    adults.value = result;
  }
});

adultsPlus_button.addEventListener("click", function(evt) {
  evt.preventDefault();
  if (!adults.value) {
    adults.value = 0;
  }
  adults.value = parseInt(adults.value, 10)+1;
});

kidsMinus_button.addEventListener("click", function(evt) {
  evt.preventDefault();
  if (!kids.value) {
    kids.value = 0;
  }
  let result = parseInt(kids.value, 10)-1;
  if (result>=0) {
    kids.value = result;
  }
});

kidsPlus_button.addEventListener("click", function(evt) {
  evt.preventDefault();
  if (!kids.value) {
    kids.value = 0;
  }
  kids.value = parseInt(kids.value, 10)+1;
});
