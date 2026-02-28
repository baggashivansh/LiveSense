async function checkHealth() {
    const statusText = document.getElementById("statusText");
    const dot = document.getElementById("dot");
    const button = document.getElementById("checkBtn");

    statusText.innerText = "Checking...";
    dot.style.background = "#9ca3af";
    button.disabled = true;

    try {
        const response = await fetch("https://livesense-backend.onrender.com/");

        if (!response.ok) throw new Error();

        const data = await response.json();

        if (data.status === "UP") {
            statusText.innerText = "Online";
            dot.style.background = "#10b981";
        } else {
            statusText.innerText = "Unexpected";
            dot.style.background = "#f59e0b";
        }

    } catch (error) {
        statusText.innerText = "Offline";
        dot.style.background = "#ef4444";
    }

    button.disabled = false;
}