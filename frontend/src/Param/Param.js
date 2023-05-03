function Param({ name, value, unit }) {
    return (
        <div className="d-flex justify-content-start align-items-center flex-row fs-2">
            <span className="m-2">{ name }:</span>
            <span className="m-2 fs-1">{ value }</span>
            <span className="m-2">{ unit }</span>  
        </div>
    )
}

export default Param;
