import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Landing from './pages/Landing';
import Adopt from './pages/Adopt';
import Nav from './components/nav';

function App() {
  return (
    <Router>
      <Nav />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/adopt" element={<Adopt />} />
      </Routes>
    </Router>
  );
}

export default App;

