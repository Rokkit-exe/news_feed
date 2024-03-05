import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import NewsFeed from './pages/NewsFeed';
import NewsArticle from './pages/NewsArticle';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/news" element={<NewsFeed />} />
        <Route path="/news/:id" element={<NewsArticle />} />
      </Routes>
    </Router>
  );
}

export default App;
