const Slider = document.getElementById("Slider");
let SliderValue = 1;
Slider,addEventListener("input", () => {
    SliderValue = Number(Slider.value);
});
console.log(SliderValue);