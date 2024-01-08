const scripts = document.querySelectorAll('.after-load');

document.addEventListener('DOMContentLoaded', () => {
    const getDataPromeses = [
        getDoc(doc = 'AdministrativeOffencesCode'),
        getDoc(doc = 'CriminalCode')
    ];

    Promise.all(getDataPromeses).then(() => {
        loadScriptsSequentially()
    });
});

function loadScriptsSequentially(index = 0) {
    if (index < scripts.length) {
        const script = scripts[index];
        const newScriptSrc = script.dataset.src;

        const newScript = document.createElement('script');
        newScript.src = newScriptSrc;
        newScript.onload = () => {
            console.log(newScriptSrc + ' loaded!');
            script.remove();
            loadScriptsSequentially(index + 1);
        };

        document.head.appendChild(newScript);
    } else {
        console.log('LOADED')
        updatePage(page);
    }
}

async function getDoc(doc) {
    const ChapterTemplate = document.querySelector(`.${doc}Chapter`);
    const LeftBarItemTemplate = document.querySelector(`.${doc}LeftBarItems`).querySelector('a');
    const OffenceTemplate = document.querySelector(`.${doc}Offence`);

    const data = await getData(doc = `${doc}`);
    data.forEach(element => {
        const chapter = JSON.parse(element['chapter'])[0];
        const offences = JSON.parse(element['offences']);

        pasteChapter(chapter, template = ChapterTemplate, doc = doc);
        pasteLeftBarItem(chapter, template = LeftBarItemTemplate, doc = doc);
        pasteOffence(offences, template = OffenceTemplate, doc = doc);
    });
    ChapterTemplate.remove();
    document.querySelector(`.${doc}LeftBarItems`).removeChild(LeftBarItemTemplate);
    OffenceTemplate.remove();
}

async function getData(doc) {
    const administrativeOffencesCodeGetLink = window.location.origin + document.querySelector(`#${doc}`).dataset.getLink;
    let data = JSON.parse(sessionStorage.getItem(`${doc}`));

    if (!data) {
        try {
            const response = await fetch(administrativeOffencesCodeGetLink);
            data = await response.json();
            sessionStorage.setItem(`${doc}`, JSON.stringify(data));
        } catch (error) {
            console.error(error);
        }
    }

    return data;
}

function pasteChapter(chapter, template, doc) {
    const copiedChapterTemplate = template.cloneNode(true);
    const copiedText = copiedChapterTemplate.innerHTML;
    let replacedText = copiedText.replace(/\$ChapterNumber\$/g, chapter.fields.number);
    replacedText = replacedText.replace(/\$ChapterName\$/g, chapter.fields.name);
    const newChapter = document.createElement('div');
    newChapter.innerHTML = replacedText;
    newChapter.classList.add('RightItem');
    document.getElementById(`${doc}Div`).appendChild(newChapter);
}

function pasteLeftBarItem(chapter, template, doc) {
    const newLeftBarItem = template.cloneNode(true);
    const html = newLeftBarItem.outerHTML.replace(/\$ChapterNumber\$/g, chapter.fields.number)
        .replace(/\$ChapterName\$/g, chapter.fields.name);
    const temp = document.createElement('div');
    temp.innerHTML = html;
    temp.firstChild.classList.remove('visually-hidden');
    document.querySelector(`.${doc}LeftBarItems`).appendChild(temp.firstChild);
}

function pasteOffence(offences, template, doc) {
    let count = 0;
    offences.forEach(offence => {
        const copiedTemplate = template.cloneNode(true);
        const copiedText = copiedTemplate.innerHTML;

        let replacedText = copiedText;

        Object.entries(offence.fields).forEach(function ([key, value]) {
            let regex = new RegExp(`\\$Offence${snakeToCamel(key)}\\$`, 'g');
            if (key.includes('conjunction')) {
                if (value == 'OR') {
                    value = 'или';
                } else if (value == 'AND') {
                    value = 'и'
                }
            }
            replacedText = replacedText.replace(regex, value);
        });

        replacedText = replacedText.replace(/\$OffenceAdditionID\$/g, `${doc}AdditionID` + offence.fields.chapter + count);

        const newOffence = document.createElement('div');
        newOffence.innerHTML = replacedText;

        Object.entries(offence.fields).forEach(function ([key, value]) {
            if (key) {
                const item = newOffence.querySelector(`.Offence${snakeToCamel(key)}`);
                if (item && value) {
                    item.classList.remove('visually-hidden');
                }
            }
        });

        document.getElementById(`${doc}Div`).querySelector(`#${doc}` + offence.fields.chapter).parentNode.insertAdjacentElement('beforeend', newOffence);
        count++;
    });
}

function snakeToCamel(str) {
    return str.replace(/([-_]\w)/g, (match) => match.charAt(1).toUpperCase())
        .replace(/_/g, '')
        .replace(/^[a-z]/, (match) => match.toUpperCase());
}