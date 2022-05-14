const removeError = (targets) => {
   let user = document.getElementById(targets);
   if(user.value.trim() != ''){
       user.style.borderColor = "#CED4DA";
   }
}

const validateLogin = () =>{
    let contact = document.getElementById("contact");
    let password = document.getElementById("password");
    let rememberme = document.getElementById("remember");

    if(contact.value.trim() === '' || password.value.trim() === ''){
        if(contact.value.trim() === ''){
            contact.style.borderColor= 'red';
            return false;
        }else{
            password.style.accentColor.borderColor = 'red';
            return false;
        }
    }else{
        if(rememberme.checked){
            let credentials = {
                'contact':contact.value.trim(),
                'password':password.value.trim()
            }
            localStorage.setItem("user",JSON.stringify(credentials))
        }
    }
}

const setUser = () =>{
    let userd = localStorage.getItem("user")
    if(userd){
        let obj = JSON.parse(userd)
        document.getElementById("contact").value = obj.contact;
        document.getElementById("password").value = obj.password;
    }
}

window.onload = setUser;