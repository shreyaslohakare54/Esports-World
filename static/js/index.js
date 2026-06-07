// Show Sign In modal on first visit
window.addEventListener('DOMContentLoaded', () => {
  const signedIn = localStorage.getItem('signedIn');
  if (!signedIn) {
    openSignIn();
  }
});

// Open sign in modal
function openSignIn() {
  document.getElementById('signinModal').style.display = 'flex';
}

// Close sign in modal
function closeSignIn() {
  document.getElementById('signinModal').style.display = 'none';
  localStorage.setItem('signedIn', 'true');
}

// Close modal on clicking outside content
window.onclick = function(event) {
  const modal = document.getElementById('signinModal');
  if (event.target === modal) {
    closeSignIn();
  }
}

// Event listeners
document.getElementById('signinBtn').addEventListener('click', openSignIn);
document.getElementById('signinClose').addEventListener('click', closeSignIn);

// Scroll to tournaments section
function scrollToTournaments() {
  document.getElementById('tournaments').scrollIntoView({ behavior: 'smooth' });
}
