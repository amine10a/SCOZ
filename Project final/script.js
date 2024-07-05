document.addEventListener("DOMContentLoaded", function() {
    // Add mouseover and mouseleave events to highlight countries on hover
    document.querySelectorAll(".allPaths").forEach(e => {
        e.setAttribute('class', `allPaths ${e.id}`);
        e.addEventListener("mouseover", function () {
            window.onmousemove = function (j) {
                const x = j.clientX;
                const y = j.clientY;
                document.getElementById('name').style.top = (y - 60) + 'px';
                document.getElementById('name').style.left = (x - 80) + 'px';
            }

            const classes = e.className.baseVal.replace(/ /g, '.');
            document.querySelectorAll(`.${classes}`).forEach(country => {
                country.style.fill = "#BF0606"; // Highlight with active color on hover
            });
            document.getElementById("name").style.opacity = 1;
            document.getElementById("namep").innerText = e.id; // Display country name
        });

        e.addEventListener("mouseleave", function () {
            const classes = e.className.baseVal.replace(/ /g, '.');
            document.querySelectorAll(`.${classes}`).forEach(country => {
                if (!country.classList.contains('active')) {
                    country.style.fill = ""; // Reset fill on mouse leave if not active
                }
            });
            document.getElementById("name").style.opacity = 0;
        });

        e.addEventListener("click", function () {
            // Remove previous active class from all paths
            document.querySelectorAll('.allPaths').forEach(p => {
                p.classList.remove('active');
                p.style.fill = ""; // Reset all paths to default fill color
            });

            // Add active class to the clicked path
            this.classList.add('active');

            // Set fill color to active color (#BF0606) for the clicked path
            this.style.fill = "#BF0606";

            // Get the country name from the ID
            const countryName = this.getAttribute('id');

            // Update the country title text
            const countryTitle = document.querySelector('.countrytitle');
            countryTitle.textContent = countryName;

            // Adjust UI as needed
            document.querySelector(".world-1").style.width = "50%";
            document.querySelector(".inputs").classList.add("active");
            document.querySelector(".frame-7").classList.add("active");
        });
    });
});


// Get the button and modal elements
const generateButton = document.getElementById('generateButton');
const loadingModal = document.getElementById('loadingModal');

// Add event listener to the button
generateButton.addEventListener('click', function() {
    // Show the loading modal
    loadingModal.style.display = 'block';

    // Simulate loading process (remove this in actual use)
    setTimeout(function() {
        // Hide the loading modal after a delay (simulating loading completion)
        loadingModal.style.display = 'none';
    }, 3000); // Example: 3000 milliseconds (3 seconds) for loading simulation
});

// Get the download button element
const downloadButton = document.getElementById('downloadButton');

// Add event listener to the download button
downloadButton.addEventListener('click', function() {
    // Simulate file download (replace with actual download logic)
    alert('Simulating file download...');
});

// Add event listener to the generate button
generateButton.addEventListener('click', function() {
    // Show the loading modal
    loadingModal.style.display = 'block';

    // Simulate loading process (remove this in actual use)
    setTimeout(function() {
        // Hide the loading modal
        loadingModal.style.display = 'none';

        // Show the success modal
        successModal.style.display = 'block';
    }, 3000); // Example: 3000 milliseconds (3 seconds) for loading simulation
});
// Get the close icon element
const closeIcon = document.querySelector('#successModal .close');

// Add event listener to the close icon
closeIcon.addEventListener('click', function() {
    successModal.style.display = 'none';
});