$(document).ready(() => {
    //search 
    const searchBtn = $('#search-btn')
    const searchForm = $('#search-form')
    //url base e filtro
    const baseUrl = 'http://localhost:8000/'
    const filter = $('#filter')

    //search 
    $(searchBtn).on('click', function() {
        searchForm.submit()
    })

    //filtro
    $(filter).change(this).val()
    console.log(filter)
    window.location.href = baseUrl + '?filter=', filter
})
