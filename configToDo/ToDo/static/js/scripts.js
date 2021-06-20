$(document).ready(() => {
    //search variaveis
    const searchBtn = $('#search-btn')
    const searchForm = $('#search-form')

    $(searchBtn).on('click', () => {
        searchForm.subit()
    })
})
