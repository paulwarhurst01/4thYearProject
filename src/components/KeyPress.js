import { useEffect } from 'react'

function useKey() {
    useEffect(() => {
        function handleKeyDown(event){
            switch (event.code){
                case "KeyW":
                    //console.log("W key pressed.");
                    ReturnKey("W");
                    break;
                case "KeyA":
                    //console.log("A key pressed");
                    ReturnKey("A")
                    break;
                case "KeyS":
                    //console.log("S key pressed");
                    ReturnKey("S")
                    break;
                case "KeyD":
                    //console.log("S key pressed");
                    ReturnKey("D")
                    break;
                default:
                    break;
            }
        }
    
        function handleKeyUp(){
            console.log("Key released");
            ReturnKey("X")
        }

        document.addEventListener("keydown", handleKeyDown)
        document.addEventListener("keyup", handleKeyUp)
        return () => {
            document.removeEventListener("keydown", handleKeyDown);
            document.removeEventListener("keyup", handleKeyUp)
        }
    }, []);
}

async function ReturnKey(key){
    const response = await fetch('/control_listen', {
        method: 'POST',
        headers: {
            'Content-Type': 'text/html'
        },
        body: (key)
    });
    if (response.ok){
        console.log('response worked')
    }
}

export default useKey;