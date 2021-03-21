import { useEffect } from 'react'

// Include useState to send 'M' back if pan and tilt keys released

function useKey() {
    useEffect(() => {
        function handleKeyDown(event){
            switch (event.code){                        // Switch function 
                case "KeyW":
                    ReturnKey("W");                     // Calls ReturnKey function
                    break;
                case "KeyA":
                    ReturnKey("A");
                    break;
                case "KeyS":
                    ReturnKey("S");
                    break;
                case "KeyD":
                    ReturnKey("D");
                    break;
                case "KeyJ":
                    ReturnKey("J");
                    break;
                case "KeyK":
                    ReturnKey("K");
                    break;
                case "KeyL":
                    ReturnKey("L");
                    break;
                case "KeyI":
                    ReturnKey("I");
                    break;
                default:
                    break;
            }
        }
    
        function handleKeyUp(){                                     // Handles keyUp event
            console.log("Key released");                            // Prints to frontend console
            ReturnKey("X")                                          // Sends ASCII code for "X"
        }

        document.addEventListener("keydown", handleKeyDown)         // Adds event listener, calls handleKeyDown
        document.addEventListener("keyup", handleKeyUp)             // Adds event listener, calls handleKeyUp
        return () => {
            document.removeEventListener("keydown", handleKeyDown); // Clean up
            document.removeEventListener("keyup", handleKeyUp)      // Clean up
        }
    }, []);
}

async function ReturnKey(key){                          // Waits for a repsonse from receiver
    const response = await fetch('/control_listen', {
        method: 'POST',                                 // Tells backend frontend is posting
        headers: {                                      // defines data structure of sent data
            'Content-Type': 'text/html'
        },
        body: (key)                                     // Contents of data structure is the key passed
    });
    if (response.ok){                                   // Checks for acknowledge
        console.log('response worked')
    }
}

export default useKey;