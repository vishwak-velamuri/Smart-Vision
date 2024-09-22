import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { AuthProvider } from 'client/src/contexts/AuthContext';
import Home from 'client/src/pages/Home';
import About from 'client/src/pages/About';
import Contact from 'client/src/pages/Contact';
import Header from 'client/src/components/Header';
import Footer from 'client/src/components/Footer';
import 'client/src/styles/App.css'; // Correct path for CSS

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
