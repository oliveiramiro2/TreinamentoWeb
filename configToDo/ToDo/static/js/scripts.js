$(document).ready(() => {
    //search 
    const campo   = document.getElementById("search");
    let tamanho = 256
    const searchBtn = $('#search-btn')
    const searchForm = $('#search-form')
    //url base e filtro
    const baseUrl = 'http://localhost:8000/'
    const filter = $('#filter')

    //search
    campo.setSelectionRange(tamanho, tamanho)

    $(search).on('keyup', function() {
        searchForm.submit()
    })


    //filtro
    $(filter).change( function() {
        let filter = $(this).val()
        window.location.href = baseUrl + '?filter=' + filter
    })
})
