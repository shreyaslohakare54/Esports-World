const slotButtons = document.querySelectorAll(".slot-buttons button");
const squadModal = document.getElementById("squadModal");
const squadClose = document.getElementById("squadClose");
const slotInput = document.getElementById("slotInput");
const modalTitle = document.getElementById("modalTitle");

const bigModal = document.getElementById("bigModal");
const bigClose = document.getElementById("bigClose");

slotButtons.forEach(btn => {
  btn.addEventListener("click", () => {
    if (btn.id === "bigTournament") {
      // Show big tournament modal locked message
      bigModal.style.display = "flex";
    } else {
      // Open registration modal for 6pm or 9pm
      const slot = btn.textContent;
      slotInput.value = slot;
      modalTitle.textContent = `Squad Registration - ${slot}`;
      squadModal.style.display = "flex";
    }
  });
});

squadClose.addEventListener("click", () => {
  squadModal.style.display = "none";
});

bigClose.addEventListener("click", () => {
  bigModal.style.display = "none";
});

window.addEventListener("click", (e) => {
  if (e.target === squadModal) squadModal.style.display = "none";
  if (e.target === bigModal) bigModal.style.display = "none";
});
