function roundCents(x) {
  return Math.round(x * 100) / 100;
}
function formatCOP(x) {
  return new Intl.NumberFormat("es-CO", {
    style: "currency",
    currency: "COP",
    minimumFractionDigits: 2,
  }).format(x);
}
function compound(p0, r, n) {
  return roundCents(p0 * Math.pow(1 + r, n));
}
function arithmetic(p0, r, n) {
  return roundCents(p0 + n * roundCents(p0 * r));
}
function monthlySeries(p0, r, months) {
  const series = [];
  for (let m = 1; m <= months; m++)
    series.push({ m, g: compound(p0, r, m), a: arithmetic(p0, r, m) });
  return series;
}
function duplicationMonthsLog(p0, r) {
  return Math.log(2) / Math.log(1 + r);
}
function duplicationMonthsIterative(p0, r) {
  const target = p0 * 2;
  let m = 0;
  let v = p0;
  const steps = [];
  while (roundCents(v) < roundCents(target)) {
    m++;
    v = v * (1 + r);
    steps.push({ m, v: roundCents(v) });
    if (m > 10000) break;
  }
  return { months: m, steps };
}
function validateInputs(p0, r, months) {
  const errors = [];
  if (!Number.isFinite(p0) || p0 <= 0)
    errors.push("El capital inicial debe ser mayor a 0.");
  if (p0 > 100000000)
    errors.push("El capital inicial no puede exceder 100.000.000.");
  if (!Number.isFinite(r) || r <= 0) errors.push("La tasa debe ser mayor a 0.");
  if (r > 1) errors.push("La tasa no puede ser mayor que 1 (100%).");
  if (!Number.isInteger(months) || months < 1)
    errors.push("Los meses deben ser un entero mayor o igual a 1.");
  if (months > 600) errors.push("Los meses no pueden exceder 600.");
  return errors;
}
function renderTable(series) {
  const tbody = document.querySelector("#table tbody");
  tbody.innerHTML = "";
  for (const row of series) {
    const tr = document.createElement("tr");
    const tds = [row.m.toString(), formatCOP(row.g), formatCOP(row.a)];
    for (const t of tds) {
      const td = document.createElement("td");
      td.textContent = t;
      tr.appendChild(td);
    }
    tbody.appendChild(tr);
  }
}
function exportCsv(p0, r, months) {
  const series = monthlySeries(p0, r, months);
  let csv = "Mes,Geométrico,Aritmético\n";
  for (const row of series)
    csv += `${row.m},${row.g.toFixed(2)},${row.a.toFixed(2)}\n`;
  const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "tabla_crecimiento.csv";
  a.click();
  URL.revokeObjectURL(url);
}
function drawChart(p0, r, interval) {
  const canvas = document.getElementById("chart");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const padding = 40;
  const w = canvas.width;
  const h = canvas.height;
  const series = monthlySeries(p0, r, interval);
  const maxVal = Math.max(...series.map((s) => Math.max(s.g, s.a)));
  function x(i) {
    return padding + (i / interval) * (w - 2 * padding);
  }
  function y(val) {
    return h - padding - (val / maxVal) * (h - 2 * padding);
  }
  ctx.strokeStyle = "#334155";
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(padding, padding);
  ctx.lineTo(padding, h - padding);
  ctx.lineTo(w - padding, h - padding);
  ctx.stroke();
  ctx.fillStyle = "#94a3b8";
  ctx.textAlign = "center";
  ctx.font = "12px system-ui";
  for (let i = 0; i <= interval; i += Math.max(1, Math.floor(interval / 6))) {
    const xi = x(i);
    ctx.fillText(i.toString(), xi, h - padding + 14);
  }
  ctx.strokeStyle = "#22c55e";
  ctx.lineWidth = 2;
  ctx.beginPath();
  series.forEach((s, i) => {
    const xi = x(i + 1);
    const yi = y(s.g);
    if (i === 0) ctx.moveTo(xi, yi);
    else ctx.lineTo(xi, yi);
  });
  ctx.stroke();
  ctx.strokeStyle = "#3b82f6";
  ctx.lineWidth = 2;
  ctx.beginPath();
  series.forEach((s, i) => {
    const xi = x(i + 1);
    const yi = y(s.a);
    if (i === 0) ctx.moveTo(xi, yi);
    else ctx.lineTo(xi, yi);
  });
  ctx.stroke();
  ctx.fillStyle = "#94a3b8";
  ctx.fillText("Geométrico", w - padding - 80, padding + 12);
  ctx.fillStyle = "#94a3b8";
  ctx.fillText("Aritmético", w - padding - 80, padding + 28);
  ctx.fillStyle = "#22c55e";
  ctx.fillRect(w - padding - 150, padding + 2, 10, 2);
  ctx.fillStyle = "#3b82f6";
  ctx.fillRect(w - padding - 150, padding + 18, 10, 2);
}
function computeAll() {
  const p0 = Number(document.getElementById("capital").value);
  const r = Number(document.getElementById("rate").value);
  const months = Number(document.getElementById("months").value);
  const errors = validateInputs(p0, r, months);
  const validation = document.getElementById("validation");
  if (errors.length) {
    validation.textContent = errors.join(" ");
    return;
  }
  validation.textContent = "";
  const final = compound(p0, r, months);
  document.getElementById("finalAmount").textContent = formatCOP(final);
  const dupLog = duplicationMonthsLog(p0, r);
  const dupIter = duplicationMonthsIterative(p0, r);
  document.getElementById("dupMonths").textContent = `${dupIter.months} meses`;
  const detail = [
    `Objetivo: ${formatCOP(roundCents(p0 * 2))}`,
    `Logaritmos: n = ln(2) / ln(1 + r) = ${dupLog.toFixed(6)} meses`,
    `Iterativo: mínimo entero = ${dupIter.months} meses`,
  ];
  document.getElementById("dupDetails").innerHTML = detail.join("<br>");
  renderTable(monthlySeries(p0, r, months));
  drawChart(p0, r, months);
}
document.getElementById("compute").addEventListener("click", computeAll);
document.getElementById("exportCsv").addEventListener("click", () => {
  const p0 = Number(document.getElementById("capital").value);
  const r = Number(document.getElementById("rate").value);
  const months = Number(document.getElementById("months").value);
  const errors = validateInputs(p0, r, months);
  if (errors.length) {
    document.getElementById("validation").textContent = errors.join(" ");
    return;
  }
  exportCsv(p0, r, months);
});
document
  .getElementById("printPdf")
  .addEventListener("click", () => window.print());
document.querySelectorAll(".intervals button").forEach((b) => {
  b.addEventListener("click", () => {
    document
      .querySelectorAll(".intervals button")
      .forEach((x) => x.classList.remove("active"));
    b.classList.add("active");
    const p0 = Number(document.getElementById("capital").value);
    const r = Number(document.getElementById("rate").value);
    const interval = Number(b.dataset.interval);
    const errors = validateInputs(p0, r, interval);
    if (errors.length) {
      document.getElementById("validation").textContent = errors.join(" ");
      return;
    }
    drawChart(p0, r, interval);
  });
});
computeAll();
