

function updateSlider(slider) {
    const valueId = slider.dataset.valueId;
    if (valueId) {
        document.getElementById(valueId).innerText = slider.value;
    }
}



document.addEventListener("DOMContentLoaded", () => {
    const sliders = document.querySelectorAll("input[type='range']");
    sliders.forEach(slider => {
        
        updateSlider(slider);

        slider.addEventListener("input", () => updateSlider(slider));
    });
});


function toggleInfo() {
    const box = document.getElementById("info-content");
    box.style.display = box.style.display === "block" ? "none" : "block";
}


function showLoader() {
    const loader = document.getElementById("loader");
    loader.style.display = "block";
}


function validateForm() {
    const validations = [
        {id: "ageSlider", min: 1, max: 120, name: "Age"},
        {id: "bpSlider", min: 50, max: 250, name: "Resting BP"},
        {id: "cholSlider", min: 50, max: 700, name: "Cholesterol"},
        {id: "hrSlider", min: 50, max: 250, name: "Max Heart Rate"},
        {id: "oldpeakSlider", min: 0, max: 10, name: "Oldpeak"},
        {id: "caSlider", min: 0, max: 4, name: "Major Vessels (ca)"}
    ];

    for (let v of validations) {
        const value = parseFloat(document.getElementById(v.id).value);
        if (value < v.min || value > v.max) {
            alert(`${v.name} must be between ${v.min} and ${v.max}`);
            return false;
        }
    }

    return true;
}


document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("heart-form");
    form.addEventListener("submit", (e) => {
        if (!validateForm()) {
            e.preventDefault(); 
            return;
        }
        showLoader(); 
    });
});

