var photoNumber = 0;
var numOfPhotos;
var photoList=[];
var photoDescriptions=[];

function updatePhoto(cycleNum){
		document.getElementsByClassName("CycleImage")[cycleNum].src=photoList[photoNumber];
		document.getElementsByClassName("CycleText")[cycleNum].innerHTML=photoDescriptions[photoNumber];
}

function nextPhoto(cycleNum){

	if(photoNumber<photoList.length-1){
		photoNumber++;
	}
	else if(photoNumber==photoList.length-1){
		photoNumber=0;
	}
	updatePhoto(cycleNum);
}


function lastPhoto(cycleNum){
	if(photoNumber>0){
		photoNumber--;
	}
	else if(photoNumber==0){
		photoNumber=photoList.length-1;
	}
	updatePhoto(cycleNum);
}