function init() {
    if (document.addEventListener) {
       document.addEventListener("keyup",keyup,false);
    }
    else if (document.attachEvent) {
       document.attachEvent("onkeyup", keyup);
    }
    else {
       document.onkeyup= keyup;
    }
}

function keyup(e) {
	if (!e) {
		e = event;
	}
	switch(e.keyCode){
		case 40: //keydown
			next_slide();
			break;
		case 32: //space
			next_slide();
			break;
		case 39: //right
			next_slide();
			break;			
		case 38: //up
			prev_slide();
			break;			
		case 37: //left
			prev_slide();
			break;			
	}
}

function next_slide(){
	location.href = $("a#next_link").attr("href");
}

function prev_slide(){
	location.href = $("a#prev_link").attr("href");
}

