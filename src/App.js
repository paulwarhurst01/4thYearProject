import './App.css';
import NavBar from './components/NavBar'
import VideoFeed from './components/VideoFeed'
import useKey from './components/KeyPress';

function App() {
  useKey();

  return (
    <div>
      <NavBar />
      <VideoFeed />
    </div>
  );
}

export default App;