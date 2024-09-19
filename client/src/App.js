import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import { ObjectRecognitionProvider } from './contexts/ObjectRecognitionContext';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import Header from './components/Header';
import Footer from './components/Footer';
import './styles/App.css'; // Correct path for CSS

const App = () => {
    return (
        <AuthProvider>
            <ObjectRecognitionProvider>
                <Router>
                    <div className="App">
                        <Header />
                        <main>
                            <Routes>
                                <Route path="/" element={<Home />} />
                                <Route path="/about" element={<About />} />
                                <Route path="/contact" element={<Contact />} />
                                {/* Add more routes as needed */}
                            </Routes>
                        </main>
                        <Footer />
                    </div>
                </Router>
            </ObjectRecognitionProvider>
        </AuthProvider>
    );
};

export default App;
