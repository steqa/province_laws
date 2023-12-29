function splitTextIntoChunks(text, chunkSize) {
    const words = text.split(' ');
    const chunks = [];
    let currentChunk = '';

    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        const potentialChunk = `${currentChunk}${word} `;
        
        if (potentialChunk.length <= chunkSize) {
            currentChunk = potentialChunk;
        } else {
            chunks.push(currentChunk);
            currentChunk = `${word} `;
        }
    }

    if (currentChunk.length > 0) {
        chunks.push(currentChunk.trim());
    }

    return chunks;
}

const copyTextIndicator = document.getElementById('copyText');
const copyTextIcon = copyTextIndicator.querySelector('#copyTextIcon');
const copiedTextIcon = copyTextIndicator.querySelector('#copiedTextIcon');

function highlightText() {
    const textContainers = document.querySelectorAll('.copied-text-container');
    textContainers.forEach(textContainer => {
        const text = textContainer.innerText;
        const chunks = splitTextIntoChunks(text, 132);
    
        textContainer.innerHTML = '';
    
        chunks.forEach(chunk => {
            const span = document.createElement('span');
            span.textContent = chunk;
            span.classList.add('copied-text')
            textContainer.appendChild(span);
        });
    });

    const spans = document.querySelectorAll('.copied-text');
    
    spans.forEach(span => {
        span.addEventListener('mouseover', (event) => {
            copyTextIndicator.style.display = 'block';
            updateCopyTextIndicatorPosition(event);
        });
    
        span.addEventListener('mouseleave', () => {
            copyTextIndicator.style.display = 'none';
            copyTextIcon.style.display = 'block';
            copiedTextIcon.style.display = 'none';
        });
        
        span.addEventListener('mousemove', (event) => {
            updateCopyTextIndicatorPosition(event);
        });
        
        span.addEventListener('click', () => {
            const textToCopy = span.textContent;
            navigator.clipboard.writeText(textToCopy)
                .then(() => {
                    copyTextIcon.style.display = 'none';
                    copiedTextIcon.style.display = 'block';
                })
                .catch(err => {
                    console.error('Не удалось скопировать текст:', err);
                });
        });
    });
}

function updateCopyTextIndicatorPosition(event) {
    copyTextIndicator.style.top = `${event.clientY + window.scrollY}px`;
    copyTextIndicator.style.left = `${event.clientX + window.scrollX + 20}px`;
}

document.addEventListener('DOMContentLoaded', highlightText);
