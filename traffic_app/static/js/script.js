// ===== FILE UPLOAD PREVIEW =====
function previewVideo(event) {
    const file = event.target.files[0];
    const videoPreview = document.getElementById("videoPreview");

    if (file) {
        const url = URL.createObjectURL(file);
        videoPreview.src = url;
        videoPreview.style.display = "block";
    }
}

// ===== SHOW LOADER ON SUBMIT =====
function showLoader() {
    document.getElementById("loader").style.display = "block";
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
