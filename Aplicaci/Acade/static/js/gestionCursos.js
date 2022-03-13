(function () {
    const btnEliminar= document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn =>{
        btn.addEventListener('click', (e) =>{
            const confirmacion= confirm('¿Usuario desea la eliminacion del curso?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
    
})();