const slotButtons = document.querySelectorAll(".slot-buttons button");
const soloModal = document.getElementById("soloModal");
const soloClose = document.getElementById("soloClose");
const slotInput = document.getElementById("slotInput");
const modalTitle = document.getElementById("modalTitle");

slotButtons.forEach(btn => {
  btn.addEventListener("click", () => {
    const slot = btn.textContent;
    slotInput.value = slot;
    modalTitle.textContent = `Solo Registration - ${slot}`;
    soloModal.style.display = "flex";
  });
});

soloClose.addEventListener("click", () => {
  soloModal.style.display = "none";
});

window.addEventListener("click", (e) => {
  if (e.target === soloModal) {
    soloModal.style.display = "none";
  }
});
