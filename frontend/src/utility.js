const colorSpectrum = [
  "rgb(250, 0, 0)", // red
  "rgb(240, 22, 54, 0.7)",
  "rgb(245, 51, 80, 0.7)", // first red
  "rgb(9, 235, 17, 0.7)",
  "rgb(75, 250, 78, 0.9)",
  "rgb(75, 250, 78, 0.7)", //BaseColor
];

export function calcColor(item) {
  const today = new Date();
  const itemDate = new Date(item.deadline);
  var calcDistance = -(Math.ceil((today - itemDate) / (1000 * 3600 * 24)) - 1);

  if (calcDistance > 7) {
    // Dadline noch mehr als 7 Tage entfernt
    return "rgb(255, 255, 255, 1)"; // Weiß
  } else {
    if (calcDistance < 0) return "rgb(250, 0, 0)";
    return colorSpectrum[calcDistance];
  }
}
