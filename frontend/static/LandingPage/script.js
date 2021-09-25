let middle_navbar = document.querySelectorAll("#middle > .list-style");
middle_navbar.forEach(button => {
    button.onclick = () => {
        document.querySelector(".active").classList.remove("active")
        button.classList.add("active")

    }
})

