/* When the user clicks on the button,
        toggle between hiding and showing the dropdown content */
        
        function open_dropdown_option() {
            document.getElementsByClassName("dropdown-options")[0].classList.toggle("show");
            }
    
            // Close the dropdown menu if the user clicks outside of it
            window.onclick = function(event) {
            if (!event.target.matches('.option-button')) {
                var dropdown = document.getElementsByClassName("dropdown-options")[0];
               
                if (dropdown.classList.contains('show')) {
                    dropdown.classList.remove('show');
                }
                
            }
            }