$(document).ready(() => {
    //search 
    const searchBtn = $('#search-btn')
    const searchForm = $('#search-form')

    $(searchBtn).on('click', function() {
        searchForm.submit()
    })
})
