import { DataGrid } from '@material-ui/data-grid'
import { useEffect, useState } from 'react'

const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'sensorName', headerName: 'Sensor', width: 130},
    { field: 'sensorValue', headerName: 'Reading', width: 130},
    { field: 'sensorUnit', headerName: 'Unit', width: 130},
];

export default function DataTable() {
    const [sensorData, setSensorData] = useState([]);
    const [seconds, setSeconds] = useState([]);

    useEffect(() => {
        fetch("sensor_readings").then(response =>
            response.json().then(data => {
                console.log(data)
                setSensorData(data)
            })
        );
    }, [seconds]);

    useEffect(()=>{
        const interval = setInterval(() => {
            setSeconds(seconds => seconds + 1);
        },1000);
        return() => clearInterval(interval);
    },[]);

    return (
        <div style={{ height: 500, width: 465}}>
            <DataGrid rows={sensorData} columns = {columns} pageSize={13} />
        </div>
    );
}