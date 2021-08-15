function makeYellow(){
    document.body.style.backgroundColor='yellow'
}

    //  event handler
const blueButton=document.getElementById('make-blue');
blueButton.onclick=makeBlue;
const grayButton=document.getElementById('make-gray');
grayButton.onclick=makeGray;

function makeBlue(){
    document.body.style.backgroundColor="blue"
}
function makeGray(){
    document.body.style.backgroundColor='gray'
}

// anonimus function
const blackButton=document.getElementById('make-black-button');
blackButton.onclick=function (){
    document.body.style.backgroundColor='black';
}

// handle add envent listener
goldenRodButton=document.getElementById('make-golden-rod');
goldenRodButton.addEventListener('click',goldenRod);

function goldenRod(){
    document.body.style.backgroundColor='goldenrod';
}

    // add event listener 
const gotpickButton=document.getElementById('make-gotpink-button');
gotpickButton.addEventListener('click', function (){
    document.body.style.backgroundColor='hotpink'
})

// Direct action
document.getElementById('make-lightblue-button').addEventListener('click', function(){
    document.body.style.backgroundColor='lightblue'
})
