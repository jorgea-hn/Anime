const switchText = document.getElementById('switch-text');
const switchInput = document.querySelector('.switch input');

switchInput.addEventListener('change', function() {
  if (this.checked) {
    switchText.textContent = 'Visto';
  } else {
    switchText.textContent = 'Pendiente';
  }
});