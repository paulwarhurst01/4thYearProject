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

    useEffect(() => {
        fetch("sensor_readings").then(response =>
            response.json().then(data => {
                console.log(data)
                setSensorData(data)
            })
        );
    }, []);

    return (
        <div style={{ height: 400, width: 465}}>
            <DataGrid rows={sensorData} columns = {columns} pageSize={5} />
        </div>
    );
}