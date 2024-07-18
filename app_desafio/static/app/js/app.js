
document.addEventListener("DOMContentLoaded", function() {
    // Adicionar confirmação para deletar
    const deleteForms = document.querySelectorAll("form.delete-form");
    deleteForms.forEach(function(form) {
        form.addEventListener("submit", function(event) {
            const confirmed = confirm("Tem certeza que deseja deletar este equipamento?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
});