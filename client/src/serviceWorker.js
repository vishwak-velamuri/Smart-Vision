const isLocalhost = Boolean(
    window.location.hostname === 'localhost' ||
    // [::1] is the IPv6 localhost
    window.location.hostname === '[::1]' ||
    // 127.0.0.0/8 are considered localhost for IPv4
    window.location.hostname.match(
        /^127(?:\.\d+){0,2}\.\d+$/
    )
);

const register = (config) => {
    if ('serviceWorker' in navigator) {
        const publicUrl = new URL(process.env.PUBLIC_URL, window.location);
        if (publicUrl.origin !== window.location.origin) {
            return;
        }

        window.addEventListener('load', () => {
            const swUrl = `${process.env.PUBLIC_URL}/service-worker.js`;

            if (isLocalhost) {
                checkValidServiceWorker(swUrl, config);
            } else {
                registerValidSW(swUrl, config);
            }
        });
    }
};

const registerValidSW = (swUrl, config) => {
    navigator.serviceWorker
        .register(swUrl)
        .then((registration) => {
            registration.onupdatefound = () => {
                const installingWorker = registration.installing;
                if (installingWorker == null) {
                    return;
                }
                installingWorker.onstatechange = () => {
                    if (installingWorker.state === 'installed') {
                        if (navigator.serviceWorker.controller) {
                            console.log(
                                'New content is available; please refresh.'
                            );
                            if (config && config.onUpdate) {
                                config.onUpdate(registration);
                            }
                        } else {
                            console.log('Content is cached for offline use.');
                            if (config && config.onSuccess) {
                                config.onSuccess(registration);
                            }
                        }
                    }
                };
            };
        })
        .catch((error) => {
            console.error('Error during service worker registration:', error);
        });
};

const checkValidServiceWorker = (swUrl, config) => {
    fetch(swUrl, {
        headers: { 'Service-Worker': 'script' },
    })
        .then((response) => {
            const contentType = response.headers.get('content-type');
            if (
                response.status === 404 ||
                (contentType != null && contentType.indexOf('javascript') === -1)
            ) {
                navigator.serviceWorker.ready.then((registration) => {
                    registration.unregister().then(() => {
                        window.location.reload();
                    });
                });
            } else {
                registerValidSW(swUrl, config);
            }
        })
        .catch(() => {
            console.log(
                'No internet connection found. App is running in offline mode.'
            );
        });
};

const unregister = () => {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.ready
            .then((registration) => {
                registration.unregister();
            })
            .catch((error) => {
                console.error(error.message);
            });
    }
};

export { register, unregister };