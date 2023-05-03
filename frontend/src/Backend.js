class Backend {
    // TODO: Clean :)
    static port = 5000;
    static apiUrl = window.location.protocol + '//' + window.location.host.split(':')[0] + `:${Backend.port}/api`

    static fetch_samples(callback) {
        Backend._fetch('samples', callback);
    }

    static _fetch(target, callback) {
        let url = `${Backend.apiUrl}/${target}`;
        console.log(`Fetching: ${url}`);

        fetch(url, {
            method: 'GET'
        })
        .then(res => res.json())
        .then(json => {
            callback({
                result: 'ok',
                data: json
            });
        })
        .catch(err => {
            console.log(`Error: ${err}`);
            callback({result: 'error'});
        })
    }

}

export default Backend;