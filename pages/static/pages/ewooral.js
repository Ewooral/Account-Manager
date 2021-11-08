
let buttons = document.getElementsByClassName("Rectangle175");
let aboutPageInfo = document.getElementById("about-page-info");
let element = document.getElementsByClassName("element")
let section = document.getElementsByClassName("section-beutifier")
let kontainer = document.getElementsByClassName("containerisation")
let toPosition = kontainer.offsetTop;

buttons[0].addEventListener('click', scrollToFirst); 
buttons[1].addEventListener('click', scrollToSecond);
buttons[2].addEventListener('click', scrollToThird); 
buttons[3].addEventListener('click', scrollToFourth);
buttons[4].addEventListener('click', scrollToFifth); 


function scrollToFirst (){
 aboutPageInfo.style.transform = "translateY(0px)";
 
    for( i =0; i<5; i++){
        buttons[i].classList.remove("active")
    }
    this.classList.add("active")
}

 function scrollToSecond (){
 aboutPageInfo.style.transform = "translateY(-400px)"
    for(i=0; i<5; i++){
        buttons[i].classList.remove("active")
    }

    this.classList.add("active")

}

function scrollToThird(){
 aboutPageInfo.style.transform = "translateY(-800px)"
    for(i=0; i<5; i++){
        buttons[i].classList.remove("active")
    }
    this.classList.add("active")

}
 function scrollToFourth(){
 aboutPageInfo.style.transform = "translateY(-1200px)"
    for(i=0; i<5; i++){
        buttons[i].classList.remove("active")
    }
    this.classList.add("active")
}

function scrollToFifth (){
 aboutPageInfo.style.transform = "translateY(-1600px)"
    for(i =0; i<5; i++){
        buttons[i].classList.remove("active")
    }
    this.classList.add("active")
}



