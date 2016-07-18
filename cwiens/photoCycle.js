var photoNumber = 0;
var numOfPhotos;
var photoList=["OutdoorChapel.jpg","CBCBroadcastCenter.jpg","TeePee.jpg","UofRHeatPlant.jpg","StJRCChurch.jpg","CASandS.JPG"];
var photoDescriptions=["A chapel in Silton, Saskatchewan. Designed by Clifford Wiens in 1969.","The CBC Broadcast Center in Regina. Designed in 1983.", "One of many spiral teepee's designed by Clifford Wiens. The teepees are found in various Saskatchewan parks.","The University of Regina Heating and Cooling Plant. Designed in 1967.","St. Joseph's Roman Catholic Church. Designed by Clifford Wiens in 1959","The Cathedral Art School and Studio, found in Regina, on Albert Street."]

function updatePhoto(cycleNum){
		document.getElementsByClassName("cycleImage")[cycleNum].src=photoList[photoNumber];
		document.getElementsByClassName("cycleText")[cycleNum].innerHTML=photoDescriptions[photoNumber];
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