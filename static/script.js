document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let fileInput = document.getElementById("imageUpload");
    let file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }
    
    let formData = new FormData();
    formData.append("filename", file.name);
    
    fetch("/upload", {
        method: "POST",
        body: JSON.stringify({ filename: file.name }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            let output = `Detected Device: ${data.detected_devices[0].device}\nRecycling Info: ${JSON.stringify(data.detected_devices[0].recycling_methods)}`;
            document.getElementById("result").innerText = output;
            document.getElementById("uploaded-image").src = data.image_url;
        }
    })
    .catch(error => console.error("Error:", error));
});
