var ws = new WebSocket( "ws://" + document.location.hostname + ":9000");

function connect(){
    ws = new WebSocket( "ws://" + document.location.hostname + ":9000");
    ws.onmessage = function(e)
    {
        incomingData = JSON.parse( e.data );
        console.log(incomingData)

        console.log(window.location)

        if (incomingData.Command == "WifiPage") {
            console.log(incomingData.Data)
            if(window.location != "http://192.168.1.138:5000/WifiPage"){
                window.location = "http://192.168.1.138:5000/WifiPage";
            }
            else{
                console.log("Wifi sayfasında")
                for (const [key, value] of Object.entries(incomingData.Data)) {
                    console.log(`${key}: ${value}`);
                  }
            }
            
        }
        else if(incomingData.Command == "VisihelpPage"){
            if(window.location != "http://192.168.1.138:5000/VisihelpPage"){
                window.location = "http://192.168.1.138:5000/VisihelpPage";
            }
        }

        


    }

    ws.onopen = function(e)
    {
        console.log( "ws open" );
    }

    ws.onclose = function(e)
    {
        console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
        setTimeout(function() {
            connect();
          }, 1000);
    
    }

    ws.onerror = function( e )
    {
        console.log( "ws error" );
    };


}

connect();
