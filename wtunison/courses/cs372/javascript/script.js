// script.js
// Copyright © 2002 Gabriel Boyer
// 07/31/2002 

var winCount  = 0;
var winHandle = null;

// function to open pop-up window containing image (simple version; replaced by openImgPopup)
function openImgPopupSimple(imgSrc, imgWidth, imgHeight, imgTitle) {
    // Close any existing window created by this function
    closeImgPopup();
    // Create a unique window name for each pop-up created
    var winName = "ImgPopup" + winCount++;
    // Create string of window options, adjusting the size of the window to fit the passed image dimensions
    var winOptions = "toolbar=no,scrollbars=no,resizable=no,width=" + (parseInt(imgWidth) + 20) + ",height=" + (parseInt(imgHeight) + 25);
    // Open the image in a pop-up window with the defined options
    winHandle = window.open(imgSrc, winName, winOptions);
    // If a title is passed, give the window that title
    if(imgTitle != null) winHandle.document.title = imgTitle;      
}

// function to open site-consistent image pop-up
function openImgPopup(imgSrc, imgWidth, imgHeight, imgTitle, resizeFlag) {
    // Function works incorrectly in Opera; use openImgPopupSimple()
    if(navigator.appName == "Opera") { 
        openImgPopupSimple(imgSrc, imgWidth, imgHeight, imgTitle);
    }
    else {
        // Close any existing window created by this function
        closeImgPopup();
        // Create a unique window name for each pop-up created
        var winName = "ImgPopup" + winCount++;
        // If no image title is passed, set the title to be the image path
        if(imgTitle == null) imgTitle = imgSrc;   
        // Set the maximum image dimensions that can fit on the screen at the current resolution
        var maxWidth  = screen.width - 130;
        var maxHeight = screen.height - (parseInt(screen.height * (250 / screen.height))); // accounts for scaling size of Start Menu
        var resizeLink = "";
        if(resizeFlag == null) resizeFlag = false;
        // If the image exceeds screen dimensions, present the option to resize
        if(imgWidth > maxWidth || imgHeight > maxHeight) {
            // If the option to resize has been selected, resize the image
            if(resizeFlag) {
                // Set default scale variable to 1 (no change in image size)
                var scale = 1;
                // If the image is too wide, calculate the proper scale to resize the image
                if(imgWidth > maxWidth && imgHeight < maxHeight) {
                    scale = maxWidth / imgWidth;                      
                }
                // If the image is too high, calculate the proper scale to resize the image
                else if(imgHeight > maxHeight && imgWidth < maxWidth) {
                    scale = maxHeight / imgHeight;
                }
                // If the image is both too high and too wide, calculate the proper scale to resize the image
                else if(imgWidth > maxWidth & imgHeight > maxHeight) {
                    var widthScale = (maxWidth / imgWidth);
                    var heightScale = (maxHeight / imgHeight); 
                    if(widthScale <= heightScale) scale = widthScale;
                    else scale = heightScale;
                }  
                // Scale the image dimensions
                imgWidth  = imgWidth * scale;
                imgHeight = imgHeight * scale;
            }
            var titleArray = imgTitle.split(' ');
            // Create link to open image again, this time resized
            resizeLink = "<br>[ <a href='#null' onClick=opener.openImgPopup('";
            resizeLink += imgSrc + "'," + imgWidth + "," + imgHeight + ",'";
            for(var i = 0; i < titleArray.length; i++) { 
                resizeLink += titleArray[i];
                if(i != (titleArray.length - 1)) resizeLink += "%20";
            }  
            resizeLink += "',true)>Resize image to fit screen</a> ]";
        }  
        // Create string of window options, adjusting the size of the window to fit the passed image dimensions
        var winOptions = "toolbar=no,scrollbars=yes,resizable=yes,";
        // If the image is more narrow than the main table can contract, size the window appropriately
        if(imgWidth <= 325) winOptions += "width=450";
        // Otherwise, simply size the window to fit the image and expanded main table
        else winOptions += "width=" + (parseInt(imgWidth) + 120);
        // Assign window a height appropriate to the image    
        winOptions += ",height=" + (parseInt(imgHeight) + 190);
        // Open the image in a pop-up window with the defined options
        winHandle = window.open(null, winName, winOptions);
        // Move the window to the top-left corner to maximize usable screen space
        winHandle.moveTo(0,0);
        // Contruct page HTML
        var strHTML = "<html>";
        strHTML += "<head>";
        strHTML += "<meta http-equiv='Content-Type' content='text/html;'>";
        strHTML += "<link rel='stylesheet' type='text/css' href='css/styles.css' title='style1'>";
        strHTML += "</head>";
        strHTML += "<body>";
        strHTML += "<table border=0 cellpadding=0 cellspacing=0 align='center'>";
        strHTML += "  <tr>";
        strHTML += "    <td background='images/top_left.gif' height=50></td>";
        strHTML += "    <td background='images/top_span.gif' height=50><img src='images/top_trunc.gif' width=300 height=50></td>";
        strHTML += "    <td background='images/top_right.gif' height=50></td>";
        strHTML += "  </tr>";
        strHTML += "  <tr>";
        strHTML += "    <td background='images/left.gif' width=30></td>";
        strHTML += "    <td bgcolor='#FFFFFF' valign='top' class='main'>";
        strHTML += "      <center>";
        // If the image was resized, format imgTitle to remove the '%20's and insert the proper spaces
        if(resizeFlag) {
            var formatTitle = imgTitle.split('%20');
            imgTitle = "";
            for(var j = 0; j < formatTitle.length; j++) {
                imgTitle += formatTitle[j];
                if(j != (formatTitle.length - 1)) imgTitle += " ";
            }
            strHTML += imgTitle;
        }
        // If the image was not resize, ignore the above
        else { 
            strHTML += imgTitle;
        }
        // If the image is not resize already, display the resize link
        if(!resizeFlag) strHTML += resizeLink; 
        strHTML += "      </center><br>";
        strHTML += "      <center><img src='" + imgSrc + "' width=" + parseInt(imgWidth) + " height=" + parseInt(imgHeight) + " border=1></center>";
        strHTML += "      <br>";
        strHTML += "      <center><a href='#null' onClick='self.close()'>Close window</a></center>";
        strHTML += "    </td>";
        strHTML += "    <td background='images/right.gif' width=30></td>";
        strHTML += "  </tr>";
        strHTML += "  <tr>";
        strHTML += "    <td background='images/bottom_left.gif' height=50></td>";
        strHTML += "    <td background='images/bottom_span.gif' height=50 align='right'></td>";
        strHTML += "    <td background='images/bottom_right.gif' height=50></td>";
        strHTML += "  </tr>";
        strHTML += "</table>";
        strHTML += "</body>";
        strHTML += "</html>";    
        // Write strPage to newly created window    
        winHandle.document.write(strHTML);
        // Assign imgTitle as the title of the window
        winHandle.document.title = imgTitle;
    }
}

// function to close pop-up window created by 'openImgPopup'
function closeImgPopup() {
    // If the browser is NOT an early version of MSIE,
    if((navigator.appName != "Microsoft Internet Explorer") || (parseInt(navigator.appVersion) >= 4))
        // and if the window exists, 
        if(winHandle != null)
            // and if the window is not closed already, close the window.
            if(!winHandle.closed) winHandle.close();
}
