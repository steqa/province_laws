const title = document.querySelector('title');
const pageBtns = document.querySelectorAll('.pageBtn');

const AdministrativeOffencesCode = document.getElementById('AdministrativeOffencesCode');
const CriminalCode = document.getElementById('CriminalCode');

let page = 'AdministrativeOffencesCode';
document.querySelector('[data-page="AdministrativeOffencesCode"]').classList.add('active');

function handler(btn) {
    page = btn.dataset.page;
    updatePage(page);
    pageBtns.forEach(pageBtn => {
        pageBtn.classList.remove('active');
    });
    btn.classList.add('active');
}

function updatePage(page) {
    if (page === 'AdministrativeOffencesCode') {
        title.innerText = 'КоАП';
        AdministrativeOffencesCode.style.display = 'block';
        CriminalCode.style.display = 'none';
    } else if (page === 'CriminalCode') {
        title.innerText = 'УК';
        AdministrativeOffencesCode.style.display = 'none';
        CriminalCode.style.display = 'block';
    }
    goToFirstElement();
}

document.addEventListener('DOMContentLoaded', updatePage(page));