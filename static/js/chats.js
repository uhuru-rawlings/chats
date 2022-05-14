const toogleAddContact = () => {
    let target = document.getElementById("addform");
    if(target.style.display == "block"){
        target.style.display = "none";
        document.getElementById("addbtn").innerHTML = "<i class='fa-solid fa-plus'></i>"
    }else{
        target.style.display = "block";
        document.getElementById("addbtn").innerHTML = "<i class='fa-solid fa-xmark'></i>"
    }
}
