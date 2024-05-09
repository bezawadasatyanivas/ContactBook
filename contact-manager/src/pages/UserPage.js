const UserPage=({params})=>{
    return (
        <>
        <h1>Welcome..</h1>
    <p> {params.email}</p>
    <p> {params.password}</p>
    
    </>
    );

}

export default UserPage;