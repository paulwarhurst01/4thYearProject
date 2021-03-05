import './App.css';
import NavBar from './components/NavBar'
import VideoFeed from './components/VideoFeed'
import useKey from './components/KeyPress';
import DataTable from './components/DataTable'
//import UpdateData from './components/DataTable'
//import { flexbox } from '@material-ui/system'
import Box from '@material-ui/core/Box'

function App() {
  useKey();

  return (
    <div style={{width: '100%'}}>
      <NavBar />
      <Box 
        display="flex"
        p={1} >
          <Box p={1} order={1}>
            <VideoFeed /> 
          </Box>
          <Box p={1} order={2}>
            <DataTable />
          </Box>
        </Box>
    </div>
  );
}

export default App;