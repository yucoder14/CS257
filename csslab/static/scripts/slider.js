const sliders = document.querySelectorAll('.slider'); 
const colormat = document.querySelector('.colormat');

const rgba = document.querySelector('#rgba'); 
const redValue = rgba.querySelector('#redvalue'); 
const greenValue = rgba.querySelector('#greenvalue'); 
const blueValue = rgba.querySelector('#bluevalue'); 
const opacityValue = rgba.querySelector('#opacityvalue'); 

const knobSize = 60;
const sliderHeight = 300; 

sliders.forEach((slider) => {
	const knob = slider.querySelector('.knob'); 
	const rand = Math.random();
	const scale = knob.getAttribute('scale');
	knob.style.top = `${sliderHeight * rand - knobSize/2}px`;
	
	knob.setAttribute('data-value', scaleSlider(rand,scale));
	dragElement(knob); 
	knob.setAttribute('id', slider.getAttribute('id'));
	}); 

function initRGBA() {
	const red = sliders.item(0).querySelector('.knob')
														 .getAttribute('data-value');
	const green = sliders.item(1).querySelector('.knob')
											 				 .getAttribute('data-value');
	const blue = sliders.item(2).querySelector('.knob')
															.getAttribute('data-value');
	const opacity = sliders.item(3).querySelector('.knob')
								    						 .getAttribute('data-value');
	redValue.innerHTML = red;  
	greenValue.innerHTML = green; 
	blueValue.innerHTML = blue; 
	opacityValue.innerHTML = opacity; 
	
	colormat.style.background = `rgba(${red},${green},${blue},${opacity})`;
}

function scaleSlider(raw,scale) {
	let dataValue = raw * scale;		
	
	if (scale == 255) {
		dataValue = dataValue.toFixed(0);
	} else {
		dataValue = dataValue.toFixed(1);
	}

	return dataValue; 
}

function dragElement(ele) {
  let color = ele.getAttribute('id') + "value";
	
	let pos1 = 0, pos2 = 0;
 
  ele.onmousedown = dragMouseDown;

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    pos2 = e.clientY;
    document.onmouseup = closeDragElement;
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
		const spanId = ele.getAttribute('id') + "value"; 
    const color = rgba.querySelector(`#${spanId}`); 
		const scale = ele.getAttribute('scale');		
		
		e = e || window.event;
    e.preventDefault();
    pos1 = pos2 - e.clientY;
    pos2 = e.clientY;
		
		const min = 0 - knobSize/2, max = sliderHeight - knobSize/2; 
		let newHeight = ele.offsetTop - pos1; ; 	
	
		if (newHeight < min) {	
			newHeight = min; 
		} else if (newHeight > max) {
			newHeight = max; 
		}
		
		const raw = (newHeight +  knobSize/2)/sliderHeight;		
		const dataValue = scaleSlider(raw,scale);			
	
		color.innerHTML = dataValue;	
		ele.setAttribute('data-value', dataValue);
    ele.style.top = newHeight + "px";
  }

  function closeDragElement() {
    document.onmouseup = null;
    document.onmousemove = null;
  }
}


const callback = (mutationList) => {
	const red = redValue.innerHTML; 
	const green = greenValue.innerHTML; 
	const blue = blueValue.innerHTML; 
	const opacity = opacityValue.innerHTML; 
	
	colormat.style.background = `rgba(${red},${green},${blue},${opacity})`;
}


initRGBA();

const config = {
	subtree: true,
	childList: true,
	characterData: false,
	attribues: false
}; 

const observer = new MutationObserver(callback);
observer.observe(rgba, config); 
