async function login(){
    const email=document.getElementById('email').value ;
    const password=document.getElementById('password').value;
    const message=document.getElementById('message');
    if(!email || !password){
        message.className='text-danger  text-center mt-3'
        message.innerText="Please fill all fields";
        return;

    }
    try{
        const res= await fetch('/auth/login',{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                email,
                password
            })
        })
        const data= await res.json()
        if(! res.ok ){
            message.className='text-danger  text-center mt-3';
            message.innerHTML = data.detail || "Login failed!!";
            return;

        }
        localStorage.setItem('token',data.access_token)
        message.className='text-success text-center mt-3';
        message.innerHTML="Login successfull redirecting....";
        setTimeout(() => {
            document.location.href="/todos-page";
        }, 1000);
    }catch(error){
        message.className='text-danger text-center mt-3';
        message.innerHTML='Something went wrong!!';
    }
}