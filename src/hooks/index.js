import axios from "axios";

const HookContext =  () => {
    const lidarCall = async () => {
        return await axios.get('/perfrom_lidar_scan');
    };

    const resetArduino = async() => {
        return await axios.get('/reset_arduino');
    };

    return {
        lidarCall, resetArduino
     }
}

export default HookContext;