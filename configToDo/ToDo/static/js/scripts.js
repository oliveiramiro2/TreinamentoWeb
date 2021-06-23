$(document).ready(() => {
    //search 
    const searchBtn = $('#search-btn')
    const searchForm = $('#search-form')
    //url base e filtro
    const baseUrl = 'http://localhost:8000/'
    const filter = $('#filter')

    //search 
    console.log(searchBtn)
    $(searchBtn).on('click', () => {
        searchForm.submit()
    })

    //filtro
    $(filter).change( function() {
        let filter = $(this).val()
        window.location.href = baseUrl + '?filter=' + filter
    })
})
