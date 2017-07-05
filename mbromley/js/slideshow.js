var i = 0; var path = new Array();

// LIST OF IMAGES
path[0] = "./img/625 Georgia Woman s.JPG";
path[1] = "./img/626 Bamboo II s.JPG ";
path[2] = "./img/627 Broadway Woman II s.JPG";
path[3] = "./img/629 Burr  Criuse Ship s.JPG";
path[4] = "./img/630 Bamboo Hole s.JPG";
path[5] = "./img/631 Window Flowerbed s.JPG";
path[6] = "./img/632 Grnvll Stop 3 Women s.JPG"

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
