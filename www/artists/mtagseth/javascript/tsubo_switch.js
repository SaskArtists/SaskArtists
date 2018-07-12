var unfolded = true;
function toggleTsubo(){
  tsubo = document.getElementById('tsubo');
  if(unfolded){
    tsubo.src = 'images/tsubo_unfold.jpg';
    tsubo.style.width = '700px';
  }
  else{
    tsubo.src = 'images/tsubo_fold.jpg'
    tsubo.style.width = '300px';
  }
  unfolded = !unfolded;
}
