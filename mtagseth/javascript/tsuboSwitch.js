var unfolded = true;
function toggleTsubo(){
  tsubo = document.getElementById('tsubo');
  if(unfolded){
    tsubo.src = 'images/tsuboUnfold.jpg';
    tsubo.style.width = '700px';
  }
  else{
    tsubo.src = 'images/TSUBO.jpg'
    tsubo.style.width = '300px';
  }
  unfolded = !unfolded;
}
