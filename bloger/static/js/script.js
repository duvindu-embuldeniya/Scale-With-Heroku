// alert("hellow world!");

let form = document.getElementById('form')
let pages = document.getElementsByClassName('page')

for(let i=0; i<pages.length; i++){
    pages[i].addEventListener('click', function(e){
        e.preventDefault()

        let page = this.dataset.page

        form.innerHTML += `<input type='text' name='page' value=${page}>`
        
        form.submit();
    })
}