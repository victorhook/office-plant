function Camera() {

    const BACKEND_URL = document.URL.split(':')[0] + ':5000';

    const take_photo = () => {
        fetch(`${BACKEND_URL}/take_picture`,
        {
            method: 'POST'
        })
        .then(res => console.log(res))
    }

    return (
        <div>
            <img className="img-fluid" src={`${BACKEND_URL}/static/img.png`}></img>
            <button onClick={take_photo}>Take photo</button>
        </div>
    )
}

export default Camera;
