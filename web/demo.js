// ---------------- SLOT COUNT ----------------
async function updateSlots() {
  const res = await fetch("http://127.0.0.1:8000/slots/status");
  const data = await res.json();
  document.getElementById("slotCount").innerText =
    `Available Slots: ${data.free_slots} / ${data.total_slots}`;
}

setInterval(updateSlots, 2000);
updateSlots();

// ---------------- VIDEO (PLAY ONCE) ----------------
const parkingVideo = document.getElementById("parkingVideo");
parkingVideo.addEventListener("ended", () => {
  parkingVideo.pause();
});

// ---------------- DEMO CAR PARK AFTER 6s ----------------
setTimeout(() => {
  fetch("http://127.0.0.1:8000/demo/car-parked", { method: "POST" });
}, 6000);

// ---------------- GENERATE TICKET ----------------
async function generateTicket() {
  const email = document.getElementById("email").value;
  if (!email) {
    alert("Please enter email");
    return;
  }

  await fetch("http://127.0.0.1:8000/ticket/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email })
  });

  document.getElementById("status").innerText =
    "✅ Ticket generated and sent to email";
}

// ---------------- QR SCAN (WEBCAM VISIBLE) ----------------
async function startQR() {
  console.log("▶ Release Ticket clicked");

  const qrSection = document.getElementById("qrSection");
  const video = document.getElementById("qrVideo");
  const status = document.getElementById("status");

  qrSection.style.display = "block";
  status.innerText = "📷 Show QR code to camera...";

  let stream;
  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: true });
  } catch (err) {
    alert("Camera permission denied");
    return;
  }

  video.srcObject = stream;

  const canvas = document.createElement("canvas");
  const ctx = canvas.getContext("2d");

  const scanInterval = setInterval(async () => {
    if (video.readyState !== video.HAVE_ENOUGH_DATA) return;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);

    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const code = jsQR(imageData.data, canvas.width, canvas.height);

    if (code) {
      console.log("✅ QR detected:", code.data);

      // Stop scanning
      clearInterval(scanInterval);
      stream.getTracks().forEach(t => t.stop());
      qrSection.style.display = "none";

      // Call backend to release ticket
      await fetch("http://127.0.0.1:8000/ticket/release", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticket_id: code.data })
      });

      // ✅ USER FEEDBACK
      status.innerText = "✅ Ticket released successfully. Slot is now free.";

      // ✅ IMMEDIATE SLOT COUNT UPDATE
      updateSlots();
    }
  }, 400);
}

// ---------------- RESET SLOTS ----------------
async function resetSlots() {
  await fetch("http://127.0.0.1:8000/admin/reset-slots", { method: "POST" });
  alert("All slots reset");
}
