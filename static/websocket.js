var ws = new WebSocket( "ws://" + document.location.hostname + ":9000");

function connect(){
    ws = new WebSocket( "ws://" + document.location.hostname + ":9000");
    ws.onmessage = function(e)
    {
        incomingData = JSON.parse( e.data );
        console.log(incomingData)
        if (incomingData.Command == "networks") {
            console.log("networks")
            

            for (let i = 0; i < incomingData.Data.length; i++) {
                console.log( i)
                var template = document.getElementById('network-template')
                var clon = template.content.cloneNode(true);
                var section = document.getElementById("content")
                section.appendChild(clon)
                div = document.getElementById('network')
                div.id = "network" + i.toString()
                div.innerText = incomingData.Data[i]
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
