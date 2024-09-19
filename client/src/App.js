import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import { ObjectRecognitionProvider } from './contexts/ObjectRecognitionContext';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import Header from './components/Header';
import Footer from './components/Footer';
import 'Smart-Vision/client/src/App.js';

const App = () => {
    return (
        <AuthProvider>
            <ObjectRecognitionProvider>
                <Router>
                    <div className="App">
                        <Header />
                        <main>
                            <Switch>
                                <Route path="/" exact component={Home} />
                                <Route path="/about" component={About} />
                                <Route path="/contact" component={Contact} />
                                {/* Add more routes as needed */}
                            </Switch>
                        </main>
                        <Footer />
                    </div>
                </Router>
            </ObjectRecognitionProvider>
        </AuthProvider>
    );
};

export default App;