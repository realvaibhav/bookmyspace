var elemlist = document.getElementsByTagName('input');
for( var i = 0; i < elemlist.length; i++){
    elemlist[i].blur();
}

function  openDropdown1(){
    document.getElementsByClassName('drop-down-city')[0].classList.add('show');
    document.getElementsByClassName('fa-caret-down')[0].classList.add('rotate-svg');
}

window.onclick = function (event){
    if(!event.target.matches('.drop-down-city-input')){
        
        var dropdown = document.getElementsByClassName('drop-down-city');
        if(dropdown[0].classList.contains('show')){
            dropdown[0].classList.remove('show');
            document.getElementsByClassName('fa-caret-down')[0].classList.remove('rotate-svg');
        }
    }
    else if(!event.target.matches('.drop-down-places-input')){
        
        var dropdown = document.getElementsByClassName('drop-down-places');
        if(dropdown[0].classList.contains('show-suggestion')){
            dropdown[0].classList.remove('show-suggestion');
        }
    }
}

function  openDropdown2(){
    document.getElementsByClassName('drop-down-places')[0].classList.add('show-suggestion');
}

// window.onclick = function (event){
//     if(!event.target.matches('.drop-down-places-input')){
//         alert("test");
//         var dropdown = document.getElementsByClassName('drop-down-places');
//         if(dropdown[0].classList.contains('show-suggestion')){
//             dropdown[0].classList.remove('show-suggestion');
//         }
//     }
// }

function getLocation(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(displayPosition);
    }
    else{
        alert("location permission not granted");
    }
}

function displayPosition(Position){
    alert("your location \nLat: " + Position.coords.latitude + "\nLong: " + Position.coords.longitude);
}