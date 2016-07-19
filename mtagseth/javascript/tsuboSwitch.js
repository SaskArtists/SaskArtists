var unfolded = false;
function toggleTsubo(){
  tsubo = document.getElementById('tsubo');
  if(unfolded){
    tsubo.src = 'images/tsuboUnfold.jpg'
    console.log()
  }
  else{
    tsubo.src = 'images/TSUBO.jpg'
  }
}
