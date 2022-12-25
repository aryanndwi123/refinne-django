
var findMyState =() =>{
    

    var success=(position)=>{
        console.log(position)
        var latitude =position.coords.latitude;
        var longitude = position.coords.longitude;
        console.log(latitude +''+longitude)
        document.getElementById('id1').value = latitude+' '+longitude;
        location.replace('https://www.google.com/maps?saddr='+latitude+','+longitude+'&daddr=The+square+one+cafe')
        
        
    }
    

    navigator.geolocation.getCurrentPosition(success);
    
    
}



document.querySelector('.find-state').addEventListener('click',findMyState);
