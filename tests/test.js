function assertEqual(a, b, msg) {
  if (a !== b) throw new Error(msg + ` | expected ${b}, got ${a}`);
}
function assertTrue(cond, msg) {
  if (!cond) throw new Error(msg);
}
function log(s) {
  document.getElementById("out").textContent += s + "\n";
}
(function run() {
  const p0 = 8000000;
  const r = 0.012;
  const n = 36;
  const final = compound(p0, r, n);
  assertTrue(final > p0, "Final should be greater than initial");
  const series = monthlySeries(p0, r, n);
  assertEqual(series.length, n, "Series length mismatch");
  for (let i = 1; i < series.length; i++) {
    assertTrue(
      series[i].g >= series[i - 1].g,
      "Geometric should be non-decreasing",
    );
    assertTrue(
      series[i].a >= series[i - 1].a,
      "Arithmetic should be non-decreasing",
    );
  }
  const dup = duplicationMonthsIterative(p0, r);
  assertTrue(dup.months > 0, "Duplication months should be positive");
  const target = roundCents(p0 * 2);
  assertTrue(
    roundCents(series[dup.months - 1].g) >= target,
    "Duplication reached",
  );
  log("All tests passed");
})();
