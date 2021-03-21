import axios from "axios";

const HookContext =  () => {
    const lidarCall = async () => {
        return await axios.get('/perfrom_lidar_scan');
    };

    const resetArduino = async() => {
        return await axios.get('/reset_arduino');
    };

    const resetMotors = async() => {
        return await axios.get('/reset_motor_controller');
    };

     return {
         lidarCall, resetArduino, resetMotors
     }

}

export default HookContext;