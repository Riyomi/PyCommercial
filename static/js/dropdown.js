function openMenu() {
    document.getElementById("myDropDown").classList.toggle('hidden');
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.closest('#dropbtn')) {
      const dropdowns = document.getElementsByClassName("dropdown-content");
      for (let i = 0; i < dropdowns.length; i++) {
          const openDropdown = dropdowns[i];
          if (!openDropdown.classList.contains('hidden')) {
            openDropdown.classList.add('hidden');
          }
    }
  }
 }