const sparkBars = document.querySelectorAll(".spark-bars");

sparkBars.forEach((node) => {
  const values = node.dataset.values.split(",").map(Number);
  const labels = node.dataset.labels.split(",");
  const max = Math.max(...values, 1);
  node.innerHTML = "";
  values.forEach((value, index) => {
    const bar = document.createElement("div");
    bar.style.height = `${Math.max(8, (value / max) * 128)}px`;
    bar.title = `${labels[index]}: ${value}`;
    const label = document.createElement("span");
    label.textContent = labels[index];
    bar.appendChild(label);
    node.appendChild(bar);
  });
});

