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
            };

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

            // Update websites based on selected country
            updateWebsites(countryName);
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
});

// DYNAMIC FORM

const countryWebsites = {
    Germany: [
        { value: 'versteigerungskalender', text: 'www.versteigerungskalender.de' },
        { value: 'Insolvenzbekanntmachungen', text: 'www.Insolvenzbekanntmachungen.de' },
        { value: 'dealone', text: 'www.deal-one.de' },
    ],
    usa: [
        { value: 'us-site1', text: 'www.us-site1.com' },
        { value: 'us-site2', text: 'www.us-site2.com' }
    ],
    france: [
        { value: 'fr-site1', text: 'www.fr-site1.fr' },
        { value: 'fr-site2', text: 'www.fr-site2.fr' }
    ]
};

const siteInputs = {
    versteigerungskalender: `
    
        <div class="input-field">
                    <label for="sector">Filter by sector:</label>
                    <select name="sectors[]" id="sector" class="choose-sector" multiple="multiple">
                        <option value=""></option>
                        <option value="40098">Agriculture & Animals</option>
                        <option value="40142">Architects & Planning Offices</option>
                        <option value="40116">Automotive & Bikes</option>
                        <option value="40100">Ancillary construction trades</option>
                        <option value="40102">Contractors</option>
                        <option value="40106">Office & IT Services</option>
                        <option value="40108">Chemicals, Plastics, Paints</option>
                        <option value="40110">Printing & Publishing</option>
                        <option value="40112">Retail, Wholesale & Online Trade</option>
                        <option value="40114">Energy & Environment</option>
                        <option value="40118">Financial Services & Private Equity Firms</option>
                        <option value="40104">Research & Education</option>
                        <option value="40122">Garden & Landscaping</option>
                        <option value="40124">Glass</option>
                        <option value="40128">Craft</option>
                        <option value="40130">House Services</option>
                        <option value="40132">Woodworking & Trade</option>
                        <option value="40134">Hotel & Gastronomy, Food Production</option>
                        <option value="40136">Real estate</option>
                        <option value="40138">Import/Export</option>
                        <option value="40140">Industry</option>
                        <option value="40144">Cosmetics & Studios</option>
                        <option value="40148">Art & Culture</option>
                        <option value="99867">Mechanical engineering</option>
                        <option value="40152">Medicine & Care</option>
                        <option value="40154">Personnel services</option>
                        <option value="40156">Security service</option>
                        <option value="40160">Sports & Leisure</option>
                        <option value="40162">Steel & Metal</option>
                        <option value="40164">Textile trade and production</option>
                        <option value="40166">Tourism & Travel</option>
                        <option value="40168">Transport & Logistics</option>
                        <option value="40174">Car Washes & Cleaning</option>
                        <option value="40176">Advertising & Marketing</option>
                    </select>
                </div>
                <div class="input-field">
                    <label for="keywords">Keywords:</label>
                    <input type="text" id="keywords" name="keywords" placeholder="Enter keywords">
                </div>
    `,
    'Insolvenzbekanntmachungen': `
         
                    <div id="dynamic-inputs">
                        <div class="input-field">
                            
                            <input type="text" id="keywords" name="keywords" placeholder="Enter keywords">
                        </div>
                        <div class="input-field">
                            
                            <input type="date" id="dateStart" name="dateStart" placeholder="Start Date">
                        </div>
                        <div class="input-field">
                            
                            <input type="date" id="dateEnd" name="dateEnd" placeholder="End Date">
                        </div>
                    </div>>
    `,
    'dealone': `
                <div class="input-field">
                    <label for="keywords">Keywords:</label>
                    <input type="text" id="keywords" name="keywords" placeholder="Enter keywords">
                </div>
    `,
    'us-site2': `
        <div class="input-field">
            <label for="service">Service:</label>
            <input type="text" id="service" name="service" placeholder="Enter service">
        </div>
    `,
    'fr-site1': `
        <div class="input-field">
            <label for="sector">Sector:</label>
            <input type="text" id="sector" name="sector" placeholder="Enter sector">
        </div>
    `,
    'fr-site2': `
        <div class="input-field">
            <label for="location">Location:</label>
            <input type="text" id="location" name="location" placeholder="Enter location">
        </div>
    `
};

function updateWebsites(selectedCountry) {
    const siteSelect = document.getElementById('site');
    const dynamicInputs = document.getElementById('dynamic-inputs');
    siteSelect.innerHTML = '<option value="" selected disabled>Choose Website</option>';

    if (selectedCountry && countryWebsites[selectedCountry]) {
        countryWebsites[selectedCountry].forEach(site => {
        if(site.value){
            const option = document.createElement('option');
            option.value = site.value;
            option.textContent = site.text;
            siteSelect.appendChild(option);
            option.click=formin()
        }
        else{
            const option = document.createElement('option');
            option.value = site.value;
            option.textContent = site.text;
            siteSelect.appendChild(option);
        }
    })

    // Clear dynamic inputs when country changes
    dynamicInputs.innerHTML = '';
}}
function formin(){
    document.getElementById('site').addEventListener('change', function() {
        const selectedSite = this.value;
        const dynamicInputs = document.getElementById('dynamic-inputs');
        dynamicInputs.innerHTML = '';
    
        if (selectedSite && siteInputs[selectedSite]) {
            dynamicInputs.innerHTML = siteInputs[selectedSite];
        }
    });
    
}


function toggleTable() {
    const table = document.getElementById('table');
    table.style.display = table.style.display === 'none' ? 'block' : 'none';
}

// Simulate selecting a country
const countryTitle = document.querySelector('.countrytitle').textContent.trim();
updateWebsites(countryTitle);


function closeModal() {
    modall.style.display = 'none';
}
