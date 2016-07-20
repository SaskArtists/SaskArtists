var navOpen = false;
function openNav(){
  var navBar = document.getElementById('navBar');
  if(navOpen){
    navBar.style.display = 'none';
  }
  else{
    navBar.style.display = 'inline';
  }
  navOpen = !navOpen;
}
