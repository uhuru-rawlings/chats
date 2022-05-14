const validateSignup = () =>{
    let username = document.getElementById("username");
    let contacts = document.getElementById("contacts");
    let userimage = document.getElementById("userimage");
    let passwords = document.getElementById("passwords");
    let cpasswords = document.getElementById("cpasswords");
    
    if(username.value.trim() === '' || contacts.value.trim() === '' || userimage.value.trim() === '' || passwords.value.trim() === '' || cpasswords.value.trim() === ''){
        if(username.value.trim() === ''){
            username.style.borderColor = "red";
            return false;
        }else if(contacts.value.trim() === ''){
            contacts.style.borderColor = "red";
            return false;
        }else if(userimage.value.trim() === ''){
            userimage.style.borderColor = "red";
            return false;
        }else if(passwords.value.trim() === ''){
            passwords.style.borderColor = "red";
            return false;
        }else{
            cpasswords.style.borderColor = "red";
            return false;
        }
    }else{ 
        if(passwords.value.trim() != cpasswords.value.trim()){
            document.getElementById("error").innerText = "password dont match.";
            return false;
        }
    }
}

const validateImage = () => {
    let userimage = document.getElementById("userimage").value.trim()
    console.log(userimage)
    let images = String(userimage)
        let images_array = images.split('')
        let accepted = ['jpg','png','jpeg']
        let len = images_array.length
        let ext = images_array[len - 3] + images_array[len - 2] + images_array[len -1]

        if(accepted[0] == ext || accepted[1] == ext || accepted[2] == ext){
            
        }else{
            document.getElementById("exterror").innerText = 'Error!. only jpg,png or jpeg accepted';
        }

}