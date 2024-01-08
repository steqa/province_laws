const navigationsBtns = document.querySelectorAll('.nl');
const chapters = document.querySelectorAll('.RightItem');

navigationsBtns.forEach(btn => {
    btn.addEventListener('click', (event) => {
        navigationsBtns.forEach(navBtn => {
            navBtn.classList.remove('active');
        });
        event.preventDefault();
        btn.classList.add('active');
        scrollToElement(btn);
    });
});

function scrollToElement(btn) {
    const element = document.querySelector(btn.getAttribute('href'));
    const offset = 80;
    const elementPosition = element.getBoundingClientRect().top;
    window.scrollTo({
        top: window.pageYOffset + elementPosition - offset,
        behavior: 'smooth'
    });
}

function goToFirstElement() {
    const currentPage = document.querySelector('.pages').querySelector('div[style*="display: block;"] > div');
    const firstNavigationBtn = currentPage.querySelector('.nl');
    firstNavigationBtn.classList.add('active');
    scrollToElement(firstNavigationBtn);
}

window.addEventListener('scroll', (event) => {
    let visibleChapters = [];

    chapters.forEach(element => {
        let displayCheck = false;
        let parentElement = element.parentElement;

        while (parentElement) {
            const display = window.getComputedStyle(parentElement).getPropertyValue('display');
            if (display === 'none') {
                displayCheck = true;
                break;
            }
            parentElement = parentElement.parentElement;
        }

        if (!displayCheck) {
            visibleChapters.push(element);
        }
    });

    const upperChapters = [];
    for (let i = 0; i < visibleChapters.length; i++) {
        const bottom = visibleChapters[i].getBoundingClientRect().bottom;
        if (bottom <= window.innerHeight * 0.35) {
            upperChapters.push(i);
        }
    }

    navigationsBtns.forEach(btn => {
        btn.classList.remove('active');
    });

    let title = null;
    if (upperChapters.length === 0) {
        title = visibleChapters[0].querySelector('h5');
    } else {
        title = visibleChapters[upperChapters[upperChapters.length - 1] + 1].querySelector('h5');
    }
    document.querySelector(`a[href="#${title.id}"]`).classList.add('active');
});
