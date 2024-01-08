const title = document.querySelector('title');
const pageBtns = document.querySelectorAll('.pageBtn');
const loadSpinner = document.getElementById('loadSpinner');

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
    loadSpinner.style.display = 'none';
    if (page === 'AdministrativeOffencesCode') {
        title.innerText = 'КоАП';
        AdministrativeOffencesCode.style.display = 'block';
        CriminalCode.style.display = 'none';
    } else if (page === 'CriminalCode') {
        title.innerText = 'УК';
        AdministrativeOffencesCode.style.display = 'none';
        CriminalCode.style.display = 'block';
    }
    if ('scrollRestoration' in history) {
        history.scrollRestoration = 'manual';
    }
    goToFirstElement();
}