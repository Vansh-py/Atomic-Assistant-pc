console.log("Script file is loaded")


element_list = [document.getElementsByClassName("alkaline") , document.getElementsByClassName('alkali') , document.getElementsByClassName('transition') , 
    document.getElementsByClassName('post-transition') , document.getElementsByClassName('non-metal') , document.getElementsByClassName('non-metal') ,
    document.getElementsByClassName('noble') , document.getElementsByClassName('lanthanide') , document.getElementsByClassName('actinide') , document.getElementsByClassName('metalloid') , 
    document.getElementsByClassName('unknown')
]
console.log(element_list)



function alkali() {
    clearHighlights()
    
    var elements = document.getElementsByClassName('alkali');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}



function alkaline() {
    clearHighlights()
    var elements = document.getElementsByClassName('alkaline');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}


function transition() {
    clearHighlights()
    var elements = document.getElementsByClassName('transition');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}

function post() {
    clearHighlights()
    var elements = document.getElementsByClassName('post-transition');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}


function non() {
    clearHighlights()
    var elements = document.getElementsByClassName('non-metal');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}

function noble() {
    clearHighlights()
    var elements = document.getElementsByClassName('noble');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}


function lanthanides() {
    clearHighlights()
    var elements = document.getElementsByClassName('lanthanide');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}


function actinides() {
    clearHighlights()
    var elements = document.getElementsByClassName('actinide');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}

function unknown() {
    clearHighlights()
    var elements = document.getElementsByClassName('alkaline');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}


function metalloids() {
    clearHighlights()
    var elements = document.getElementsByClassName('metalloid');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}

function unknown() {
    clearHighlights()
    var elements = document.getElementsByClassName('unknown');
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add('highlight');
    }
}


function clearHighlights() {
    const highlightedElements = document.querySelectorAll('.highlight');
    highlightedElements.forEach(element => {
        element.classList.remove('highlight');
    });
}   


