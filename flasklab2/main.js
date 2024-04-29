let svg = document.querySelector("svg");
let rects = document.querySelectorAll("rect");

rects.forEach(rect => {
  rect.addEventListener("mouseenter", e => {
    svg.appendChild(rect);
  });
});
