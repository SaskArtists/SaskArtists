var i = 0; var path = new Array();

// LIST OF IMAGES
path[0] = "./img/wife.jpg";
path[1] = "./img/Bol14.jpg";
path[2] = "./img/Bol9.jpg";
path[3] = "./img/bol1.jpg";
path[4] = "./img/wbolen.jpg";
path[5] = "./img/pot.jpg";

function imageForward() {
  document.slide.src = path[i];
  if(i>=5){
    i=0;
  }else{
    i++;
  }



}

function imageBack() {
  document.slide.src = path[i];
  if(i<=1){
    i=0;
  }else{
    i--;
  }

}
