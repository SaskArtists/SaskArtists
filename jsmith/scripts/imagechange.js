$(function () {
  $("#frontpageimg").mouseenter(function(){
    $(this).attr("src","images/horse.jpg");
  }).mouseleave(function(){
    $(this).attr("src","images/dog.jpg");
  });
});
