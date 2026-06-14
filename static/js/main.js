// ── Tone Selection ──
let selectedTone = "Professional";

document.querySelectorAll(".tone-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tone-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    selectedTone = btn.dataset.tone;
  });
});

// ── Character Counter ──
const topicInput = document.getElementById("topic");
topicInput.addEventListener("input", () => {
  document.getElementById("char-count").textContent = topicInput.value.length + " / 200";
});

// ── Agent Step Helpers ──
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

function setStep(n, state) {
  // state: "pending" | "active" | "done"
  const el = document.getElementById("step" + n);
  if (!el) return;
  el.className = "step " + state;
}

async function animateSteps() {
  for (let i = 1; i <= 4; i++) setStep(i, "pending");

  setStep(1, "active");
  await sleep(700);
  setStep(1, "done"); setStep(2, "active");
  await sleep(600);
  setStep(2, "done"); setStep(3, "active");
  await sleep(500);
  setStep(3, "done"); setStep(4, "active");
}

// ── Generate Post ──
async function generatePost() {
  const topic    = topicInput.value.trim();
  const language = document.getElementById("language").value;
  const errEl    = document.getElementById("error-msg");

  errEl.textContent = "";

  if (!topic) {
    errEl.textContent = "Please enter a topic for your post.";
    return;
  }

  // Disable button
  const genBtn = document.getElementById("gen-btn");
  genBtn.disabled = true;
  genBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Generating…';

  // Show agent steps
  document.getElementById("empty-state").style.display  = "none";
  document.getElementById("linkedin-card").style.display = "none";
  document.getElementById("action-row").style.display   = "none";
  document.getElementById("agent-steps").style.display  = "block";

  // Start step animation (runs independently)
  animateSteps();

  try {
    const res = await fetch("/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic, language, tone: selectedTone }),
    });

    const data = await res.json();

    if (!res.ok) {
      errEl.textContent = data.error || "Something went wrong. Please try again.";
      document.getElementById("agent-steps").style.display = "none";
      document.getElementById("empty-state").style.display = "flex";
      return;
    }

    // Mark all steps done
    for (let i = 1; i <= 4; i++) setStep(i, "done");
    await sleep(400);

    // Show result
    document.getElementById("agent-steps").style.display  = "none";
    document.getElementById("lk-body").textContent        = data.post;
    document.getElementById("linkedin-card").style.display = "block";
    document.getElementById("action-row").style.display   = "flex";
    document.getElementById("meta-info").textContent      = `${data.word_count} words · ${data.language} · ${data.tone}`;

  } catch (err) {
    errEl.textContent = "Network error. Please try again.";
    document.getElementById("agent-steps").style.display = "none";
    document.getElementById("empty-state").style.display = "flex";
  } finally {
    genBtn.disabled = false;
    genBtn.innerHTML = '<i class="fa-solid fa-wand-magic-sparkles"></i> Generate Post';
  }
}

// ── Copy Post ──
async function copyPost() {
  const text = document.getElementById("lk-body").textContent;
  if (!text) return;
  try {
    await navigator.clipboard.writeText(text);
    const btn = document.querySelector(".act-btn");
    btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
    setTimeout(() => { btn.innerHTML = '<i class="fa-regular fa-copy"></i> Copy Post'; }, 2000);
  } catch (e) {
    alert("Copy failed. Please select and copy manually.");
  }
}

// ── Enter key shortcut ──
topicInput.addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); generatePost(); }
});
