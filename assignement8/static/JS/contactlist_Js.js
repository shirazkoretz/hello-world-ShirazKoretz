
fetch('https://reqres.in/api/users?page=2').then(response => response.json() )
.then(responseJSON=>createUsersList(responseJSON.data)).catch(err=>console.log(err));


function createUsersList(users) {
    console.log(users);
    const curr_main = document.querySelector("main");
    for (let user of users) {
        const section = document.createElement("section");
        section.innerHTML = `
<div>
${user.first_name}
</div>

`;
        curr_main.appendChild(section);
    }
}
