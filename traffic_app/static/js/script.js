// ===== FILE UPLOAD PREVIEW =====
function previewVideo(event) {
    const file = event.target.files[0];
    const videoPreview = document.getElementById("videoPreview");
    const videoPreviewContainer = document.getElementById("videoPreviewContainer");
    const dropZone = document.getElementById("dropZone");

    if (file) {
        const url = URL.createObjectURL(file);
        videoPreview.src = url;
        videoPreviewContainer.style.display = "block";
        // Add file name to drop zone when file is selected
        dropZone.querySelector('.drop-zone-content h5').textContent = file.name;
        dropZone.querySelector('.drop-zone-content p').textContent = (file.size / (1024 * 1024)).toFixed(2) + " MB";
    }
}

// ===== DRAG AND DROP HANDLERS =====
const dropZone = document.getElementById("dropZone");
const videoInput = document.getElementById("videoInput");

if (dropZone && videoInput) {
    dropZone.addEventListener("dragover", function(e) {
        e.preventDefault();
        dropZone.classList.add("dragover");
    });

    dropZone.addEventListener("dragleave", function() {
        dropZone.classList.remove("dragover");
    });

    dropZone.addEventListener("drop", function(e) {
        e.preventDefault();
        dropZone.classList.remove("dragover");
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            videoInput.files = files;
            // Trigger the change event
            const event = new Event("change", { bubbles: true });
            videoInput.dispatchEvent(event);
        }
    });
}

// ===== SHOW LOADER ON SUBMIT =====
function showLoader() {
    const loaderOverlay = document.getElementById("loaderOverlay");
    if (loaderOverlay) {
        loaderOverlay.style.display = "flex";
    }
}

// ===== AUTO REFRESH DASHBOARD =====
function autoRefresh() {
    setInterval(() => {
        location.reload();
    }, 10000); // refresh every 10 seconds
}

// ===== ALERT FOR ANOMALY =====
function checkAnomaly(isAnomaly) {
    if (isAnomaly === "True") {
        alert("⚠️ Anomaly Detected in Traffic!");
    }
}

// ===== CHART (OPTIONAL) =====
function renderChart(vehicleCount) {
    const ctx = document.getElementById('trafficChart');

    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Vehicles'],
            datasets: [{
                label: 'Vehicle Count',
                data: [vehicleCount],
            }]
        }
    });
}
