import React from 'react';
import ReactDOM from 'react-dom/client'; // React 18+ import
import App from './App';
import './styles/App.css'; // Adjust the path if necessary
import * as serviceWorker from './serviceWorker';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);

// Register service worker for PWA capabilities
serviceWorker.register();
