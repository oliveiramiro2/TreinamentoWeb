$(document).ready(() => {
    //search 
    const searchBtn = $('#search-btn')
    const searchForm = $('#search-form')

    searchBtn.style = 'background-color=blue;'

    $(searchBtn).on('click', () => {
        searchForm.subit()
    })
})
